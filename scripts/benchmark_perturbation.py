#!/usr/bin/env python3
"""Perturbation-response benchmark against RegulonDB ground truth.

The phenotype battery (scripts/score_phenotypes.py) is small and self-authored —
fine for development, not for a paper. This benchmark is derived from a curated
external standard instead: for each transcription regulator in RegulonDB, knock
it out in the simulator and check whether each target gene moves in the
RegulonDB-predicted direction.

Ground truth (unambiguous only for single-regulator targets):
  - knock out an ACTIVATOR  -> its target should go DOWN (repressed / lower)
  - knock out a  REPRESSOR  -> its target should go UP   (expressed / higher)

We score only targets with exactly ONE mapped regulator, where the net direction
is well-defined without expression data. Targets with multiple regulators are
reported separately as the conflict set that needs an expression compendium
(PRECISE/iModulons) to score honestly — see docs/REMOTE_WORK_PLAN.md Phase 6.

    python scripts/benchmark_perturbation.py --mode mock --max-tfs 30
    python scripts/benchmark_perturbation.py --mode both --max-tfs 50   # needs vLLM

Metrics: direction accuracy (correct / scorable), plus an "unreachable" count
(target never changed -> edge missing or signal did not propagate), which folds
the KG coverage gap into the benchmark honestly.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.actions import ActionInterpreter  # noqa: E402
from ecoil_sim.agents import PromptBuilder  # noqa: E402
from ecoil_sim.config import load_yaml_like  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.llm import AsyncVLLMClient, NameResolver, RuleBasedMockLLM, load_guided_json  # noqa: E402
from ecoil_sim.registry import RuleRegistry  # noqa: E402
from ecoil_sim.retrieval import TemporalGraphRAG  # noqa: E402
from ecoil_sim.rules import FallbackPolicy  # noqa: E402
from ecoil_sim.sim.engine import SimulationEngine  # noqa: E402
from ecoil_sim.storage import SimulationStore  # noqa: E402
from ecoil_sim.validation import ActionValidator  # noqa: E402

GOLD = PROJECT_ROOT / "data" / "regulationDB" / "NetworkRegulatorGene.tsv"
UP_STATES = {"expressed", "overexpressed", "active", "high", "medium"}
DOWN_STATES = {"repressed", "knocked_out", "inhibited", "degraded", "low", "absent"}


def parse_args():
    p = argparse.ArgumentParser(description="RegulonDB-grounded perturbation benchmark.")
    p.add_argument("--config", type=Path, default=Path("configs/simulation.yaml"))
    p.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    p.add_argument("--gold", type=Path, default=GOLD)
    p.add_argument("--mode", choices=("mock", "llm", "both"), default="mock")
    p.add_argument("--max-tfs", type=int, default=30, help="number of regulators to test (by target count)")
    p.add_argument("--rounds", type=int, default=3)
    p.add_argument("--max-active-agents", type=int, default=256)
    p.add_argument("--output-root", type=Path, default=Path("runs/_benchmark"))
    return p.parse_args()


def load_gold(path: Path):
    rows = []
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if line.startswith("#") or not line.strip():
                continue
            cols = [c.strip() for c in line.rstrip("\n").split("\t")]
            if len(cols) >= 6 and cols[1] and cols[4] and cols[5] in ("+", "-"):
                rows.append((cols[1], cols[4], cols[5]))
    return rows


def name_index(graph: StaticGraph):
    idx = defaultdict(set)
    for e in graph.entities.values():
        for key in [e.name] + list(e.aliases):
            k = key.strip().lower()
            if k:
                idx[k].add(e.entity_id)
    return idx


def regulator_source(graph: StaticGraph, reg_ids: set) -> str:
    """Pick the entity among reg_ids that actually sources regulatory edges."""
    best, best_deg = None, -1
    for rid in reg_ids:
        deg = sum(
            1 for e in graph.out_edges.get(rid, []) if e.relation_type in ("activates", "represses")
        )
        if deg > best_deg:
            best, best_deg = rid, deg
    return best if best_deg > 0 else None


def build_cases(graph: StaticGraph, gold):
    """regulator_source_id -> list of (target_gene_id, expected_dir) for single-regulator targets."""
    idx = name_index(graph)
    # target gene -> set of (regulator_name, sign)
    regs_per_target = defaultdict(set)
    for reg, tgt, sign in gold:
        regs_per_target[tgt.lower()].add((reg.lower(), sign))
    cases = defaultdict(list)
    multi = 0
    for tgt_l, regs in regs_per_target.items():
        if len(regs) != 1:
            multi += 1
            continue
        (reg_l, sign), = tuple(regs)
        tgt_ids = [i for i in idx.get(tgt_l, set()) if graph.entities[i].entity_type == "gene"]
        if not tgt_ids:
            continue
        src = regulator_source(graph, idx.get(reg_l, set()))
        if not src:
            continue
        expected = "down" if sign == "+" else "up"  # KO activator -> down; KO repressor -> up
        cases[src].append((tgt_ids[0], expected))
    return cases, multi


def build_engine(deps, mode, store_root, args):
    client = RuleBasedMockLLM() if mode == "mock" else AsyncVLLMClient(
        base_url=deps["llm_cfg"].get("base_url", "http://localhost:8000/v1"),
        api_key=deps["llm_cfg"].get("api_key", "EMPTY"),
        model=deps["llm_cfg"].get("model", ""),
        max_concurrency=int(deps["run_cfg"].get("max_concurrency_per_gpu", 50)) * 2,
        timeout_seconds=float(deps["run_cfg"].get("timeout_seconds", 120)),
        max_retries=int(deps["run_cfg"].get("max_retries", 2)),
        max_tokens=int(deps["llm_cfg"].get("decision_max_tokens", 256)),
        temperature=float(deps["llm_cfg"].get("temperature", 0.2)),
        top_p=float(deps["llm_cfg"].get("top_p", 0.8)),
        guided_json=load_guided_json(deps["model_config"], PROJECT_ROOT),
        enable_thinking=bool(deps["llm_cfg"].get("enable_thinking", False)),
    )
    store_root.mkdir(parents=True, exist_ok=True)
    return SimulationEngine(
        graph=deps["graph"], registry=deps["registry"], retriever=deps["retriever"],
        prompt_builder=deps["prompt_builder"], store=SimulationStore(store_root), llm_client=client,
        name_resolver=deps["name_resolver"], action_interpreter=deps["action_interpreter"],
        validator=deps["validator"],
    )


def direction_of(state) -> str:
    """Net expression direction, folding the two regulatory axes.

    Genes carry permissibility (state: expressed/repressed) AND rate
    (efficiency: low/high). An activator loss keeps a gene 'expressed' but drops
    its efficiency -> expression is still DOWN. RegulonDB's +/- maps to this
    combined direction, so we must read both axes.
    """
    if state is None:
        return "none"
    eff = getattr(state, "efficiency", "")
    # rate axis dominates when permissibility is unchanged
    if state.state == "overexpressed" or eff == "high":
        return "up"
    if eff == "low":
        return "down"
    if state.state in DOWN_STATES or state.abundance_label in ("low", "absent"):
        return "down"
    if state.state in UP_STATES or state.abundance_label in ("high", "medium"):
        return "up"
    return "none"


def state_signature(state) -> tuple:
    if state is None:
        return ()
    return (state.state, getattr(state, "efficiency", ""), state.abundance_label)


async def score_mode(deps, cases, mode, args, out_dir):
    correct = scorable = unreachable = 0
    per_tf = []
    tested = list(cases.items())[: args.max_tfs]
    for src, targets in tested:
        engine = build_engine(deps, mode, out_dir / f"{mode}__{src.replace('/', '_')}", args)
        perturb = [{"entity_id": src, "state": "inhibited", "source": "benchmark",
                    "input_source": "regulondb_benchmark", "reason": "KO regulator"}]
        state = await engine.run(perturbations=perturb, max_rounds=args.rounds,
                                 max_active_agents=args.max_active_agents,
                                 initial_profile=deps["initial_profile"])
        tf_correct = tf_total = tf_unreached = 0
        baseline = deps["baseline_states"]
        for tgt_id, expected in targets:
            obs = state.states.get(tgt_id)
            # only score targets that actually moved from baseline (any axis)
            moved = obs is not None and state_signature(obs) != baseline.get(tgt_id, ())
            if not moved:
                tf_unreached += 1
                continue
            tf_total += 1
            tf_correct += int(direction_of(obs) == expected)
        correct += tf_correct
        scorable += tf_total
        unreachable += tf_unreached
        per_tf.append({"regulator": src, "name": deps["graph"].entities[src].name,
                       "targets": len(targets), "scored": tf_total, "correct": tf_correct,
                       "unreachable": tf_unreached})
    return {
        "mode": mode, "tested_regulators": len(tested),
        "direction_accuracy": round(correct / scorable, 3) if scorable else None,
        "correct": correct, "scorable": scorable, "unreachable": unreachable,
        "per_regulator": per_tf,
    }


def build_deps(config: dict, model_config: dict) -> dict:
    """Build the shared simulation dependencies (graph/registry/retriever/etc.).

    Reused by benchmark_expression.py so both benchmarks share one wiring.
    """
    from ecoil_sim.state import TemporalState
    gcfg = config.get("graph", {})
    sim_cfg = config.get("simulation", {})
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / gcfg.get("normalized_dir", "data/normalized"))
    registry = RuleRegistry.from_registry_dir(PROJECT_ROOT / gcfg.get("registry_dir", "data/registry"))
    edge_cfg = load_yaml_like(PROJECT_ROOT / gcfg.get("edge_weights", "configs/edge_weights.yaml"))
    name_resolver = NameResolver(graph.entities.values())
    fb = FallbackPolicy.from_config(PROJECT_ROOT / config.get("fallback", {}).get("policy", "configs/fallback_rules.yaml"))
    profile_path = PROJECT_ROOT / sim_cfg.get("initial_profile", "data/initial_conditions/glucose_log_phase.yaml")
    initial_profile = load_yaml_like(profile_path) if profile_path.exists() else {}
    base_state = TemporalState.initialize(graph.entities.values(), initial_profile)
    baseline_states = {eid: state_signature(s) for eid, s in base_state.states.items()}
    return {
        "graph": graph, "registry": registry,
        "retriever": TemporalGraphRAG(graph, registry, edge_cfg.get("edge_weights", {}),
                                      edge_cfg.get("state_distance", {}),
                                      min_score=float(sim_cfg.get("min_retrieval_score", 0.2))),
        "prompt_builder": PromptBuilder(PROJECT_ROOT / "prompts/agent_decision.system.md"),
        "name_resolver": name_resolver,
        "action_interpreter": ActionInterpreter(graph, fallback_policy=fb),
        "validator": ActionValidator(name_resolver=name_resolver),
        "initial_profile": initial_profile, "baseline_states": baseline_states,
        "model_config": model_config, "llm_cfg": model_config.get("llm", {}),
        "run_cfg": config.get("llm", {}),
    }


def main() -> int:
    args = parse_args()
    config = load_yaml_like(PROJECT_ROOT / args.config)
    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    deps = build_deps(config, model_config)
    graph = deps["graph"]

    cases, multi = build_cases(graph, load_gold(PROJECT_ROOT / args.gold))
    cases = dict(sorted(cases.items(), key=lambda kv: -len(kv[1])))  # most-targets first
    total_single = sum(len(v) for v in cases.values())
    print(f"single-regulator target cases: {total_single} across {len(cases)} regulators; "
          f"multi-regulator targets (deferred, need expression data): {multi}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = PROJECT_ROOT / args.output_root / timestamp
    out_dir.mkdir(parents=True, exist_ok=True)
    modes = ["mock", "llm"] if args.mode == "both" else [args.mode]
    results = {}
    for m in modes:
        print(f"[{m}] running {min(args.max_tfs, len(cases))} regulators...")
        results[m] = asyncio.run(score_mode(deps, cases, m, args, out_dir))
        r = results[m]
        print(f"  [{m}] direction_accuracy={r['direction_accuracy']} "
              f"(correct {r['correct']}/{r['scorable']}); unreachable={r['unreachable']}")

    (out_dir / "benchmark.json").write_text(
        json.dumps({"timestamp": timestamp, "single_regulator_cases": total_single,
                    "multi_regulator_targets_deferred": multi, "results": results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {out_dir / 'benchmark.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
