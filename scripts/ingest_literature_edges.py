#!/usr/bin/env python3
"""Ingest literature-curated regulatory edges — verified, evidence-gated, separately accounted.

Reads data/literature/regulatory_edges.jsonl (hand-curated from
docs/LITERATURE_EVIDENCE_2023_2026.md) and produces a SEPARATE overlay of edges
plus an honest ledger. Designed around five integrity rules:

  (1) Never pollute the RegulonDB validation layer. Eligible edges are written to
      a separate overlay file tagged source_database=Literature; the RegulonDB
      gold and the DB-derived edges.csv are untouched, so KG recall stays frozen.
      The ledger reports how many literature edges OVERLAP RegulonDB (the recall
      inflation we are avoiding) vs are NOVEL.
  (2) No double-cheating: this only adds/【flags】edges; it does not write the
      phenotype expectations. Edge provenance (DOI) is recorded.
  (3) Evidence gating is enforced in code: only evidence_tier=='direct' AND
      peer_reviewed AND strain=='K-12' is eligible as a hard edge. Preprints,
      reviews, omics, and non-K-12 are GATED OUT (kept in the ledger, not added).
  (4) b-number / UniProt are verified against the KG canonical id set. No guesses:
      unresolvable endpoints are reported, not invented.
  (5) Canonical ids only; direction conflicts with existing edges are flagged for
      a human, never auto-overwritten; orphans are reported.

    python scripts/ingest_literature_edges.py            # ledger only (dry run)
    python scripts/ingest_literature_edges.py --write     # also write the overlay

Outputs: docs/LITERATURE_INGEST_LEDGER.md (+ data/literature/literature_edges.overlay.csv with --write).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.graph import StaticGraph  # noqa: E402

LIT = PROJECT_ROOT / "data" / "literature" / "regulatory_edges.jsonl"
OVERLAY = PROJECT_ROOT / "data" / "literature" / "literature_edges.overlay.csv"
LEDGER = PROJECT_ROOT / "docs" / "LITERATURE_INGEST_LEDGER.md"
GOLD = PROJECT_ROOT / "data" / "regulationDB" / "NetworkRegulatorGene.tsv"
EDGE_COLUMNS = ["source_id", "relation_type", "target_id", "direction", "evidence",
                "source_database", "source_record_id", "notes", "edge_weight", "string_channel"]


def parse_args():
    p = argparse.ArgumentParser(description="Ingest literature regulatory edges (verified, gated, separate).")
    p.add_argument("--graph", type=Path, default=Path("data/normalized/simulation"))
    p.add_argument("--lit", type=Path, default=LIT)
    p.add_argument("--write", action="store_true", help="write the overlay CSV (default: ledger only)")
    return p.parse_args()


def load_lit(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def build_indexes(graph: StaticGraph):
    name_idx = defaultdict(set)
    for e in graph.entities.values():
        for k in [e.name] + list(e.aliases):
            if k.strip():
                name_idx[k.strip().lower()].add(e.entity_id)
    reg = {}
    for e in graph.edges:
        if e.relation_type in ("activates", "represses"):
            reg[(e.source_id, e.target_id)] = e.relation_type
    return name_idx, reg


def resolve_regulator(row, graph, name_idx):
    """Regulator -> its PROTEIN canonical id (graph routes regulation protein->gene).
    Verified against the KG; no guessing."""
    up = (row.get("regulator_uniprot") or "").strip()
    if up and f"protein.{up}" in graph.entities:
        return f"protein.{up}", f"uniprot:{up}"
    for cand in sorted(name_idx.get((row.get("regulator") or "").lower(), set())):
        if cand.startswith("protein."):
            return cand, "name:protein"
    return None, "unresolved"


def resolve_target(row, graph, name_idx):
    """Target -> its GENE canonical id, verified against the KG; no guessing."""
    bnum = (row.get("target_bnum") or "").strip()
    if bnum and f"gene.{bnum}" in graph.entities:
        return f"gene.{bnum}", f"bnum:{bnum}"
    for cand in sorted(name_idx.get((row.get("target") or "").lower(), set())):
        if cand.startswith("gene."):
            return cand, "name:gene"
    return None, "unresolved"


def is_eligible_hard_edge(row):
    return (row.get("evidence_tier") == "direct"
            and bool(row.get("peer_reviewed"))
            and row.get("strain") == "K-12")


def load_gold_pairs():
    """Frozen RegulonDB (regulator_name, target_name) lowercased set — read-only."""
    pairs = set()
    if not GOLD.exists():
        return pairs
    for line in GOLD.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        c = [x.strip() for x in line.split("\t")]
        if len(c) >= 6 and c[1] and c[4]:
            pairs.add((c[1].lower(), c[4].lower()))
    return pairs


def main() -> int:
    args = parse_args()
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / args.graph)
    name_idx, existing_reg = build_indexes(graph)
    gold_pairs = load_gold_pairs()
    rows = load_lit(PROJECT_ROOT / args.lit)

    ledger = []          # (category, row, detail)
    overlay_edges = []   # rows eligible to ADD
    cat = Counter()

    for row in rows:
        src, src_how = resolve_regulator(row, graph, name_idx)
        tgt, tgt_how = resolve_target(row, graph, name_idx)

        # (4) id verification — no guessing
        if src is None or tgt is None:
            cat["UNRESOLVED"] += 1
            ledger.append(("UNRESOLVED", row, f"regulator={src_how} target={tgt_how}"))
            continue

        rel = row["relation"]
        existing = existing_reg.get((src, tgt))
        in_gold = ((row.get("regulator", "").lower(), row.get("target", "").lower()) in gold_pairs)

        # (5) conflict with an existing edge -> flag, never overwrite
        if existing is not None:
            if existing == rel:
                cat["ALREADY_IN_GRAPH_CONFIRM"] += 1
                ledger.append(("ALREADY_IN_GRAPH_CONFIRM", row, f"{src}->{tgt} {rel}; gold={in_gold}"))
            else:
                cat["CONFLICT"] += 1
                ledger.append(("CONFLICT", row, f"{src}->{tgt}: graph={existing} vs lit={rel}; gold={in_gold} (NOT changed)"))
            continue

        # (3) evidence gating — enforced
        if not is_eligible_hard_edge(row):
            cat["GATED_OUT"] += 1
            why = []
            if row.get("evidence_tier") != "direct": why.append(f"tier={row.get('evidence_tier')}")
            if not row.get("peer_reviewed"): why.append("preprint")
            if row.get("strain") != "K-12": why.append(f"strain={row.get('strain')}")
            ledger.append(("GATED_OUT", row, f"{src}->{tgt} {rel}; " + ",".join(why) + f"; gold={in_gold}"))
            continue

        # eligible NEW hard edge
        cat["ADD"] += 1
        ledger.append(("ADD", row, f"{src}->{tgt} {rel}; novel_vs_regulondb={not in_gold}"))
        overlay_edges.append({
            "source_id": src, "relation_type": rel, "target_id": tgt, "direction": "directed",
            "evidence": "literature_direct", "source_database": "Literature",
            "source_record_id": row.get("doi", ""), "notes": f"{row.get('paper','')}: {row.get('notes','')[:160]}",
            "edge_weight": "", "string_channel": "",
        })

    # (1) separate accounting: how many literature edges overlap frozen RegulonDB
    add_in_gold = sum(1 for c, r, _ in ledger if c == "ADD"
                      and (r.get("regulator", "").lower(), r.get("target", "").lower()) in gold_pairs)

    # ---- ledger report ----
    lines = [
        "# Literature edge ingest ledger",
        "",
        f"Source: `{args.lit}` ({len(rows)} curated edges)  ·  graph: `{args.graph}`",
        f"RegulonDB gold: `{GOLD.name}` (FROZEN, read-only — used only to flag overlap).",
        "",
        "## Summary",
        "",
        "| Category | n | meaning |",
        "| --- | --- | --- |",
        f"| ADD | {cat['ADD']} | eligible new hard edges -> overlay (separate file, NOT in edges.csv) |",
        f"| ALREADY_IN_GRAPH_CONFIRM | {cat['ALREADY_IN_GRAPH_CONFIRM']} | literature agrees with an edge already present |",
        f"| CONFLICT | {cat['CONFLICT']} | literature direction != graph; flagged for human, NOT changed |",
        f"| GATED_OUT | {cat['GATED_OUT']} | preprint / review / omics / non-K12 -> not a hard edge |",
        f"| UNRESOLVED | {cat['UNRESOLVED']} | endpoint id not in KG canonical set -> not guessed |",
        "",
        f"**Circularity guard:** of {cat['ADD']} ADDed edges, **{add_in_gold} already exist in RegulonDB** and "
        f"{cat['ADD']-add_in_gold} are NOVEL. Because the overlay is a separate file, KG-recall validation "
        "(validate_kg.py on edges.csv) never sees these, so recall is not inflated.",
        "",
        "## Per-edge ledger",
        "",
        "| Category | Edge | Paper | Tier | Detail |",
        "| --- | --- | --- | --- | --- |",
    ]
    order = {"ADD": 0, "CONFLICT": 1, "ALREADY_IN_GRAPH_CONFIRM": 2, "GATED_OUT": 3, "UNRESOLVED": 4}
    for c, r, detail in sorted(ledger, key=lambda x: order.get(x[0], 9)):
        edge = f"{r.get('regulator')}->{r.get('target')} ({r.get('relation')})"
        tier = f"{r.get('evidence_tier')}{'' if r.get('peer_reviewed') else '/preprint'}/{r.get('strain')}"
        lines.append(f"| {c} | {edge} | {r.get('paper','')} | {tier} | {detail} |")
    LEDGER.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if args.write and overlay_edges:
        OVERLAY.parent.mkdir(parents=True, exist_ok=True)
        with OVERLAY.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=EDGE_COLUMNS)
            w.writeheader()
            w.writerows(overlay_edges)

    print("\n".join(lines[:18]))
    print(f"\nLedger: {LEDGER}")
    if args.write:
        print(f"Overlay written: {OVERLAY} ({len(overlay_edges)} edges)" if overlay_edges else "No eligible edges to write.")
    else:
        print(f"(dry run — pass --write to emit {OVERLAY.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
