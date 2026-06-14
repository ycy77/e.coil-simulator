#!/usr/bin/env python3
"""Validate the knowledge graph's regulatory layer against the RegulonDB gold standard.

The simulator's accuracy is bounded by the graph. This script measures that bound
with reviewer-grade numbers instead of opinion: how much of the RegulonDB
TF/regulator -> gene network the graph actually contains (recall), whether the
graph's activates/represses signs agree with RegulonDB (sign accuracy), and what
classes of regulation the gene->gene graph structurally cannot represent (sigma
factors, sRNAs, small-molecule effectors like ppGpp).

Gold standard: data/regulationDB/NetworkRegulatorGene.tsv (regulator, target gene,
sign +/-/?). Public, curated, the standard reference for E. coli regulation.

    python scripts/validate_kg.py                 # validate the simulation baseline
    python scripts/validate_kg.py --graph data/normalized   # validate the full graph

Writes docs/KG_VALIDATION_<date>.md and prints a summary.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.graph import StaticGraph  # noqa: E402

GOLD = PROJECT_ROOT / "data" / "regulationDB" / "NetworkRegulatorGene.tsv"


def parse_args():
    p = argparse.ArgumentParser(description="Validate KG regulatory layer vs RegulonDB.")
    p.add_argument("--graph", type=Path, default=Path("data/normalized/simulation"))
    p.add_argument("--gold", type=Path, default=GOLD)
    p.add_argument("--date", default="", help="date stamp for the output filename")
    return p.parse_args()


def load_gold(path: Path):
    """Yield (regulator_name, target_gene_name, sign) from the RegulonDB network."""
    rows = []
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if line.startswith("#") or not line.strip():
                continue
            cols = [c.strip() for c in line.rstrip("\n").split("\t")]
            if len(cols) < 6:
                continue
            regulator, target, sign = cols[1], cols[4], cols[5]
            if regulator and target:
                rows.append((regulator, target, sign))
    return rows


def build_name_index(graph: StaticGraph):
    """name/alias (lowercased) -> set of entity_ids.

    A regulator name like "FNR" maps to BOTH the gene and the TF protein; the
    graph routes regulation through the protein (protein->gene edges), so we must
    keep all candidates and treat a match on any of them as coverage.
    """
    index = defaultdict(set)
    for entity in graph.entities.values():
        for key in [entity.name] + list(entity.aliases):
            k = key.strip().lower()
            if k:
                index[k].add(entity.entity_id)
    return index


def main() -> int:
    args = parse_args()
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / args.graph)
    gold = load_gold(PROJECT_ROOT / args.gold)
    name_index = build_name_index(graph)

    # Index the graph's regulatory edges by (source_id, target_id) -> sign.
    graph_reg = {}
    for edge in graph.edges:
        if edge.relation_type in ("activates", "represses"):
            graph_reg[(edge.source_id, edge.target_id)] = edge.relation_type

    gold_unique = set()  # dedup identical (reg, target, sign)
    for r, t, s in gold:
        gold_unique.add((r.lower(), t.lower(), s))

    total = len(gold_unique)
    reg_mappable = tgt_mappable = both_mappable = 0
    present = 0
    sign_checked = sign_agree = 0
    unmapped_regulators = Counter()
    sign_dist = Counter()

    for reg_name, tgt_name, sign in gold_unique:
        sign_dist[sign or "?"] += 1
        reg_ids = name_index.get(reg_name, set())
        tgt_ids = name_index.get(tgt_name, set())
        reg_mappable += bool(reg_ids)
        tgt_mappable += bool(tgt_ids)
        if not reg_ids:
            unmapped_regulators[reg_name] += 1
        if reg_ids and tgt_ids:
            both_mappable += 1
            # A match on ANY (regulator-candidate -> target-candidate) pair counts:
            # the regulator name may resolve to a gene and a protein; the edge is
            # usually protein->gene.
            rel = None
            for rid in reg_ids:
                for tid in tgt_ids:
                    rel = graph_reg.get((rid, tid))
                    if rel:
                        break
                if rel:
                    break
            if rel:
                present += 1
                if sign in ("+", "-"):
                    sign_checked += 1
                    gold_rel = "activates" if sign == "+" else "represses"
                    sign_agree += int(rel == gold_rel)

    def pct(a, b):
        return f"{100*a/b:.1f}%" if b else "—"

    lines = [
        f"# Knowledge-graph validation vs RegulonDB ({args.graph})",
        "",
        f"Gold standard: `{args.gold}` — {total} unique (regulator, target, sign) interactions.",
        "",
        "## Coverage (recall)",
        "",
        f"- Regulators mappable to a graph entity: **{pct(reg_mappable, total)}** ({reg_mappable}/{total})",
        f"- Target genes mappable: **{pct(tgt_mappable, total)}** ({tgt_mappable}/{total})",
        f"- Both endpoints mappable: **{pct(both_mappable, total)}** ({both_mappable}/{total})",
        f"- **Interactions present as a graph edge: {pct(present, total)} of all gold ({present}/{total}); "
        f"{pct(present, both_mappable)} of the mappable subset ({present}/{both_mappable})**",
        "",
        "## Sign accuracy (precision of direction)",
        "",
        f"- Graph edges with a checkable RegulonDB sign: {sign_checked}",
        f"- **Sign agreement (activates↔+, represses↔−): {pct(sign_agree, sign_checked)} ({sign_agree}/{sign_checked})**",
        "",
        "## What the gene→gene graph structurally cannot represent",
        "",
        f"- RegulonDB sign distribution: {dict(sign_dist)}",
        f"- Unmappable regulators (sigma factors, sRNAs, small-molecule effectors like ppGpp, complexes): "
        f"{len(unmapped_regulators)} distinct, covering {sum(unmapped_regulators.values())} interactions.",
        f"  Top unmapped: {', '.join(f'{n}({c})' for n, c in unmapped_regulators.most_common(15))}",
        "",
        "## Interpretation",
        "",
        "- Recall is the ceiling on what perturbation effects the simulator can ever reproduce: "
        "any RegulonDB interaction absent from the graph is a response the simulator physically cannot make.",
        "- Unmappable regulators expose the operator/sigma/sRNA structure gap: RegulonDB regulation routed "
        "through sigma factors, sRNAs and small-molecule effectors is collapsed or dropped, which is why "
        "true L3 (AND/OR operator logic) cannot yet be represented.",
        "- Sign accuracy < 100% flags edges whose direction disagrees with the curated standard — "
        "data-quality items to fix before publication.",
    ]
    report = "\n".join(lines) + "\n"

    out_name = f"KG_VALIDATION_{args.date}.md" if args.date else "KG_VALIDATION.md"
    out_path = PROJECT_ROOT / "docs" / out_name
    out_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
