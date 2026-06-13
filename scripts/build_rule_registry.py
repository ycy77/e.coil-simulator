#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict


DEFAULT_RULE_TYPES = {
    "represses": "transcription_regulation",
    "activates": "transcription_regulation",
    "inhibits": "inhibition",
    "binds": "binding",
    "transports": "transport",
    "forms_complex": "complex_assembly",
    "is_component_of": "complex_assembly",
    "is_critical_for": "complex_assembly",
    "catalyzes": "catalysis",
    "is_substrate_of": "catalysis",
    "is_product_of": "catalysis",
    "encodes": "translation_effect",
    "participates_in": "environment_shift",
}


def confidence_from_evidence(evidence: str, source_database: str) -> str:
    evidence = (evidence or "").upper()
    if evidence in {"C", "CONFIRMED", "STRONG"}:
        return "high"
    if evidence in {"S", "DATABASE", "CURATED"}:
        return "medium"
    if source_database in {"UniProt", "KEGG", "RegulonDB"}:
        return "medium"
    return "low"


def edge_to_rule(row: Dict[str, str]) -> Dict[str, Any]:
    relation = row["relation_type"]
    rule_type = DEFAULT_RULE_TYPES.get(relation, "environment_shift")
    source = row["source_id"]
    target = row["target_id"]
    record = row.get("source_record_id") or f"{source}->{target}"
    rule_id = f"native.{relation}.{source}.{target}.{record}".replace(" ", "_")
    rule_id = rule_id.replace("/", "_").replace(":", "_")
    return {
        "rule_id": rule_id,
        "priority_class": "native",
        "rule_type": rule_type,
        "source": {
            "database": row.get("source_database", ""),
            "accession": record,
            "evidence": row.get("evidence", ""),
        },
        "species_scope": "Escherichia coli K-12 MG1655",
        "participants": {
            "source_id": source,
            "target_id": target,
            "relation_type": relation,
        },
        "conditions": {
            "requires_graph_edge": True,
            "edge_direction": row.get("direction", "directed"),
        },
        "effects": [
            {
                "relation_type": relation,
                "source_id": source,
                "target_id": target,
                "effect_hint": relation,
            }
        ],
        "constraints": {
            "no_new_edges": True,
            "must_reference_existing_entities": True,
        },
        "confidence": confidence_from_evidence(row.get("evidence", ""), row.get("source_database", "")),
        "notes": row.get("notes", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build native rule registry from normalized edges.")
    parser.add_argument("--edges", type=Path, default=Path("data/normalized/edges.csv"))
    parser.add_argument("--output", type=Path, default=Path("data/registry/native_rules.jsonl"))
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with args.edges.open(newline="", encoding="utf-8") as handle, args.output.open("w", encoding="utf-8") as out:
        for row in csv.DictReader(handle):
            if not row.get("source_id") or not row.get("target_id") or not row.get("relation_type"):
                continue
            out.write(json.dumps(edge_to_rule(row), ensure_ascii=False) + "\n")
            count += 1
    print(f"wrote {args.output} rows={count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
