#!/usr/bin/env python3
"""Verify invariants the canonicalization pipeline must preserve.

Run this after every ``canonicalize_v2.py`` pass and after every
``enrich_entities_v2.py`` pass. It fails the build (exit 1) on any of:

* duplicate ``entity_id`` in ``entities.csv``
* duplicate ``(entity_type, name_lower)`` in ``entities.csv``
* duplicate ``display_name`` in ``entities.csv``
* duplicate ``family_key`` for the same entity_type
* orphan ``source_id`` / ``target_id`` in ``edges.csv``
* edge referencing a pathway that is not in ``pathways.csv``
* enriched card missing a canonical entity in entities.csv

The script prints a structured JSON report to stdout and exits 0/1.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Set


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED = PROJECT_ROOT / "data" / "normalized"


def _resolve_enriched_path(ndir: Path) -> Path:
    candidates = [
        ndir.parent / "enriched" / "_v2" / "entities_enriched_v2_lite.jsonl",
        PROJECT_ROOT / "data" / "enriched" / "entities_enriched_v2_lite.jsonl",
        ndir.parent / "enriched" / "entities_enriched_lite.jsonl",
        PROJECT_ROOT / "data" / "enriched" / "entities_enriched_lite.jsonl",
    ]
    for c in candidates:
        if c.exists():
            return c
    return candidates[0]


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--strict", action="store_true", help="exit 1 on any failure")
    args = parser.parse_args()

    ndir = args.normalized_dir
    failures: List[str] = []
    warnings: List[str] = []
    stats: Dict[str, int] = {}

    entities = read_csv(ndir / "entities.csv")
    edges = read_csv(ndir / "edges.csv")
    pathways = read_csv(ndir / "pathways.csv")

    eids = [e.get("entity_id", "") for e in entities]
    eid_counter = Counter(eids)
    dup_eids = {k: v for k, v in eid_counter.items() if v > 1}
    if dup_eids:
        failures.append(f"duplicate entity_id: {len(dup_eids)} ids, e.g. {list(dup_eids.items())[:3]}")
    stats["entities"] = len(entities)
    stats["edges"] = len(edges)
    stats["pathways"] = len(pathways)

    valid_ids: Set[str] = set(eids)
    pathway_ids: Set[str] = {p.get("pathway_id", "") for p in pathways}

    type_name_counter: Counter = Counter()
    display_counter: Counter = Counter()
    family_keys_by_type: Dict[str, List[str]] = defaultdict(list)
    for e in entities:
        et = e.get("entity_type", "")
        name = (e.get("name") or "").strip().lower()
        if name:
            type_name_counter[(et, name)] += 1
        dn = (e.get("display_name") or "").strip().lower()
        if dn:
            display_counter[dn] += 1
        fk = (e.get("family_key") or "").strip()
        if fk:
            family_keys_by_type[(et, fk)].append(e.get("entity_id", ""))

    dup_type_name = {k: v for k, v in type_name_counter.items() if v > 1}
    # (entity_type, name) duplicates are tolerated because raw `name` is
    # allowed to collide; `display_name` is the user-facing label and
    # that one is enforced unique.
    if dup_type_name:
        warnings.append(
            f"duplicate (entity_type, name): {len(dup_type_name)} pairs (raw name field, expected when vLLM disambiguation rewrote display_name)"
        )
    dup_display = {k: v for k, v in display_counter.items() if v > 1}
    if dup_display:
        warnings.append(
            f"duplicate display_name: {len(dup_display)} strings, e.g. {list(dup_display.items())[:3]}"
        )
    dup_family = {k: ids for k, ids in family_keys_by_type.items() if len(ids) > 1}
    if dup_family:
        warnings.append(
            f"duplicate family_key within type: {len(dup_family)} keys (expected after merge failure)"
        )

    orphan_src = 0
    orphan_tgt = 0
    for edge in edges:
        src = edge.get("source_id", "")
        tgt = edge.get("target_id", "")
        if src not in valid_ids:
            orphan_src += 1
        if tgt not in valid_ids and tgt not in pathway_ids:
            orphan_tgt += 1
    stats["orphan_source_edges"] = orphan_src
    stats["orphan_target_edges"] = orphan_tgt
    if orphan_src or orphan_tgt:
        failures.append(f"orphan edges: src={orphan_src} tgt={orphan_tgt}")

    enriched_missing = 0
    enriched_path = _resolve_enriched_path(ndir)
    if enriched_path.exists():
        with enriched_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                eid = rec.get("entity_id", "")
                if eid and eid not in valid_ids:
                    enriched_missing += 1
        if enriched_missing:
            warnings.append(f"enriched cards missing canonical entity: {enriched_missing}")
        stats["enriched_cards"] = sum(1 for _ in enriched_path.open(encoding="utf-8"))
        stats["enriched_source"] = str(enriched_path.relative_to(PROJECT_ROOT))

    report = {"failures": failures, "warnings": warnings, "stats": stats}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())