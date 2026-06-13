#!/usr/bin/env python3
"""Quantitative phenotype scorer — the measurable closed loop.

Unlike ``eval_baseline.py`` (qualitative side-by-side reasoning traces for a
human), this script produces *numbers*: for every pattern in
``data/phenotypes/phenotype_db.yaml`` it runs the simulator, compares the final
state against the pattern's ``expected_states`` / ``expected_abundance``, and
reports per-pattern and per-level (L0/L1/L2/L3) accuracy.

Why this exists
---------------
The project's thesis is "decisions to the model". This script measures whether
that pays off: it scores ``--mode mock`` and ``--mode llm`` on the same battery
so you can see, per signal level, how much accuracy the LLM adds over the
deterministic mock. The interesting rows are L2+ (direction conflicts): the mock
opts out there by design, so any L2+ accuracy is the LLM earning its keep.

Metrics
-------
* For a pattern with ``expected_states`` / ``expected_abundance``:
  ``state_acc`` = matched expected states / total expected states (same for
  abundance). ``pattern_score`` = (matched states + matched abundance) /
  (total states + total abundance).
* For the L0 negative control (``no_signal_baseline``, no expected change):
  ``pattern_score`` = 1.0 iff the run produced zero changes, else
  ``max(0, 1 - spurious_changes / spurious_tolerance)``.
* A pattern with no ``signals`` block and level != L0 is **unrunnable** (there
  is no perturbation to drive it) and is reported separately, not scored.

LLM runs use temperature > 0, so pass ``--repeat N`` to measure variance: the
script reports mean ± stdev of ``pattern_score`` across repeats.

Usage
-----
    # Deterministic baseline (no vLLM needed) — verify the harness:
    python scripts/score_phenotypes.py --mode mock

    # Real model (needs vLLM up; see configs/model.qwen35_9b.yaml):
    python scripts/score_phenotypes.py --mode llm --repeat 3

    # Head-to-head, the headline number:
    python scripts/score_phenotypes.py --mode both --repeat 3 --level L2

Output: ``runs/_scorecard/<timestamp>/scorecard.json`` + ``scorecard.md``.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

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
from ecoil_sim.state import TemporalState  # noqa: E402
from ecoil_sim.storage import SimulationStore  # noqa: E402
from ecoil_sim.validation import ActionValidator  # noqa: E402

SPURIOUS_TOLERANCE = 10  # L0: this many spurious changes drives the score to 0


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Quantitative phenotype scorer (mock vs LLM).")
    p.add_argument("--config", type=Path, default=Path("configs/simulation.yaml"))
    p.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    p.add_argument("--phenotype-db", type=Path, default=Path("data/phenotypes/phenotype_db.yaml"))
    p.add_argument("--mode", choices=("mock", "llm", "both"), default="mock")
    p.add_argument("--level", choices=("L0", "L1", "L2", "L3", "L4", "all"), default="all")
    p.add_argument("--pattern", default=None, help="Run only this pattern id")
    p.add_argument("--rounds", type=int, default=4)
    p.add_argument("--max-active-agents", type=int, default=128)
    p.add_argument("--repeat", type=int, default=1, help="Repeats per pattern (LLM variance)")
    p.add_argument("--output-root", type=Path, default=Path("runs/_scorecard"))
    return p.parse_args()


# --------------------------------------------------------------------------- #
# Pattern loading / perturbation derivation
# --------------------------------------------------------------------------- #
def load_patterns(path: Path) -> Dict[str, Dict]:
    raw = load_yaml_like(path)
    return {pid: spec for pid, spec in raw.items() if isinstance(spec, dict)}


def filter_patterns(patterns: Dict[str, Dict], level: str, pattern_id: Optional[str]) -> List[Tuple[str, Dict]]:
    out = []
    for pid, spec in patterns.items():
        if pattern_id and pid != pattern_id:
            continue
        if level != "all" and spec.get("signal_level", "L1") != level:
            continue
        out.append((pid, spec))
    return out


def derive_perturbations(spec: Dict) -> List[Dict]:
    signals_by_target = spec.get("signals", {})
    if not isinstance(signals_by_target, dict) or not signals_by_target:
        return []
    seen: Dict[Tuple[str, str], Dict] = {}
    for target, signals in signals_by_target.items():
        if not isinstance(signals, list):
            continue
        for signal in signals:
            if not isinstance(signal, dict):
                continue
            source = signal.get("from", "")
            state_value = signal.get("state", "")
            if not source or not state_value:
                continue
            seen[(source, state_value)] = {
                "entity_id": source,
                "state": state_value,
                "source": "score_pattern",
                "input_source": "phenotype_db",
                "reason": f"derived from pattern signal -> {target}",
            }
    return list(seen.values())


# --------------------------------------------------------------------------- #
# Engine wiring
# --------------------------------------------------------------------------- #
def build_dependencies(args) -> Dict:
    config = load_yaml_like(PROJECT_ROOT / args.config)
    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    graph_cfg = config.get("graph", {})
    sim_cfg = config.get("simulation", {})
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / graph_cfg.get("normalized_dir", "data/normalized"))
    registry = RuleRegistry.from_registry_dir(PROJECT_ROOT / graph_cfg.get("registry_dir", "data/registry"))
    edge_cfg = load_yaml_like(PROJECT_ROOT / graph_cfg.get("edge_weights", "configs/edge_weights.yaml"))
    retriever = TemporalGraphRAG(
        graph=graph,
        registry=registry,
        edge_weights=edge_cfg.get("edge_weights", {}),
        state_distance=edge_cfg.get("state_distance", {}),
        min_score=float(sim_cfg.get("min_retrieval_score", 0.2)),
    )
    fallback_path = PROJECT_ROOT / config.get("fallback", {}).get("policy", "configs/fallback_rules.yaml")
    name_resolver = NameResolver(graph.entities.values())
    initial_profile_path = PROJECT_ROOT / sim_cfg.get(
        "initial_profile", "data/initial_conditions/glucose_log_phase.yaml"
    )
    initial_profile = load_yaml_like(initial_profile_path) if initial_profile_path.exists() else {}
    return {
        "config": config,
        "model_config": model_config,
        "graph": graph,
        "registry": registry,
        "retriever": retriever,
        "prompt_builder": PromptBuilder(PROJECT_ROOT / "prompts/agent_decision.system.md"),
        "fallback_policy": FallbackPolicy.from_config(fallback_path),
        "name_resolver": name_resolver,
        "validator": ActionValidator(name_resolver=name_resolver),
        "action_interpreter": ActionInterpreter(graph, fallback_policy=FallbackPolicy.from_config(fallback_path)),
        "initial_profile": initial_profile,
        "sim_cfg": sim_cfg,
    }


def make_llm_client(deps: Dict):
    llm_cfg = deps["model_config"].get("llm", {})
    run_cfg = deps["config"].get("llm", {})
    return AsyncVLLMClient(
        base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
        api_key=llm_cfg.get("api_key", "EMPTY"),
        model=llm_cfg.get("model", ""),
        max_concurrency=int(run_cfg.get("max_concurrency_per_gpu", 50)),
        timeout_seconds=float(run_cfg.get("timeout_seconds", 120)),
        max_retries=int(run_cfg.get("max_retries", 2)),
        max_tokens=int(llm_cfg.get("decision_max_tokens", 256)),
        temperature=float(llm_cfg.get("temperature", 0.2)),
        top_p=float(llm_cfg.get("top_p", 0.8)),
        guided_json=load_guided_json(deps["model_config"], PROJECT_ROOT),
        enable_thinking=bool(llm_cfg.get("enable_thinking", False)),
    )


async def run_once(deps: Dict, perturbations: List[Dict], mode: str, store_root: Path, args) -> TemporalState:
    client = RuleBasedMockLLM() if mode == "mock" else make_llm_client(deps)
    store_root.mkdir(parents=True, exist_ok=True)
    engine = SimulationEngine(
        graph=deps["graph"],
        registry=deps["registry"],
        retriever=deps["retriever"],
        prompt_builder=deps["prompt_builder"],
        store=SimulationStore(store_root),
        llm_client=client,
        name_resolver=deps["name_resolver"],
        action_interpreter=deps["action_interpreter"],
        validator=deps["validator"],
    )
    return await engine.run(
        perturbations=perturbations,
        max_rounds=args.rounds,
        max_active_agents=args.max_active_agents,
        steady_state_patience=int(deps["sim_cfg"].get("steady_state_patience", 2)),
        initial_profile=deps["initial_profile"],
    )


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #
def score_run(spec: Dict, state: TemporalState) -> Dict:
    level = spec.get("signal_level", "L1")
    expected_states = spec.get("expected_states", {}) or {}
    expected_abundance = spec.get("expected_abundance", {}) or {}

    # L0 negative control: any change is a failure.
    if level == "L0" and not expected_states and not expected_abundance:
        changed = [
            eid for eid, hist in state.history.items()
            if any(item.get("changed") for item in hist)
        ]
        spurious = len(changed)
        score = 1.0 if spurious == 0 else max(0.0, 1.0 - spurious / SPURIOUS_TOLERANCE)
        return {
            "scored": True,
            "kind": "negative_control",
            "pattern_score": round(score, 3),
            "spurious_changes": spurious,
            "spurious_examples": changed[:10],
        }

    state_total = len(expected_states)
    state_matched = 0
    state_detail = {}
    for eid, want in expected_states.items():
        obs = state.states.get(eid)
        got = obs.state if obs else None
        ok = got == want
        state_matched += int(ok)
        state_detail[eid] = {"expected": want, "observed": got, "match": ok}

    ab_total = len(expected_abundance)
    ab_matched = 0
    ab_detail = {}
    for eid, want in expected_abundance.items():
        obs = state.states.get(eid)
        got = obs.abundance_label if obs else None
        ok = got == want
        ab_matched += int(ok)
        ab_detail[eid] = {"expected": want, "observed": got, "match": ok}

    total = state_total + ab_total
    matched = state_matched + ab_matched
    return {
        "scored": True,
        "kind": "phenotype",
        "pattern_score": round(matched / total, 3) if total else 0.0,
        "state_acc": round(state_matched / state_total, 3) if state_total else None,
        "abundance_acc": round(ab_matched / ab_total, 3) if ab_total else None,
        "state_detail": state_detail,
        "abundance_detail": ab_detail,
    }


def unresolved_sources(deps: Dict, perturbations: List[Dict]) -> List[str]:
    graph = deps["graph"]
    return sorted({p["entity_id"] for p in perturbations if p["entity_id"] not in graph.entities})


async def score_pattern(deps: Dict, pid: str, spec: Dict, mode: str, args, out_dir: Path) -> Dict:
    perturbations = derive_perturbations(spec)
    level = spec.get("signal_level", "L1")
    missing = unresolved_sources(deps, perturbations)
    runnable_perts = [p for p in perturbations if p["entity_id"] not in missing]

    # Unrunnable: needs a perturbation but the pattern provides none (or all sources missing).
    if level != "L0" and not runnable_perts:
        return {
            "pattern_id": pid,
            "signal_level": level,
            "mode": mode,
            "scored": False,
            "reason": "no resolvable perturbation source" if perturbations else "no signals block",
            "unresolved_sources": missing,
        }

    scores: List[float] = []
    repeats_detail = []
    for i in range(max(1, args.repeat) if mode == "llm" else 1):
        store_root = out_dir / f"{pid}__{mode}__rep{i}"
        state = await run_once(deps, runnable_perts, mode, store_root, args)
        result = score_run(spec, state)
        scores.append(result["pattern_score"])
        repeats_detail.append(result)

    summary = {
        "pattern_id": pid,
        "signal_level": level,
        "mode": mode,
        "scored": True,
        "repeats": len(scores),
        "mean_score": round(statistics.mean(scores), 3),
        "stdev_score": round(statistics.pstdev(scores), 3) if len(scores) > 1 else 0.0,
        "scores": scores,
        "unresolved_sources": missing,
        "detail": repeats_detail[0],  # first repeat detail for inspection
    }
    return summary


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def aggregate_by_level(results: List[Dict]) -> Dict[str, Dict]:
    by_level: Dict[str, List[float]] = {}
    for r in results:
        if not r.get("scored"):
            continue
        by_level.setdefault(r["signal_level"], []).append(r["mean_score"])
    return {
        lvl: {"n": len(v), "mean_score": round(statistics.mean(v), 3)}
        for lvl, v in sorted(by_level.items())
    }


def render_scorecard_md(modes: List[str], all_results: Dict[str, List[Dict]], args) -> str:
    lines = ["# Phenotype scorecard", "", f"Generated: {datetime.now().isoformat(timespec='seconds')}", ""]
    lines.append(f"- config: `{args.config}`  rounds: {args.rounds}  max_active_agents: {args.max_active_agents}")
    lines.append(f"- repeats (llm): {args.repeat}")
    lines.append("")

    # Per-level summary, modes side by side.
    lines.append("## Accuracy by signal level")
    lines.append("")
    header = "| Level | " + " | ".join(f"{m} mean" for m in modes) + " | n |"
    sep = "| --- | " + " | ".join("---" for _ in modes) + " | --- |"
    lines.append(header)
    lines.append(sep)
    aggs = {m: aggregate_by_level(all_results[m]) for m in modes}
    all_levels = sorted({lvl for m in modes for lvl in aggs[m]})
    for lvl in all_levels:
        cells = []
        n = 0
        for m in modes:
            a = aggs[m].get(lvl)
            cells.append(f"{a['mean_score']:.3f}" if a else "—")
            n = max(n, a["n"] if a else 0)
        lines.append(f"| {lvl} | " + " | ".join(cells) + f" | {n} |")
    lines.append("")

    if "mock" in modes and "llm" in modes:
        lines.append("> **The headline:** on L2+ rows, `llm mean` should exceed `mock mean`. "
                     "If they tie, the LLM is not earning its keep on conflict resolution.")
        lines.append("")

    # Per-pattern detail per mode.
    for m in modes:
        lines.append(f"## Per-pattern detail — `{m}`")
        lines.append("")
        lines.append("| Pattern | Level | mean | stdev | scores | notes |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for r in all_results[m]:
            if not r.get("scored"):
                note = r.get("reason", "")
                if r.get("unresolved_sources"):
                    note += f" (missing: {', '.join(r['unresolved_sources'])})"
                lines.append(f"| `{r['pattern_id']}` | {r['signal_level']} | — | — | — | {note} |")
                continue
            scores = ", ".join(f"{s:.2f}" for s in r["scores"])
            note = ""
            if r.get("unresolved_sources"):
                note = f"missing src: {', '.join(r['unresolved_sources'])}"
            lines.append(
                f"| `{r['pattern_id']}` | {r['signal_level']} | {r['mean_score']:.3f} | "
                f"{r['stdev_score']:.3f} | {scores} | {note} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if not (PROJECT_ROOT / args.phenotype_db).exists():
        print(f"phenotype_db not found: {args.phenotype_db}")
        return 1
    patterns = load_patterns(PROJECT_ROOT / args.phenotype_db)
    selected = filter_patterns(patterns, args.level, args.pattern)
    if not selected:
        print("no patterns matched the filter")
        return 0

    deps = build_dependencies(args)
    modes = ["mock", "llm"] if args.mode == "both" else [args.mode]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = PROJECT_ROOT / args.output_root / timestamp
    out_dir.mkdir(parents=True, exist_ok=True)

    all_results: Dict[str, List[Dict]] = {m: [] for m in modes}
    for m in modes:
        for pid, spec in selected:
            print(f"[{m}] {pid} ({spec.get('signal_level','?')})")
            try:
                res = asyncio.run(score_pattern(deps, pid, spec, m, args, out_dir))
            except Exception as exc:  # keep the battery going; record the failure
                res = {"pattern_id": pid, "signal_level": spec.get("signal_level", "?"),
                       "mode": m, "scored": False, "reason": f"run error: {exc}"}
                print(f"   ! {exc}")
            all_results[m].append(res)

    scorecard = {
        "timestamp": timestamp,
        "config": str(args.config),
        "rounds": args.rounds,
        "repeats": args.repeat,
        "by_level": {m: aggregate_by_level(all_results[m]) for m in modes},
        "results": all_results,
    }
    (out_dir / "scorecard.json").write_text(json.dumps(scorecard, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "scorecard.md").write_text(render_scorecard_md(modes, all_results, args), encoding="utf-8")

    print(f"\nScorecard: {out_dir / 'scorecard.md'}")
    for m in modes:
        agg = aggregate_by_level(all_results[m])
        summary = "  ".join(f"{lvl}={a['mean_score']:.2f}(n={a['n']})" for lvl, a in agg.items())
        print(f"  [{m}] {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
