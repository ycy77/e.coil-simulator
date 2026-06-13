#!/usr/bin/env python3
"""Use the local vLLM-served Qwen3.5-9B to mine E. coli UniProt
FUNCTION annotations for graph edges.

The current v2 dump carries FUNCTION text inline (one block per
entity) but never split it into structured edges. We batch
each protein's annotation into a JSON extraction request to
vLLM and parse the response.

Extraction targets (one prompt, six edge classes):
  * "regulates":   activator / repressor of a named gene or
                   protein
  * "binds":       binds a named molecule, cofactor, or
                   protein
  * "subunit_of":  belongs to a named protein complex
  * "catalyzes":   catalyzes a named reaction
  * "transports":  transports a named substrate
  * "interacts":   generic physical / functional interaction

The output is a JSON list of
``{source_name, relation, target_name, evidence}`` per
protein. We then resolve each name to a baseline entity via
the canonical name index and emit an edge.

Usage:
    python scripts/llm_extract_edges.py --limit 200
    python scripts/llm_extract_edges.py              # all eligible
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENTS = PROJECT_ROOT / "data" / "normalized" / "simulation" / "entities.csv"
DEFAULT_EDGES = PROJECT_ROOT / "data" / "normalized" / "simulation" / "edges.csv"
DEFAULT_OUT = PROJECT_ROOT / "data" / "normalized" / "_v2" / "edges_llm.csv"
VLLM_URL = "http://127.0.0.1:8000/v1/chat/completions"
VLLM_MODEL = "/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B"

PROMPT_SYSTEM = (
    "You are a senior bioinformatics curator extracting structured "
    "edges from a single UniProt FUNCTION text. Output ONLY a JSON "
    "object, no prose. Schema:\n"
    "{\"source\": <this protein's gene name>, \"edges\": [\n"
    "  {\"rel\": \"regulates\"|\"binds\"|\"subunit_of\"|\"catalyzes\"|\"transports\"|\"interacts\",\n"
    "   \"target\": <target entity gene name as it appears in E. coli K-12>,\n"
    "   \"evidence\": <short verbatim quote from FUNCTION>}\n"
    "]}\n"
    "Rules:\n"
    "1. Only include edges the FUNCTION text *explicitly* supports.\n"
    "2. Target names must be E. coli K-12 gene symbols (lowercase 3-5 letter mnemonic like 'asnA', 'lrp', 'rpoH'). If a name is ambiguous or generic (e.g. 'DNA', 'RNA'), skip it.\n"
    "3. Self-edges are not allowed.\n"
    "4. If the FUNCTION text mentions 'this pseudogene' / 'fragment of X' or 'N-terminal/C-terminal fragment of X', include an edge rel='fragment_of' target=X.\n"
    "5. The protein's own name is the one given in the prompt; do not invent a different one."
)

PROMPT_USER_TEMPLATE = (
    "Gene: {name}\n"
    "FUNCTION: {function}\n"
    "Extract the edges."
)


def call_vllm(name: str, function: str, retries: int = 3) -> Optional[dict]:
    """Call vLLM and parse the JSON response. Returns None on failure."""
    import urllib.request
    body = {
        "model": VLLM_MODEL,
        "messages": [
            {"role": "system", "content": PROMPT_SYSTEM},
            {"role": "user", "content": PROMPT_USER_TEMPLATE.format(name=name, function=function[:3500])},
        ],
        "temperature": 0.0,
        "max_tokens": 2500,  # Qwen3 emits a long <think> chain; need headroom
    }
    payload = json.dumps(body).encode("utf-8")
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                VLLM_URL, data=payload, headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read())
            text = result["choices"][0]["message"]["content"]
            return _parse_json_response(text)
        except Exception as e:
            if attempt == retries - 1:
                print(f"  vllm error for {name}: {e}", file=sys.stderr)
                return None
            time.sleep(1 + attempt)


def _parse_json_response(text: str) -> Optional[dict]:
    """LLMs sometimes wrap JSON in fences, prepend a <think>
    block (Qwen3), or add other prose. Strip the
    <think>...</think> block, then find the first balanced
    { ... } block and parse it."""
    # Strip the Qwen3 chain-of-thought block.
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Try a fence-stripped parse first
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, re.DOTALL)
    if fence:
        try:
            return json.loads(fence.group(1))
        except json.JSONDecodeError:
            pass
    # Try the whole string
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    # Find the first balanced { ... } block
    start = cleaned.find("{")
    if start == -1:
        return None
    depth = 0
    in_str = False
    escape = False
    for i in range(start, len(cleaned)):
        c = cleaned[i]
        if in_str:
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_str = False
            continue
        if c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                snippet = cleaned[start:i+1]
                try:
                    return json.loads(snippet)
                except json.JSONDecodeError:
                    return None
    return None


# Valid edge relations (in the curation schema)
_VALID_RELATIONS = {
    "regulates", "binds", "subunit_of", "catalyzes",
    "transports", "interacts", "fragment_of",
}
# Mapped to the relation_type vocabulary used in our edge files
RELATION_MAP = {
    "regulates": "regulates",
    "binds": "binds",
    "subunit_of": "is_subunit_of",
    "catalyzes": "catalyzes",
    "transports": "transports",
    "interacts": "interacts",
    "fragment_of": "paralog_of",
}


def build_edge_rows(parsed: dict, name_to_id: Dict[str, List[str]]) -> List[dict]:
    """Resolve the LLM response to concrete entity IDs and emit
    edge rows. Skip any target that does not resolve to a
    baseline entity (we want quality over recall)."""
    if not parsed:
        return []
    edges = parsed.get("edges") or []
    src = parsed.get("source") or ""
    src_ids = name_to_id.get(src.lower(), [])
    if not src_ids:
        return []
    src_id = src_ids[0]
    rows = []
    seen: Set[Tuple[str, str, str]] = set()
    for e in edges:
        rel = (e.get("rel") or "").strip().lower()
        if rel not in _VALID_RELATIONS:
            continue
        target = (e.get("target") or "").strip()
        if not target:
            continue
        # Resolve target: case-insensitive lookup in our name index
        tgt_ids = name_to_id.get(target.lower(), [])
        if not tgt_ids:
            continue
        tgt_id = tgt_ids[0]
        if tgt_id == src_id:
            continue
        mapped = RELATION_MAP[rel]
        triple = (src_id, tgt_id, mapped)
        if triple in seen:
            continue
        seen.add(triple)
        rows.append({
            "source_id": src_id,
            "target_id": tgt_id,
            "relation_type": mapped,
            "direction": "directed",
            "evidence": (e.get("evidence") or "")[:200],
            "source_database": "UniProt",
            "source_record_id": src_id,
            "notes": f"LLM-extracted from FUNCTION; rel={rel}",
            "reaction_id": "", "reactants": "", "products": "",
            "ec_number": "", "pathway": "",
        })
    return rows


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entities", type=Path, default=DEFAULT_ENTS)
    p.add_argument("--edges", type=Path, default=DEFAULT_EDGES)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p.add_argument("--limit", type=int, default=0,
                   help="Process at most N proteins (0 = all eligible)")
    p.add_argument("--degree-le", type=int, default=2,
                   help="Process only proteins with degree <= this many (default 2)")
    p.add_argument("--offset", type=int, default=0,
                   help="Skip the first N selected proteins")
    p.add_argument("--rate-per-sec", type=float, default=4.0,
                   help="Throttle vLLM requests")
    args = p.parse_args()

    print(f"[1/4] reading entities and edges ...")
    ents = list(csv.DictReader(args.entities.open(encoding="utf-8")))
    edges = list(csv.DictReader(args.edges.open(encoding="utf-8")))

    # Build a lowercase name -> ids index for resolution
    name_to_id: Dict[str, List[str]] = defaultdict(list)
    for e in ents:
        nm = (e.get("name") or "").strip()
        if nm:
            name_to_id[nm.lower()].append(e["entity_id"])

    # Compute degree per entity from the *current* edge set
    deg: Counter = Counter()
    for e in edges:
        deg[e["source_id"]] += 1
        deg[e["target_id"]] += 1

    # Pick proteins with FUNCTION text and low degree
    candidates = [
        e for e in ents
        if e["entity_type"] == "protein"
        and (e.get("annotation") or "").strip()
        and deg.get(e["entity_id"], 0) <= args.degree_le
    ]
    candidates.sort(key=lambda e: (deg.get(e["entity_id"], 0), e["entity_id"]))
    print(f"      {len(candidates)} proteins with degree <= {args.degree_le} and FUNCTION text")

    if args.offset:
        candidates = candidates[args.offset:]
    if args.limit:
        candidates = candidates[:args.limit]
    print(f"      processing {len(candidates)} (offset={args.offset}, limit={args.limit})")

    print(f"[2/4] calling vLLM at {VLLM_URL} ...")
    new_rows: List[dict] = []
    n_parsed = 0
    n_skipped_invalid = 0
    t0 = time.time()
    interval = 1.0 / max(args.rate_per_sec, 0.5)
    for i, e in enumerate(candidates):
        function = e.get("annotation", "")
        # Trim to the FUNCTION block only; the rest is noise.
        function = function.split("SUBCELLULAR LOCATION")[0]
        function = function.split("SUBUNIT:")[0]
        parsed = call_vllm(e["name"], function)
        if parsed is None:
            n_skipped_invalid += 1
            continue
        n_parsed += 1
        new_rows.extend(build_edge_rows(parsed, name_to_id))
        if (i + 1) % 10 == 0:
            rate = (i + 1) / (time.time() - t0 + 1e-6)
            eta = (len(candidates) - i - 1) / max(rate, 0.1)
            print(f"      [{i+1}/{len(candidates)}] {n_parsed} parsed, "
                  f"{n_skipped_invalid} invalid, "
                  f"{len(new_rows)} new edges, "
                  f"rate {rate:.1f}/s, ETA {eta:.0f}s")
        time.sleep(interval)

    print(f"[3/4] de-duping against existing edges ...")
    existing = {(e["source_id"], e["target_id"], e["relation_type"]) for e in edges}
    new_unique: List[dict] = []
    for r in new_rows:
        triple = (r["source_id"], r["target_id"], r["relation_type"])
        if triple not in existing:
            new_unique.append(r)
            existing.add(triple)

    print(f"[4/4] writing {len(new_unique)} unique LLM-extracted edges to {args.out} ...")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "source_id", "target_id", "relation_type", "direction", "evidence",
            "source_database", "source_record_id", "notes",
            "reaction_id", "reactants", "products", "ec_number", "pathway",
        ])
        w.writeheader()
        for r in new_unique:
            w.writerow(r)

    elapsed = time.time() - t0
    print()
    print("=" * 50)
    print(f"  processed:        {len(candidates)}")
    print(f"  parsed:          {n_parsed}")
    print(f"  invalid json:    {n_skipped_invalid}")
    print(f"  raw edges:       {len(new_rows)}")
    print(f"  unique (no dup): {len(new_unique)}")
    print(f"  elapsed:         {elapsed:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
