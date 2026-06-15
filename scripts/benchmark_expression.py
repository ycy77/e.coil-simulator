#!/usr/bin/env python3
"""DE-grounded perturbation benchmark — the path to the headline "LLM beats rules" claim.

Unlike benchmark_perturbation.py (ground truth = RegulonDB topology SIGN, which the
deterministic mock can mostly reproduce), this scores the simulator against
MEASURED differential expression: for a real perturbation experiment, did the
simulator predict each significant gene's direction (up/down) correctly?

The decisive subset is CONFLICT genes — genes with opposing regulators (activator
AND repressor) — where the rules must opt out and only the model can resolve the
net direction. The LLM-vs-mock gap on that subset is the experiment that earns a
paper.

Decoupled from any specific compendium: it consumes a generic DE table. Convert
PRECISE-1K / iModulons / a GEO knockout series to this TSV on the GPU host:

    perturbation_id<TAB>gene<TAB>log2fc<TAB>padj
    delta_fnr<TAB>b1234<TAB>-2.1<TAB>1e-8
    ...

and a perturbation map (YAML) saying how to set each experiment up in the sim:

    delta_fnr: [{entity: fnr, state: inhibited}]      # Δfnr -> Fnr loss of function

    python scripts/benchmark_expression.py --expression de.tsv --map map.yaml --mode both

Outputs runs/_expr_benchmark/<ts>/benchmark.json + a summary (overall + conflict-subset
direction accuracy, mock vs llm).
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.config import load_yaml_like  # noqa: E402
# reuse the shared wiring + direction folding from the RegulonDB benchmark
from benchmark_perturbation import build_deps, build_engine, direction_of, name_index  # type: ignore  # noqa: E402


def parse_args():
    p = argparse.ArgumentParser(description="DE-grounded perturbation benchmark (measured fold-changes).")
    p.add_argument("--config", type=Path, default=Path("configs/simulation_lit.yaml"))
    p.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    p.add_argument("--expression", type=Path, required=True, help="DE table TSV: perturbation_id, gene, log2fc, padj")
    p.add_argument("--map", type=Path, required=True, help="YAML: perturbation_id -> [{entity, state}, ...]")
    p.add_argument("--mode", choices=("mock", "llm", "both"), default="mock")
    p.add_argument("--lfc", type=float, default=1.0, help="|log2fc| threshold for a significant DEG")
    p.add_argument("--padj", type=float, default=0.05)
    p.add_argument("--rounds", type=int, default=6)
    p.add_argument("--max-active-agents", type=int, default=256)
    p.add_argument("--output-root", type=Path, default=Path("runs/_expr_benchmark"))
    return p.parse_args()


# --------------------------------------------------------------------------- #
# Pure, testable helpers
# --------------------------------------------------------------------------- #
def load_de_table(path: Path):
    """perturbation_id -> {gene_key_lower: (log2fc, padj)}."""
    out = defaultdict(dict)
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            pid = (row.get("perturbation_id") or "").strip()
            gene = (row.get("gene") or "").strip().lower()
            if not pid or not gene:
                continue
            try:
                lfc = float(row.get("log2fc", "nan"))
                padj = float(row.get("padj", "nan"))
            except ValueError:
                continue
            out[pid][gene] = (lfc, padj)
    return dict(out)


def conflict_genes(graph) -> set:
    """Gene ids with opposing regulators (activated by one, repressed by another)."""
    inc = defaultdict(lambda: {"activates": set(), "represses": set()})
    for e in graph.edges:
        if e.relation_type in ("activates", "represses") and e.target_id.startswith("gene."):
            inc[e.target_id][e.relation_type].add(e.source_id)
    out = set()
    for gid, d in inc.items():
        if (d["activates"] - d["represses"]) and (d["represses"] - d["activates"]):
            out.add(gid)
    return out


def measured_direction(lfc: float) -> str:
    return "up" if lfc > 0 else "down"


def score_against_de(graph, final_states, de_for_pert, idx, lfc_thr, padj_thr, conflict_set):
    """Compare predicted gene directions to measured significant DEGs.

    Returns (overall[correct,total], conflict[correct,total]) for genes that are
    significant in the DE data, map to a graph gene, and actually moved in the sim.
    """
    overall = [0, 0]
    conflict = [0, 0]
    for gene_key, (lfc, padj) in de_for_pert.items():
        if abs(lfc) < lfc_thr or padj > padj_thr:
            continue
        gids = [i for i in idx.get(gene_key, set()) if i.startswith("gene.")]
        if not gids:
            continue
        gid = gids[0]
        obs = final_states.get(gid)
        pred = direction_of(obs)
        if pred == "none":
            continue  # sim didn't move it -> not a direction call (coverage, not error)
        meas = measured_direction(lfc)
        ok = int(pred == meas)
        overall[0] += ok
        overall[1] += 1
        if gid in conflict_set:
            conflict[0] += ok
            conflict[1] += 1
    return overall, conflict


# --------------------------------------------------------------------------- #
def main() -> int:
    args = parse_args()
    config = load_yaml_like(PROJECT_ROOT / args.config)
    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    deps = build_deps(config, model_config)
    graph = deps["graph"]
    idx = name_index(graph)
    conflict_set = conflict_genes(graph)
    de = load_de_table(PROJECT_ROOT / args.expression)
    pert_map = load_yaml_like(PROJECT_ROOT / args.map)
    print(f"DE perturbations: {len(de)}; conflict genes in graph: {len(conflict_set)}")

    def resolve(entity_ref: str):
        if entity_ref in graph.entities:
            return entity_ref
        cands = idx.get(entity_ref.lower(), set())
        for pref in ("protein.", "gene."):
            for c in sorted(cands):
                if c.startswith(pref):
                    return c
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = PROJECT_ROOT / args.output_root / timestamp
    out_dir.mkdir(parents=True, exist_ok=True)
    modes = ["mock", "llm"] if args.mode == "both" else [args.mode]

    async def run_mode(mode):
        overall = [0, 0]; conflict = [0, 0]; ran = 0; skipped = []
        for pid, spec in pert_map.items():
            if pid not in de:
                skipped.append((pid, "no DE rows")); continue
            perts = []
            for item in (spec or []):
                rid = resolve(str(item.get("entity", "")))
                if rid:
                    perts.append({"entity_id": rid, "state": item.get("state", "inhibited"),
                                  "source": "expr_benchmark", "input_source": "expression", "reason": pid})
            if not perts:
                skipped.append((pid, "no resolvable entity")); continue
            eng = build_engine(deps, mode, out_dir / f"{mode}__{pid}", args)
            state = await eng.run(perturbations=perts, max_rounds=args.rounds,
                                  max_active_agents=args.max_active_agents,
                                  initial_profile=deps["initial_profile"])
            o, c = score_against_de(graph, state.states, de[pid], idx, args.lfc, args.padj, conflict_set)
            for dst, src in ((overall, o), (conflict, c)):
                dst[0] += src[0]; dst[1] += src[1]
            ran += 1
        return {"mode": mode, "perturbations_run": ran, "skipped": skipped,
                "overall_direction_acc": round(overall[0] / overall[1], 3) if overall[1] else None,
                "overall_n": overall[1],
                "conflict_direction_acc": round(conflict[0] / conflict[1], 3) if conflict[1] else None,
                "conflict_n": conflict[1]}

    results = {m: asyncio.run(run_mode(m)) for m in modes}
    (out_dir / "benchmark.json").write_text(json.dumps({"timestamp": timestamp, "results": results}, indent=2),
                                            encoding="utf-8")
    for m, r in results.items():
        print(f"  [{m}] overall={r['overall_direction_acc']} (n={r['overall_n']})  "
              f"CONFLICT={r['conflict_direction_acc']} (n={r['conflict_n']})")
    if "mock" in results and "llm" in results:
        print("  Headline: on the CONFLICT subset, llm should exceed mock.")
    print(f"\nWrote {out_dir / 'benchmark.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
