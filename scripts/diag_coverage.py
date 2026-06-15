#!/usr/bin/env python3
"""Coverage vs accuracy diagnostic for the DE benchmark.

Question: is the ~chance direction accuracy on measured DE a COVERAGE problem
(the sim never wakes/moves most measured DEGs) or an ACCURACY problem (it moves
them but gets the direction wrong)? Run one KO at increasing propagation depth
(rounds x max_active_agents) and watch whether coverage — and accuracy on the
covered genes — rises.

    python scripts/diag_coverage.py --pid delcrp_glc --entity crp \
        --expression data/raw/precise1k/precise1k_de.tsv
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.config import load_yaml_like  # noqa: E402
from benchmark_perturbation import build_deps, build_engine, direction_of, name_index  # noqa: E402
from benchmark_expression import load_de_table, conflict_genes, measured_direction  # noqa: E402


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--config", type=Path, default=Path("configs/simulation_lit.yaml"))
    p.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    p.add_argument("--expression", type=Path, required=True)
    p.add_argument("--pid", default="delcrp_glc")
    p.add_argument("--entity", default="crp")
    p.add_argument("--lfc", type=float, default=1.0)
    p.add_argument("--padj", type=float, default=0.05)
    p.add_argument("--mode", default="mock")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml_like(PROJECT_ROOT / args.config)
    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    deps = build_deps(config, model_config)
    graph = deps["graph"]
    idx = name_index(graph)
    conflict_set = conflict_genes(graph)
    de = load_de_table(PROJECT_ROOT / args.expression)
    if args.pid not in de:
        print(f"no DE rows for {args.pid}")
        return 1
    de_pert = de[args.pid]

    # resolve perturbation entity (prefer protein, then gene)
    rid = args.entity if args.entity in graph.entities else None
    if rid is None:
        cands = idx.get(args.entity.lower(), set())
        for pref in ("protein.", "gene."):
            for c in sorted(cands):
                if c.startswith(pref):
                    rid = c
                    break
            if rid:
                break
    if rid is None:
        print(f"could not resolve {args.entity}")
        return 1
    perts = [{"entity_id": rid, "state": "inhibited", "source": "diag",
              "input_source": "diag", "reason": args.pid}]

    # measured-significant DEGs that map to a graph gene
    sig_genes = []
    for gk, (lfc, padj) in de_pert.items():
        if abs(lfc) < args.lfc or padj > args.padj:
            continue
        gids = [i for i in idx.get(gk, set()) if i.startswith("gene.")]
        if gids:
            sig_genes.append((gids[0], lfc))
    sig_mappable = len(sig_genes)
    sig_conf = sum(1 for gid, _ in sig_genes if gid in conflict_set)
    print(f"{args.pid}: entity={rid}  measured-sig mappable genes={sig_mappable} (conflict {sig_conf})\n")
    print(f"{'rounds':>6} {'agents':>7} | {'moved':>6} {'cov%':>6} {'acc':>6} | {'conf_moved':>10} {'conf_cov%':>9} {'conf_acc':>8}")

    for rounds, agents in [(6, 256), (12, 1024), (20, 4096)]:
        eng = build_engine(deps, args.mode, PROJECT_ROOT / "runs" / "_diag" / f"{args.pid}_{rounds}_{agents}", None)
        state = asyncio.run(eng.run(perturbations=perts, max_rounds=rounds,
                                    max_active_agents=agents, initial_profile=deps["initial_profile"]))
        moved = corr = cmoved = ccorr = 0
        for gid, lfc in sig_genes:
            pred = direction_of(state.states.get(gid))
            if pred == "none":
                continue
            ok = int(pred == measured_direction(lfc))
            moved += 1; corr += ok
            if gid in conflict_set:
                cmoved += 1; ccorr += ok
        cov = round(100 * moved / sig_mappable, 1) if sig_mappable else 0
        acc = round(corr / moved, 3) if moved else None
        ccov = round(100 * cmoved / sig_conf, 1) if sig_conf else 0
        cacc = round(ccorr / cmoved, 3) if cmoved else None
        print(f"{rounds:>6} {agents:>7} | {moved:>6} {cov:>6} {str(acc):>6} | {cmoved:>10} {ccov:>9} {str(cacc):>8}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
