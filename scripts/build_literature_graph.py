#!/usr/bin/env python3
"""Build a literature-augmented simulation graph, kept SEPARATE from the frozen one.

Produces `data/normalized/simulation_lit/` = the curated baseline
(`data/normalized/simulation/`) + the verified/gated literature overlay
(`data/literature/literature_edges.overlay.csv`), and rebuilds its rule registry.

The frozen `data/normalized/simulation/` is never modified, so RegulonDB-recall
validation (validate_kg.py) keeps using the literature-free graph. Only
literature-grounded phenotype runs use this augmented graph
(configs/simulation_lit.yaml). This is the structural form of integrity rule (1):
literature edges and the validation gold are accounted separately.

Orphan overlay edges (endpoint not in the baseline entity set) are reported and
skipped, never silently kept (rule 5).

    python scripts/build_literature_graph.py
"""
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "data" / "normalized" / "simulation"
OVERLAY = PROJECT_ROOT / "data" / "literature" / "literature_edges.overlay.csv"
OUT = PROJECT_ROOT / "data" / "normalized" / "simulation_lit"
REGISTRY_OUT = PROJECT_ROOT / "data" / "registry" / "simulation_lit" / "native_rules.jsonl"


def main() -> int:
    if not (SRC / "entities.csv").exists():
        print(f"missing source graph: {SRC}"); return 1
    OUT.mkdir(parents=True, exist_ok=True)

    # entities + pathways copied verbatim (literature adds edges, not nodes)
    entity_ids = set()
    with (SRC / "entities.csv").open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            entity_ids.add(row["entity_id"])
    shutil.copy2(SRC / "entities.csv", OUT / "entities.csv")
    if (SRC / "pathways.csv").exists():
        shutil.copy2(SRC / "pathways.csv", OUT / "pathways.csv")

    # read baseline edges + existing (src,rel,tgt) set for dedup
    with (SRC / "edges.csv").open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames
        base_edges = list(reader)
    existing = {(e["source_id"], e["relation_type"], e["target_id"]) for e in base_edges}

    # overlay edges: verify endpoints (rule 5 — orphans reported, not kept)
    added, orphans, dups = [], [], []
    if OVERLAY.exists():
        with OVERLAY.open(newline="", encoding="utf-8") as fh:
            for e in csv.DictReader(fh):
                s, r, t = e["source_id"], e["relation_type"], e["target_id"]
                if s not in entity_ids or t not in entity_ids:
                    orphans.append((s, r, t)); continue
                if (s, r, t) in existing:
                    dups.append((s, r, t)); continue
                added.append({c: e.get(c, "") for c in cols})

    with (OUT / "edges.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(base_edges)
        w.writerows(added)

    print(f"baseline edges: {len(base_edges)}; literature added: {len(added)}; "
          f"dups skipped: {len(dups)}; orphans skipped: {len(orphans)}")
    for s, r, t in orphans:
        print(f"  ORPHAN (endpoint not in baseline): {s} -{r}-> {t}")
    print(f"wrote {OUT/'edges.csv'} ({len(base_edges)+len(added)} edges)")

    # rebuild the rule registry for the augmented graph
    REGISTRY_OUT.parent.mkdir(parents=True, exist_ok=True)
    rc = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "build_rule_registry.py"),
         "--edges", str(OUT / "edges.csv"), "--output", str(REGISTRY_OUT)],
        capture_output=True, text=True,
    )
    print(rc.stdout.strip() or rc.stderr.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
