#!/usr/bin/env python3
"""Re-build enriched entity cards from canonicalized entities.

This is the second-generation enricher. It assumes ``canonicalize_v2``
has produced ``data/normalized/_v2/entities.csv`` (or promoted it
in-place) and rebuilds:

* ``data/enriched/entities_enriched_v2.jsonl``
* ``data/enriched/entities_enriched_v2_lite.jsonl``
* ``data/enriched/entities_enriched_v2_summary.csv``
* ``data/enriched/enrichment_report_v2.json``

The new enricher is multi-source: it walks every cross-source row for a
canonical entity (the ``merged_from`` field stores the original ids) and
joins annotations from UniProt, EcoCyc, KEGG, NCBI and RegulonDB into a
single ``raw_annotations`` block. The ``display_name`` is taken
verbatim from ``entities.csv.display_name`` so the on-screen labels
match the deduplicated ones produced by canonicalize_v2.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]


CORE_FIELDS = [
    "entity_id",
    "entity_type",
    "display_name",
    "canonical_name",
    "family_key",
    "aliases",
    "summary",
    "functional_context",
    "biological_role",
    "subcellular_location",
    "default_state",
    "allowed_states",
    "evidence_sources",
    "source_databases",
    "source_id",
    "external_ids",
    "linked_entities",
    "edge_context",
    "pathways",
    "raw_annotations",
    "merged_from",
    "is_exogenous",
    "quality",
]


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> int:
    n = 0
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            n += 1
    return n


def split_list(value: str, sep: str = "|") -> List[str]:
    if not value:
        return []
    out: List[str] = []
    for tok in value.replace(",", sep).replace(";", sep).split(sep):
        tok = tok.strip()
        if tok:
            out.append(tok)
    return out


def trim(text: str, limit: int) -> str:
    text = (text or "").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def classify_quality(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return "empty"
    lowered = text.lower()
    if lowered.startswith("ecocyc compound") or lowered.startswith("ecocyc complex") or lowered.startswith("ecocyc reaction") or lowered.startswith("ecocyc protein"):
        return "placeholder"
    if len(text) < 30 and "ncbirefseq" in lowered.replace(" ", "").lower():
        return "placeholder"
    if len(text) < 40:
        return "placeholder"
    return "informative"


def build_edges_index(edges: List[Dict[str, str]]) -> Tuple[Dict[str, List[Dict[str, str]]], Dict[str, List[Dict[str, str]]]]:
    out_edges: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    in_edges: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for e in edges:
        out_edges[e.get("source_id", "")].append(e)
        in_edges[e.get("target_id", "")].append(e)
    return out_edges, in_edges


def edge_context_for(entity_id: str, out_edges: Dict[str, List[Dict[str, str]]], in_edges: Dict[str, List[Dict[str, str]]]) -> Dict[str, Any]:
    incoming_by_relation: Dict[str, List[str]] = defaultdict(list)
    outgoing_by_relation: Dict[str, List[str]] = defaultdict(list)
    for e in in_edges.get(entity_id, []):
        rel = e.get("relation_type", "")
        incoming_by_relation[rel].append(e.get("source_id", ""))
    for e in out_edges.get(entity_id, []):
        rel = e.get("relation_type", "")
        outgoing_by_relation[rel].append(e.get("target_id", ""))
    return {
        "in_degree": sum(len(v) for v in incoming_by_relation.values()),
        "out_degree": sum(len(v) for v in outgoing_by_relation.values()),
        "incoming_by_relation": {k: sorted(set(v)) for k, v in incoming_by_relation.items()},
        "outgoing_by_relation": {k: sorted(set(v)) for k, v in outgoing_by_relation.items()},
    }


def derive_linked_entities(row: Dict[str, str], ec: Dict[str, Any]) -> Dict[str, List[str]]:
    linked: Dict[str, List[str]] = {}
    if row.get("entity_type") == "gene":
        for tgt in ec.get("outgoing_by_relation", {}).get("encodes", []):
            linked.setdefault("encoded_protein", []).append(tgt)
    elif row.get("entity_type") == "protein":
        for src in ec.get("incoming_by_relation", {}).get("encodes", []):
            linked.setdefault("encoding_genes", []).append(src)
    for rel in ("catalyzes", "is_component_of", "is_critical_for", "transports"):
        for tgt in ec.get("outgoing_by_relation", {}).get(rel, []):
            linked.setdefault(rel, []).append(tgt)
    return {k: sorted(set(v))[:60] for k, v in linked.items()}


def derive_summary(row: Dict[str, str], raw: Dict[str, Any], ec: Dict[str, Any]) -> str:
    parts: List[str] = []
    name = (row.get("display_name") or row.get("name") or row.get("entity_id") or "").strip()
    et = row.get("entity_type", "")
    if name:
        parts.append(f"{name} ({row.get('entity_id', '')}) is a {et} entity.")
    if raw.get("normalized_annotation"):
        parts.append(f"Normalized annotation: {raw['normalized_annotation']}")
    if raw.get("normalized_notes"):
        parts.append(f"Notes: {raw['normalized_notes']}")
    if raw.get("merged_aliases"):
        parts.append("Aliases: " + ", ".join(raw["merged_aliases"][:8]))
    if row.get("subcellular_location"):
        parts.append(f"Subcellular location: {row['subcellular_location']}")
    in_relations = ec.get("incoming_by_relation", {})
    out_relations = ec.get("outgoing_by_relation", {})
    if in_relations.get("represses"):
        parts.append(f"Repressed by: {', '.join(in_relations['represses'][:8])}")
    if in_relations.get("activates"):
        parts.append(f"Activated by: {', '.join(in_relations['activates'][:8])}")
    if out_relations.get("encodes"):
        parts.append(f"Encodes: {', '.join(out_relations['encodes'][:8])}")
    if out_relations.get("catalyzes"):
        parts.append(f"Catalyzes: {', '.join(out_relations['catalyzes'][:8])}")
    return trim(" ".join(parts), 1400)


def lite_card(card: Dict[str, Any]) -> Dict[str, Any]:
    keep = {
        "entity_id", "entity_type", "display_name", "canonical_name", "family_key",
        "summary", "aliases", "external_ids", "linked_entities",
        "evidence_sources", "source_databases", "is_exogenous", "quality",
    }
    return {k: v for k, v in card.items() if k in keep}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=PROJECT_ROOT / "data" / "normalized")
    parser.add_argument("--enriched-dir", type=Path, default=PROJECT_ROOT / "data" / "enriched")
    parser.add_argument("--apply-in-place", action="store_true")
    args = parser.parse_args()

    ndir = args.normalized_dir
    edir = args.enriched_dir

    entities = read_csv(ndir / "entities.csv")
    edges = read_csv(ndir / "edges.csv")
    out_e, in_e = build_edges_index(edges)

    cards: List[Dict[str, Any]] = []
    for row in entities:
        eid = row.get("entity_id", "")
        ec = edge_context_for(eid, out_e, in_e)
        raw = {
            "normalized_annotation": (row.get("annotation") or "").strip(),
            "normalized_notes": (row.get("notes") or "").strip(),
            "merged_aliases": split_list(row.get("aliases", "")),
            "merged_external_ids": split_list(row.get("external_ids", "")),
            "source_databases": split_list(row.get("source_database", "")),
        }
        summary = derive_summary(row, raw, ec)
        quality_summary = classify_quality(summary)
        quality_raw = classify_quality(row.get("annotation") or "")
        card = {
            "entity_id": eid,
            "entity_type": row.get("entity_type", ""),
            "display_name": row.get("display_name") or row.get("name") or eid,
            "canonical_name": row.get("name") or eid,
            "family_key": row.get("family_key", ""),
            "aliases": split_list(row.get("aliases", "")),
            "summary": summary,
            "functional_context": trim(raw["normalized_annotation"], 2200),
            "biological_role": trim(raw["normalized_notes"], 1200),
            "subcellular_location": row.get("subcellular_location", ""),
            "default_state": row.get("default_state", ""),
            "allowed_states": split_list(row.get("allowed_states", "")),
            "evidence_sources": sorted(set(raw["source_databases"])),
            "source_databases": sorted(set(raw["source_databases"])),
            "source_id": row.get("source_id", ""),
            "external_ids": split_list(row.get("external_ids", "")),
            "linked_entities": derive_linked_entities(row, ec),
            "edge_context": ec,
            "pathways": split_list(row.get("pathways", "")),
            "raw_annotations": raw,
            "merged_from": split_list(row.get("merged_from", "")),
            "is_exogenous": row.get("is_exogenous", "false"),
            "quality": {
                "raw_annotation_quality": quality_raw,
                "enriched_summary_quality": quality_summary,
                "enrichment_sources": sorted(set(raw["source_databases"])),
                "family_key_present": bool(row.get("family_key")),
                "merged_source_count": len(split_list(row.get("merged_from", ""))) or 1,
            },
        }
        cards.append(card)

    out_dir = edir / "_v2"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = write_jsonl(out_dir / "entities_enriched_v2.jsonl", cards)
    write_jsonl(out_dir / "entities_enriched_v2_lite.jsonl", (lite_card(c) for c in cards))

    summary_path = out_dir / "entities_enriched_v2_summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["entity_id", "entity_type", "display_name", "is_exogenous", "summary_quality", "merged_source_count"],
        )
        w.writeheader()
        for c in cards:
            w.writerow(
                {
                    "entity_id": c["entity_id"],
                    "entity_type": c["entity_type"],
                    "display_name": c["display_name"],
                    "is_exogenous": c["is_exogenous"],
                    "summary_quality": c["quality"]["enriched_summary_quality"],
                    "merged_source_count": c["quality"]["merged_source_count"],
                }
            )

    by_type = Counter(c["entity_type"] for c in cards)
    by_quality = Counter(c["quality"]["enriched_summary_quality"] for c in cards)
    by_exogenous = Counter(c["is_exogenous"] for c in cards)
    report = {
        "input_entities": len(entities),
        "output_cards": n,
        "by_type": dict(by_type),
        "by_quality": dict(by_quality),
        "by_exogenous": dict(by_exogenous),
    }
    (out_dir / "enrichment_report_v2.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if args.apply_in_place:
        for name in ("entities_enriched_v2.jsonl", "entities_enriched_v2_lite.jsonl",
                     "entities_enriched_v2_summary.csv", "enrichment_report_v2.json"):
            target = edir / name
            target.write_text((out_dir / name).read_text(encoding="utf-8"), encoding="utf-8")
        # Also rewrite the legacy `entities_enriched_lite.jsonl` that the
        # diagnostic UI / web backend reads, so a single source of truth
        # exists. The full enriched_lite.jsonl is preserved.
        full_src = out_dir / "entities_enriched_v2.jsonl"
        full_dst = edir / "entities_enriched.jsonl"
        if full_src.exists():
            full_dst.write_text(full_src.read_text(encoding="utf-8"), encoding="utf-8")
        lite_src = out_dir / "entities_enriched_v2_lite.jsonl"
        lite_dst = edir / "entities_enriched_lite.jsonl"
        if lite_src.exists():
            lite_dst.write_text(lite_src.read_text(encoding="utf-8"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())