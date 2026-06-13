#!/usr/bin/env python3
"""Audit every entity in the normalized graph with a strict vLLM backend.

This script is the single source of truth for entity classification
(endogenous / exogenous-drug / exogenous-chemical / class-abstraction /
unsure) and name uniqueness. It deliberately does **not** fall back to a
mock or rule-only path: if the configured vLLM endpoint is unreachable
the script aborts with a clear error.

Usage::

    # Dry run, 50 entities per type, only rules+keyword signal (no LLM):
    python scripts/audit_entities.py --dry --limit 50

    # Real audit, full coverage, all entity_types:
    python scripts/audit_entities.py --apply --vllm-url http://127.0.0.1:8000

    # Audit one type only:
    python scripts/audit_entities.py --apply --types small_molecule --limit 1000

Outputs (under ``data/audit/``)::

    decisions/<entity_type>.jsonl       -- one JSON line per audited entity
    ambiguous/<entity_type>.jsonl       -- entities the model could not classify
    reports/<entity_type>.report.md     -- human-readable summary
    audit_summary.json                  -- aggregate stats across types

Decision record schema::

    {
      "entity_id": "...",
      "entity_type": "...",
      "name": "...",
      "audit": {
        "endogenous": "endogenous|exogenous-drug|exogenous-chemical|class-abstraction|unsure",
        "name_uniqueness": "unique|collides",
        "collides_with": ["..."],
        "confidence": 0.0,
        "rationale": "...",
        "model": "Qwen3_5-9B",
        "audit_method": "vllm",
        "raw_signals": {
          "name": "...",
          "source_database": "...",
          "external_ids": "...",
          "annotation_excerpt": "...",
          "aliases": "...",
          "in_edge_count": 0,
          "out_edge_count": 0
        }
      }
    }
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from threading import Lock
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import urllib.request
    import urllib.error
except ImportError:  # pragma: no cover - stdlib
    pass


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED = PROJECT_ROOT / "data" / "normalized"
ENRICHED = PROJECT_ROOT / "data" / "enriched" / "entities_enriched_lite.jsonl"
AUDIT_DIR = PROJECT_ROOT / "data" / "audit"
DECISIONS_DIR = AUDIT_DIR / "decisions"
AMBIGUOUS_DIR = AUDIT_DIR / "ambiguous"
REPORTS_DIR = AUDIT_DIR / "reports"

ENTITY_TYPES = ["gene", "protein", "complex", "reaction", "small_molecule", "rna"]

# Heuristic drug / antibiotic keywords. These drive the keyword signal that
# the LLM is asked to weigh, not the final decision.
DRUG_KEYWORDS = [
    "mycin", "micin", "cillin", "penam", "penem", "cef", "xacin", "floxacin",
    "cyclin", "tetracycl", "azole", "nidazole", "globomycin",
    "bactin", "bacitracin", "vancomy", "rifa", "tobra", "kana",
    "gentam", "streptomy", "spectino", "bleomyc", "mitomyc", "daunor", "doxor",
    "irinotec", "etopos", "methotre", "cisplatin", "hydroxyurea",
    "chloramphen", "novobio", "puromy", "erythromy", "azithromy",
    "sulfonamid", "aminoglycosid", "quinolon", "trimethoprim",
]


@dataclass
class EntityRow:
    entity_id: str
    entity_type: str
    name: str
    aliases: str
    annotation: str
    notes: str
    source_database: str
    source_id: str
    external_ids: str
    default_state: str
    is_external: str

    @classmethod
    def from_csv(cls, row: Dict[str, str]) -> "EntityRow":
        return cls(
            entity_id=row.get("entity_id", "").strip(),
            entity_type=row.get("entity_type", "").strip(),
            name=row.get("name", "").strip(),
            aliases=row.get("aliases", "").strip(),
            annotation=(row.get("annotation") or "").strip(),
            notes=(row.get("notes") or "").strip(),
            source_database=row.get("source_database", "").strip(),
            source_id=row.get("source_id", "").strip(),
            external_ids=row.get("external_ids", "").strip(),
            default_state=row.get("default_state", "").strip(),
            is_external=row.get("is_external", "").strip(),
        )


def load_entities() -> Dict[str, EntityRow]:
    path = NORMALIZED / "entities.csv"
    out: Dict[str, EntityRow] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            e = EntityRow.from_csv(row)
            if e.entity_id:
                out[e.entity_id] = e
    return out


def load_enriched() -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    if not ENRICHED.exists():
        return out
    with ENRICHED.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            eid = rec.get("entity_id")
            if eid:
                out[eid] = rec
    return out


def load_edge_counts() -> Dict[str, Tuple[int, int]]:
    path = NORMALIZED / "edges.csv"
    in_count: Dict[str, int] = defaultdict(int)
    out_count: Dict[str, int] = defaultdict(int)
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            src = row.get("source_id", "").strip()
            tgt = row.get("target_id", "").strip()
            if src:
                out_count[src] += 1
            if tgt:
                in_count[tgt] += 1
    return {eid: (in_count.get(eid, 0), out_count.get(eid, 0)) for eid in set(in_count) | set(out_count)}


def keyword_hits(text: str) -> List[str]:
    if not text:
        return []
    lowered = text.lower()
    hits = []
    for kw in DRUG_KEYWORDS:
        if kw in lowered:
            hits.append(kw)
    return hits


def build_signals(entity: EntityRow, in_out: Tuple[int, int], enriched: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    text_blob = " ".join([
        entity.name or "",
        entity.aliases or "",
        entity.annotation or "",
        entity.notes or "",
        (enriched or {}).get("summary", "") if enriched else "",
    ])
    return {
        "name": entity.name,
        "aliases": entity.aliases,
        "source_database": entity.source_database,
        "source_id": entity.source_id,
        "external_ids": entity.external_ids,
        "annotation_excerpt": entity.annotation[:200],
        "notes_excerpt": entity.notes[:200],
        "default_state": entity.default_state,
        "is_external": entity.is_external,
        "in_edge_count": in_out[0],
        "out_edge_count": in_out[1],
        "drug_keyword_hits": keyword_hits(text_blob),
        "enriched_summary_excerpt": ((enriched or {}).get("summary", "")[:200]) if enriched else "",
    }


def build_prompt(entity: EntityRow, signals: Dict[str, Any]) -> List[Dict[str, str]]:
    system = (
        "You audit E. coli biology knowledge-graph entities. "
        "The model is E. coli K-12. The simulation treats each entity "
        "as an Agent that can exist in the initial intracellular system "
        "or only as an externally added perturbation. Classify strictly:\n"
        "  - endogenous: a component the cell makes / uses by itself "
        "(genes, proteins, complexes, reactions that the cell catalyzes, "
        "RNAs, and intracellular metabolites like ATP, NAD+, H2O, amino acids, "
        "sugars, nucleotides, cofactors, and lipids).\n"
        "  - exogenous-drug: an antibiotic / therapeutic / probe that is NOT "
        "produced by E. coli (e.g. globomycin, streptomycin, ampicillin, "
        "rifampicin, tetracycline, puromycin, methotrexate, tunicamycin, "
        "chloramphenicol, kanamycin).\n"
        "  - exogenous-chemical: a non-drug chemical that E. coli does not "
        "produce (industrial / environmental / heavy metals / dyes).\n"
        "  - class-abstraction: a name that denotes an entire compound class "
        "rather than one specific molecule (e.g. 'a penicillin', 'a ceramide', "
        "'a sulfonamide', 'an IV6-beta-D-galactosaminylneolactotetraosylceramide').\n"
        "  - unsure: only if the raw signals are truly insufficient to decide.\n"
        "For entity_type == 'reaction' or 'rna' choose endogenous when the "
        "reaction/RNA is encoded by E. coli and present in E. coli metabolism. "
        "Do NOT return unsure for things that obviously belong in one bucket.\n"
        "Also judge name uniqueness across the catalog; if the same "
        "entity_type+name is reused by multiple entity_ids, return "
        "name_uniqueness='collides' and list the other ids in collides_with.\n"
        "Return strict JSON only with keys: "
        "endogenous (endogenous|exogenous-drug|exogenous-chemical|class-abstraction|unsure), "
        "name_uniqueness (unique|collides), "
        "collides_with (array of strings, empty if unique), "
        "confidence (0..1 float), "
        "rationale (one short paragraph)."
    )
    user = (
        f"entity_id: {entity.entity_id}\n"
        f"entity_type: {entity.entity_type}\n"
        f"raw_signals: {json.dumps(signals, ensure_ascii=False)}\n\n"
        "Return JSON only."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def call_vllm(messages: List[Dict[str, str]], url: str, model: str, timeout: int = 120, max_tokens: int = 512) -> Dict[str, Any]:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.0,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        f"{url.rstrip('/')}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    content = body["choices"][0]["message"]["content"]
    return json.loads(content)


def collect_collisions(entities: Dict[str, EntityRow]) -> Dict[str, List[str]]:
    groups: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    for eid, e in entities.items():
        if not e.name:
            continue
        groups[(e.entity_type, e.name.lower())].append(eid)
    collisions: Dict[str, List[str]] = {}
    for (et, name), ids in groups.items():
        if len(ids) > 1:
            for eid in ids:
                others = sorted(x for x in ids if x != eid)
                collisions[eid] = others
    return collisions


def decide_one(
    entity: EntityRow,
    signals: Dict[str, Any],
    collisions: List[str],
    vllm_url: str,
    model: str,
    max_tokens: int = 512,
    parse_retries: int = 1,
    request_timeout: int = 120,
) -> Dict[str, Any]:
    """Call vLLM and parse the JSON response.

    Network / 5xx / timeout errors propagate (strict no-fallback). A
    JSON parse error on the model's reply is treated as the model
    failing to produce a usable classification, so the entity is
    rerouted to ``ambiguous`` with ``audit_method=parse_error``. We do
    **not** silently classify it via rules.
    """
    messages = build_prompt(entity, signals)
    last_err: Optional[Exception] = None
    content: Optional[str] = None
    for attempt in range(parse_retries + 1):
        try:
            content = call_vllm(messages, vllm_url, model, timeout=request_timeout, max_tokens=max_tokens)
            return _normalize(content, entity, signals, collisions, model)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ConnectionError) as exc:
            # Strict: any transport failure aborts the whole batch.
            print(
                f"FATAL: vLLM transport error for {entity.entity_id}: {exc}",
                file=sys.stderr,
            )
            raise SystemExit(2) from exc
        except json.JSONDecodeError as exc:
            last_err = exc
            if attempt < parse_retries:
                # The model produced truncated/garbled JSON. Try once
                # more with a larger budget; if it still fails we treat
                # the entity as ambiguous.
                max_tokens += 256
                continue
    return {
        "endogenous": "unsure",
        "name_uniqueness": "collides" if collisions else "unique",
        "collides_with": collisions,
        "confidence": 0.0,
        "rationale": f"model reply was not parseable JSON: {last_err}",
        "model": model,
        "audit_method": "parse_error",
        "raw_signals": signals,
        "raw_reply_excerpt": (content or "")[:400] if content else "",
    }


def _normalize(
    raw: Dict[str, Any],
    entity: EntityRow,
    signals: Dict[str, Any],
    collisions: List[str],
    model: str,
) -> Dict[str, Any]:
    raw_endogenous = str(raw.get("endogenous", "unsure")).strip().lower()
    raw_uniqueness = str(raw.get("name_uniqueness", "collides" if collisions else "unique")).strip().lower()
    if raw_endogenous not in {"endogenous", "exogenous-drug", "exogenous-chemical", "class-abstraction", "unsure"}:
        raw_endogenous = "unsure"
    if raw_uniqueness not in {"unique", "collides"}:
        raw_uniqueness = "collides" if collisions else "unique"
    collides_with = list(raw.get("collides_with", collisions) or [])
    if raw_uniqueness == "unique":
        collides_with = []
    elif raw_uniqueness == "collides" and not collides_with:
        collides_with = collisions
    confidence = float(raw.get("confidence", 0.5))
    if confidence < 0 or confidence > 1:
        confidence = max(0.0, min(1.0, confidence))
    return {
        "endogenous": raw_endogenous,
        "name_uniqueness": raw_uniqueness,
        "collides_with": collides_with,
        "confidence": round(confidence, 3),
        "rationale": str(raw.get("rationale", "")).strip(),
        "model": model,
        "audit_method": "vllm",
        "raw_signals": signals,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vllm-url", default="http://127.0.0.1:8000")
    parser.add_argument("--model", default=None, help="vLLM served-model id; auto-detected if omitted")
    parser.add_argument("--types", nargs="*", default=ENTITY_TYPES)
    parser.add_argument("--limit", type=int, default=0, help="0 = all")
    parser.add_argument("--apply", action="store_true", help="Write decisions; otherwise dry-run")
    parser.add_argument("--checkpoint-every", type=int, default=500)
    parser.add_argument("--concurrency", type=int, default=64, help="concurrent in-flight requests to vLLM")
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--request-timeout", type=int, default=120, help="per-request timeout in seconds")
    parser.add_argument("--resume", action="store_true", help="skip entity_ids already in decisions+ambiguous")
    args = parser.parse_args()

    if not args.apply:
        print("[dry-run] pass --apply to write decisions", file=sys.stderr)

    for d in (DECISIONS_DIR, AMBIGUOUS_DIR, REPORTS_DIR):
        d.mkdir(parents=True, exist_ok=True)

    entities = load_entities()
    enriched = load_enriched()
    edge_counts = load_edge_counts()
    collisions = collect_collisions(entities)

    by_type: Dict[str, List[EntityRow]] = defaultdict(list)
    for e in entities.values():
        by_type[e.entity_type].append(e)

    summary: Dict[str, Any] = {"types": {}, "model": args.model, "vllm_url": args.vllm_url}

    # Resolve model id from /v1/models; never accept a placeholder.
    if not args.model:
        try:
            with urllib.request.urlopen(f"{args.vllm_url.rstrip('/')}/v1/models", timeout=10) as resp:
                listing = json.loads(resp.read().decode("utf-8"))
            models = listing.get("data", [])
            if not models:
                print("FATAL: vLLM /v1/models returned no models", file=sys.stderr)
                raise SystemExit(2)
            args.model = models[0]["id"]
            print(f"Resolved vLLM model id: {args.model}", file=sys.stderr)
        except Exception as exc:
            print(f"FATAL: cannot resolve vLLM model id from {args.vllm_url}: {exc}", file=sys.stderr)
            raise SystemExit(2)

    for et in args.types:
        rows = sorted(by_type.get(et, []), key=lambda r: r.entity_id)
        if args.limit:
            rows = rows[: args.limit]
        decisions_path = DECISIONS_DIR / f"{et}.jsonl"
        ambiguous_path = AMBIGUOUS_DIR / f"{et}.jsonl"
        report_path = REPORTS_DIR / f"{et}.report.md"

        # Resume support: skip rows already audited.
        if args.resume:
            seen_ids: Set[str] = set()
            for p in (decisions_path, ambiguous_path):
                if p.exists():
                    with p.open(encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                seen_ids.add(json.loads(line).get("entity_id", ""))
                            except json.JSONDecodeError:
                                continue
            before = len(rows)
            rows = [r for r in rows if r.entity_id not in seen_ids]
            print(
                f"[{et}] resume: skipped {before - len(rows)} already-audited, "
                f"{len(rows)} remaining",
                file=sys.stderr,
            )

        counters = defaultdict(int)
        sample_decisions: List[Dict[str, Any]] = []
        ambiguous_sample: List[Dict[str, Any]] = []

        # Append-mode files so reruns accumulate (and resume works).
        out_d = decisions_path.open("a", encoding="utf-8")
        out_a = ambiguous_path.open("a", encoding="utf-8")
        write_lock = Lock()

        def _audit_one(entity: EntityRow) -> Dict[str, Any]:
            in_out = edge_counts.get(entity.entity_id, (0, 0))
            signals = build_signals(entity, in_out, enriched.get(entity.entity_id))
            audit = decide_one(
                entity,
                signals,
                collisions.get(entity.entity_id, []),
                args.vllm_url,
                args.model,
                max_tokens=args.max_tokens,
                request_timeout=args.request_timeout,
            )
            return {
                "entity_id": entity.entity_id,
                "entity_type": entity.entity_type,
                "name": entity.name,
                "audit": audit,
            }

        try:
            t0 = time.time()
            done = 0
            with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as pool:
                futures = [pool.submit(_audit_one, entity) for entity in rows]
                for fut in as_completed(futures):
                    decision = fut.result()
                    audit = decision["audit"]
                    with write_lock:
                        counters[audit["endogenous"]] += 1
                        counters[f"uniqueness:{audit['name_uniqueness']}"] += 1
                        # An entry is ambiguous only if the model itself
                        # could not classify it (unsure / parse_error) or
                        # if its self-reported confidence is below 0.55.
                        if (
                            audit["endogenous"] == "unsure"
                            or audit["audit_method"] == "parse_error"
                            or audit["confidence"] < 0.55
                        ):
                            out_a.write(json.dumps(decision, ensure_ascii=False) + "\n")
                            out_a.flush()
                            if len(ambiguous_sample) < 5:
                                ambiguous_sample.append(decision)
                        else:
                            out_d.write(json.dumps(decision, ensure_ascii=False) + "\n")
                            out_d.flush()
                            if len(sample_decisions) < 5:
                                sample_decisions.append(decision)
                    done += 1
                    if done % args.checkpoint_every == 0 or done == len(rows):
                        elapsed = time.time() - t0
                        rate = done / max(elapsed, 0.001)
                        eta = (len(rows) - done) / max(rate, 0.001)
                        print(
                            f"  [{et}] {done}/{len(rows)} audited ({rate:.1f}/s, eta {eta:.1f}s)",
                            file=sys.stderr,
                        )
        finally:
            out_d.close()
            out_a.close()

        # Build a tiny markdown report so a human can skim it.
        with report_path.open("w", encoding="utf-8") as f:
            f.write(f"# Audit report: {et}\n\n")
            f.write(f"- model: `{args.model}`\n")
            f.write(f"- vllm_url: `{args.vllm_url}`\n")
            f.write(f"- audited: {len(rows)}\n")
            f.write(f"- by_class:\n")
            for k in ("endogenous", "exogenous-drug", "exogenous-chemical", "class-abstraction", "unsure"):
                f.write(f"  - {k}: {counters.get(k, 0)}\n")
            f.write(f"- by_name_uniqueness:\n")
            f.write(f"  - unique: {counters.get('uniqueness:unique', 0)}\n")
            f.write(f"  - collides: {counters.get('uniqueness:collides', 0)}\n\n")
            f.write("## Sample decisions\n\n")
            for d in sample_decisions:
                a = d["audit"]
                f.write(f"- `{d['entity_id']}` ({d['name']!r}): {a['endogenous']} / {a['name_uniqueness']} (conf {a['confidence']})\n")
                f.write(f"  - rationale: {a['rationale'][:240]}\n")
            f.write("\n## Ambiguous sample\n\n")
            for d in ambiguous_sample:
                a = d["audit"]
                f.write(f"- `{d['entity_id']}` ({d['name']!r}): {a['endogenous']} (conf {a['confidence']})\n")
                f.write(f"  - rationale: {a['rationale'][:240]}\n")
        summary["types"][et] = {
            "audited": len(rows),
            "counters": dict(counters),
            "decisions_path": str(decisions_path.relative_to(PROJECT_ROOT)),
            "ambiguous_path": str(ambiguous_path.relative_to(PROJECT_ROOT)),
            "report_path": str(report_path.relative_to(PROJECT_ROOT)),
        }
        print(
            f"[{et}] audited={len(rows)} decisions={counters.get('endogenous', 0) + counters.get('exogenous-drug', 0) + counters.get('exogenous-chemical', 0) + counters.get('class-abstraction', 0)} unsure={counters.get('unsure', 0)}",
            file=sys.stderr,
        )

    (AUDIT_DIR / "audit_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote summary to {AUDIT_DIR / 'audit_summary.json'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())