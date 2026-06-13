#!/usr/bin/env python3
"""Merge STRING PPI channels into the simulation baseline.

The user has pre-filtered STRING into three channels, all
already mapped to our ``protein.PXXXXX`` entity_ids and with
pre-computed ``edge_weight``:

  * experimental  (escore >= 700): 9721 edges
  * database      (dscore >= 700): 13583 edges
  * coexpression  (cscore >= 800): 9465 edges

We merge them into the simulation edge set, de-duping against
existing edges (same source/target). STRING edges become
relation_type ``interacts`` with channel-specific ``edge_weight``
and a ``string_channel`` column. The combined score is also
preserved on the edge record for downstream scoring.

This script is idempotent: re-running it never duplicates.

Output: ``data/normalized/simulation/edges.csv`` (extended
schema with the new columns).
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SIM_DIR = PROJECT_ROOT / "data" / "normalized" / "simulation"
SRC_DIR = PROJECT_ROOT / "data" / "normalized"

CHANNELS = [
    # (filename, channel_name)
    ("string_experimental_edges_escore700.csv",  "experimental"),
    ("string_database_edges_dscore700.csv",      "database"),
    ("string_coexpression_edges_cscore800.csv",  "coexpression"),
]

# Base weights (per the design doc).
#   experimental: escore/1000 * 0.85
#   database:     dscore/1000 * 0.75
#   coexpression: 0.35  (only cscore >= 800 in this file)
# We re-derive edge_weight from the raw channel_score in the
# file (the user already pre-computed it but we recompute for
# consistency in case the source files change).
BASE_WEIGHT = {
    "experimental": 0.85,
    "database":     0.75,
    "coexpression": 0.35,
}


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--src-dir", type=Path, default=SRC_DIR)
    p.add_argument("--sim-dir", type=Path, default=SIM_DIR)
    args = p.parse_args()

    print(f"[1/4] reading baseline edges from {args.sim_dir / 'edges.csv'} ...")
    base_edges = read_csv(args.sim_dir / "edges.csv")
    base_fields = list(base_edges[0].keys()) if base_edges else []
    print(f"      {len(base_edges)} baseline edges, fields={base_fields}")

    print(f"[2/4] reading STRING channels from {args.src_dir} ...")
    string_rows: List[Dict[str, str]] = []
    for fname, channel in CHANNELS:
        rows = read_csv(args.src_dir / fname)
        for r in rows:
            # Some files have a multi-id column delimited by
            # | (e.g. the experimental edges have the gene
            # b-number as an alt id). Take the FIRST entity id
            # only -- multiple ids would mean ambiguous
            # protein identity which we cannot safely add.
            src_eid = (r.get("source_entity_ids") or "").split("|")[0].strip()
            tgt_eid = (r.get("target_entity_ids") or "").split("|")[0].strip()
            if not src_eid or not tgt_eid or src_eid == tgt_eid:
                continue
            score = int(r.get("channel_score") or 0)
            weight = round(score / 1000.0 * BASE_WEIGHT[channel], 4)
            string_rows.append({
                "source_id": src_eid,
                "target_id": tgt_eid,
                "relation_type": "interacts",
                "direction": "undirected",
                "evidence": f"STRING {channel} channel_score={score}",
                "source_database": f"STRING:{channel}",
                "source_record_id": f"{r.get('source_string_id','')}|{r.get('target_string_id','')}",
                "notes": f"channel={channel} combined_score={r.get('combined_score','')}",
                "reaction_id": "", "reactants": "", "products": "",
                "ec_number": "", "pathway": "",
                # New columns
                "edge_weight": f"{weight}",
                "string_channel": channel,
            })
    print(f"      {len(string_rows)} STRING rows from {len(CHANNELS)} channels")

    print(f"[3/4] extending baseline schema + merging ...")
    # Add the new columns to the baseline schema if not present
    new_cols = ["edge_weight", "string_channel"]
    ext_fields = list(base_fields)
    for c in new_cols:
        if c not in ext_fields:
            ext_fields.append(c)
    # Backfill edge_weight for any existing baseline edges
    # that lack one. The design doc gives a relation-specific
    # weight table; we honour it here.
    RELATION_WEIGHT = {
        "activates":        0.90,
        "represses":        0.90,
        "inhibits":         0.80,
        "binds":            0.80,
        "encodes":          0.75,
        "transcribed_as":   0.70,
        "transports":       0.65,
        "bound_by":         0.60,
        "produces":         0.55,
        "consumes":         0.55,
        "is_subunit_of":    0.55,
        "interacts":        0.50,
        "regulates":        0.50,
        "is_component_of":  0.50,
        "spontaneous_produces": 0.40,
        "spontaneous_consumes": 0.40,
        "paralog_of":       0.30,
        "participates_in":  0.20,
    }
    for e in base_edges:
        if not e.get("edge_weight"):
            e["edge_weight"] = f"{RELATION_WEIGHT.get(e.get('relation_type',''), 0.40):.2f}"
        if not e.get("string_channel"):
            e["string_channel"] = ""

    # Dedupe STRING rows against existing baseline (same
    # source/target). If a STRING interact edge already exists
    # (e.g. as a regulates/binds edge), keep the more specific
    # one.
    existing_pairs = {(e["source_id"], e["target_id"]) for e in base_edges}
    new_unique: List[Dict[str, str]] = []
    for r in string_rows:
        pair = (r["source_id"], r["target_id"])
        if pair in existing_pairs:
            continue
        new_unique.append(r)
        existing_pairs.add(pair)
    print(f"      {len(new_unique)} unique STRING edges to add")

    print(f"[4/4] writing {len(base_edges) + len(new_unique)} edges ...")
    all_edges = base_edges + new_unique
    with (args.sim_dir / "edges.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ext_fields)
        w.writeheader()
        for e in all_edges:
            w.writerow({k: e.get(k, "") for k in ext_fields})

    # Summary
    by_channel = defaultdict(int)
    for e in new_unique:
        by_channel[e["string_channel"]] += 1
    print()
    print("=" * 50)
    print(f"  baseline edges (before): {len(base_edges)}")
    print(f"  STRING edges added:      {sum(by_channel.values())}")
    for ch, c in sorted(by_channel.items()):
        print(f"    {ch:15s} {c}")
    print(f"  total edges (after):     {len(base_edges) + len(new_unique)}")
    print("=" * 50)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
