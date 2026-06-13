#!/usr/bin/env python3
"""Single-run side-by-side reasoning review: mock vs LLM.

This script does NOT produce statistical accuracy numbers. Its purpose is
qualitative: for each curated response pattern in
``data/phenotypes/phenotype_db.yaml`` it runs the simulator once with
the deterministic :class:`RuleBasedMockLLM` and once with the real
:class:`AsyncVLLMClient`, and lays out the resulting reasoning traces
so a human reviewer can decide whether the LLM is behaving like a
competent biologist or is hallucinating.

Output framing depends on signal complexity:

* **L0 / L1** — both mock and LLM should produce complete results.
  The script generates a side-by-side reasoning comparison; if the two
  diverge, the reviewer checks whether the LLM's reasoning is
  biologically justified.

* **L2 / L3** — the mock deliberately *opts out* at conflicting
  candidate agents (``conflict_free_only: true``). The mock run is
  therefore incomplete by design; comparing its truncated output with
  the LLM's full output is a category error. The script only shows
  the LLM's reasoning trace plus a clear "mock refused here" marker
  on each conflict node.

The key design principle recorded in each comparison is that every
Agent's LLM only sees its own annotation, its own current state, and
the signals arriving from its changed neighbours. It does not see
the global perturbation picture. This is what makes the L2
conflict resolution work: the LLM must read its annotation to decide
which conflicting signal wins.

Usage::

    # All L0/L1 patterns, both modes (the typical sanity check)
    python scripts/eval_baseline.py --mode both --level L1

    # Only the L2 conflict patterns (mock will be incomplete; LLM is the focus)
    python scripts/eval_baseline.py --mode both --level L2

    # A single L2 pattern, llm only
    python scripts/eval_baseline.py --mode llm --pattern lac_dual_signal_glucose_present

Output goes to ``runs/_eval_baseline/<pattern_id>/<mode>/`` plus a
``comparison.md`` next to the two runs, and a top-level ``INDEX.md``.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.actions import ActionInterpreter  # noqa: E402
from ecoil_sim.agents import PromptBuilder  # noqa: E402
from ecoil_sim.config import load_yaml_like  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.llm import (  # noqa: E402
    AsyncVLLMClient,
    NameResolver,
    RuleBasedMockLLM,
    compute_signals,
    build_conflict_report,
    load_guided_json,
)
from ecoil_sim.paths import PROJECT_ROOT  # noqa: E402
from ecoil_sim.registry import RuleRegistry  # noqa: E402
from ecoil_sim.retrieval import TemporalGraphRAG  # noqa: E402
from ecoil_sim.rules import FallbackPolicy  # noqa: E402
from ecoil_sim.sim.engine import run_sync, SimulationEngine  # noqa: E402
from ecoil_sim.storage import SimulationStore  # noqa: E402
from ecoil_sim.state import TemporalState  # noqa: E402
from ecoil_sim.validation import ActionValidator  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Single-run mock vs LLM reasoning comparison.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/simulation.yaml"),
    )
    parser.add_argument(
        "--model-config",
        type=Path,
        default=Path("configs/model.qwen35_9b.yaml"),
    )
    parser.add_argument(
        "--phenotype-db",
        type=Path,
        default=Path("data/phenotypes/phenotype_db.yaml"),
    )
    parser.add_argument(
        "--mode",
        choices=("mock", "llm", "both"),
        default="both",
    )
    parser.add_argument(
        "--level",
        choices=("L0", "L1", "L2", "L3", "L4", "all"),
        default="all",
    )
    parser.add_argument("--pattern", default=None, help="Run only this pattern id")
    parser.add_argument("--rounds", type=int, default=2)
    parser.add_argument("--max-active-agents", type=int, default=8)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("runs/_eval_baseline"),
    )
    return parser.parse_args()


def load_patterns(path: Path) -> Dict[str, Dict]:
    raw = load_yaml_like(path)
    return {pid: spec for pid, spec in raw.items() if isinstance(spec, dict)}


def filter_patterns(
    patterns: Dict[str, Dict],
    level: str,
    pattern_id: Optional[str],
) -> List[Tuple[str, Dict]]:
    out: List[Tuple[str, Dict]] = []
    for pid, spec in patterns.items():
        if pattern_id and pid != pattern_id:
            continue
        spec_level = spec.get("signal_level", "L1")
        if level != "all" and spec_level != level:
            continue
        out.append((pid, spec))
    return out


def derive_perturbations(spec: Dict) -> List[Dict]:
    """Translate the pattern's ``signals`` block into perturbation changes.

    Each signal in the spec lists an upstream source and the state it
    would be in once the perturbation is applied. We collect unique
    ``(source, state)`` pairs into the perturbation list so that the
    simulator sees exactly the multi-signal environment the pattern
    describes.

    If a pattern has no ``signals`` block, the perturbation list is
    empty — the pattern only constrains the post-conditions and the
    simulator is run from the default initial profile.
    """
    signals_by_target = spec.get("signals", {})
    if not signals_by_target:
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
                "source": "eval_pattern",
                "input_source": "phenotype_db",
                "reason": f"derived from pattern signal: {source} -> {target} via {signal.get('edge', '?')}",
            }
    return list(seen.values())


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
    prompt_builder = PromptBuilder(PROJECT_ROOT / "prompts/agent_decision.system.md")
    fallback_path = PROJECT_ROOT / config.get("fallback", {}).get("policy", "configs/fallback_rules.yaml")
    fallback_policy = FallbackPolicy.from_config(fallback_path)
    name_resolver = NameResolver(graph.entities.values())
    validator = ActionValidator(name_resolver=name_resolver)
    action_interpreter = ActionInterpreter(graph, fallback_policy=fallback_policy)
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
        "prompt_builder": prompt_builder,
        "fallback_policy": fallback_policy,
        "name_resolver": name_resolver,
        "validator": validator,
        "action_interpreter": action_interpreter,
        "initial_profile": initial_profile,
        "sim_cfg": sim_cfg,
    }


def make_engine(deps: Dict, llm_client, store_root: Path) -> Tuple[SimulationEngine, Path]:
    store_root.mkdir(parents=True, exist_ok=True)
    store = SimulationStore(store_root)
    engine = SimulationEngine(
        graph=deps["graph"],
        registry=deps["registry"],
        retriever=deps["retriever"],
        prompt_builder=deps["prompt_builder"],
        store=store,
        llm_client=llm_client,
        name_resolver=deps["name_resolver"],
        action_interpreter=deps["action_interpreter"],
        validator=deps["validator"],
    )
    return engine, store_root


async def run_one(
    deps: Dict,
    perturbations: List[Dict],
    store_root: Path,
    mode: str,
    args,
) -> Tuple[TemporalState, Path]:
    if mode == "mock":
        llm_client = RuleBasedMockLLM()
    else:
        model_cfg = deps["model_config"]
        llm_cfg = model_cfg.get("llm", {})
        gpu_count = 1
        max_concurrency = gpu_count * int(
            deps["config"].get("llm", {}).get("max_concurrency_per_gpu", 50)
        )
        llm_client = AsyncVLLMClient(
            base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
            api_key=llm_cfg.get("api_key", "EMPTY"),
            model=llm_cfg.get("model", ""),
            max_concurrency=max_concurrency,
            timeout_seconds=float(llm_cfg.get("timeout_seconds", 120)),
            max_retries=int(llm_cfg.get("max_retries", 2)),
            max_tokens=int(llm_cfg.get("decision_max_tokens", 256)),
            temperature=float(llm_cfg.get("temperature", 0.2)),
            top_p=float(llm_cfg.get("top_p", 0.8)),
            guided_json=load_guided_json(model_cfg, PROJECT_ROOT),
            enable_thinking=bool(llm_cfg.get("enable_thinking", False)),
        )
    engine, store_root = make_engine(deps, llm_client, store_root)
    state = await engine.run(
        perturbations=perturbations,
        max_rounds=args.rounds,
        max_active_agents=args.max_active_agents,
        steady_state_patience=int(deps["sim_cfg"].get("steady_state_patience", 2)),
        initial_profile=deps["initial_profile"],
    )
    return state, store_root


def _rederive_local_views(
    state_path: Path,
    graph: StaticGraph,
    name_resolver: NameResolver,
) -> Dict[str, Dict]:
    """Re-derive the per-agent LLM local view from the saved run.

    The local view is what the LLM *would* have seen at the start of
    round N+1: each candidate's annotation, current state, and the
    signals arriving from changed neighbours. We re-derive it from the
    propagation edges written to disk so the reviewer can see what the
    LLM reasoned from without changing the engine to persist prompts.
    """
    rounds_dir = state_path / "rounds"
    if not rounds_dir.exists():
        return {}
    snapshots: List[TemporalState] = []
    for snap_path in sorted(rounds_dir.glob("round_*.json"), key=lambda p: int(p.stem.split("_")[-1])):
        snap = json.loads(snap_path.read_text(encoding="utf-8"))
        snapshots.append(snap)

    local_views: Dict[str, Dict] = {}
    for prev_snap, cur_snap in zip(snapshots, snapshots[1:]):
        prev_changes: Dict[str, Dict] = {}
        for entity_id, agent in prev_snap.get("states", {}).items():
            if not agent.get("changed"):
                continue
            prev_changes[entity_id] = agent
        if not prev_changes:
            continue

        # Build a TemporalState equivalent at the start of cur_snap so
        # we can ask the retriever-style helpers for the conflict view.
        state_at_start = _build_state_from_snapshot(graph, prev_snap)

        # Group propagation edges by target for this round
        target_to_sources: Dict[str, List[str]] = defaultdict(list)
        for edge in cur_snap.get("propagation_edges", []) or []:
            if edge.get("round") != cur_snap.get("round"):
                continue
            target_to_sources[edge["target"]].append(edge["source"])

        for target, sources in target_to_sources.items():
            relevant_sources = [s for s in sources if s in prev_changes]
            if not relevant_sources:
                continue
            entity = graph.entities.get(target)
            if not entity:
                continue
            local_views[target] = {
                "round": cur_snap.get("round"),
                "name": name_resolver.to_public(target),
                "annotation": entity.annotation[:1800],
                "current_state": state_at_start.states[target].state if target in state_at_start.states else "",
                "current_abundance": state_at_start.states[target].abundance_label if target in state_at_start.states else "",
                "changed_neighbors": {
                    s: {
                        "state": prev_changes[s].get("state", ""),
                        "abundance": prev_changes[s].get("abundance_label", ""),
                    }
                    for s in relevant_sources
                },
            }
    return local_views


def _build_state_from_snapshot(graph: StaticGraph, snap: Dict) -> TemporalState:
    state = TemporalState.initialize(graph.entities.values())
    for entity_id, agent in snap.get("states", {}).items():
        if entity_id not in state.states:
            continue
        state.states[entity_id].state = agent.get("state", state.states[entity_id].state)
        state.states[entity_id].abundance_label = agent.get("abundance_label", state.states[entity_id].abundance_label)
    return state


def _agent_traces_from_stage_reports(store_root: Path) -> Dict[str, Dict]:
    """Collect reasoning traces for changed agents plus the final state of every entity.

    The stage report only records agents whose ``changed`` flag is True.
    For an L1 single-signal pattern the LLM/mock may emit an action that
    is a no-op because the candidate was already in the expected state
    (for example, the lac operon genes are pre-set to ``repressed`` in
    the glucose log phase initial profile). A reviewer still needs to
    see that the agent was considered, what reasoning was emitted, and
    what the final state ended up being. This collector joins the
    stage report with the final-round snapshot so the comparison.md can
    show both the reasoning and the final state of every expected
    entity.
    """
    traces: Dict[str, Dict] = {}
    stages_dir = store_root / "stage_reports"
    if not stages_dir.exists():
        return traces
    for stage_path in sorted(stages_dir.glob("round_*.json")):
        stage = json.loads(stage_path.read_text(encoding="utf-8"))
        for change in stage.get("new_changes", []) or []:
            entity_id = change.get("entity_id", "")
            if not entity_id:
                continue
            payload = traces.setdefault(
                entity_id,
                {
                    "rounds": [],
                    "final_state": change.get("state"),
                    "final_abundance": change.get("abundance_label"),
                    "changed": True,
                },
            )
            payload["rounds"].append(
                {
                    "round": change.get("round"),
                    "reason": change.get("reason"),
                    "metadata": change.get("metadata", {}) or {},
                    "changed_neighbors": change.get("changed_neighbors", []) or [],
                }
            )
            payload["final_state"] = change.get("state", payload["final_state"])
            payload["final_abundance"] = change.get("abundance_label", payload["final_abundance"])
    return traces


def _final_state_overview(store_root: Path) -> Dict[str, Dict[str, str]]:
    """Read the last round snapshot and return the final state of every entity."""
    rounds_dir = store_root / "rounds"
    if not rounds_dir.exists():
        return {}
    snapshots = sorted(rounds_dir.glob("round_*.json"), key=lambda p: int(p.stem.split("_")[-1]))
    if not snapshots:
        return {}
    final = json.loads(snapshots[-1].read_text(encoding="utf-8"))
    return {
        entity_id: {
            "state": agent.get("state", ""),
            "abundance": agent.get("abundance_label", ""),
            "efficiency": agent.get("efficiency", ""),
        }
        for entity_id, agent in (final.get("states") or {}).items()
    }


def _format_final_cell(row: Dict[str, str]) -> str:
    """Render an entity's final state / abundance / efficiency for the table."""
    if not row:
        return "—"
    parts = []
    state = row.get("state") or ""
    if state:
        parts.append(f"state=`{state}`")
    abundance = row.get("abundance") or ""
    if abundance:
        parts.append(f"abundance=`{abundance}`")
    efficiency = row.get("efficiency") or ""
    if efficiency:
        parts.append(f"efficiency=`{efficiency}`")
    return "<br>".join(parts) or "—"


def _format_local_view(view: Dict) -> List[str]:
    lines: List[str] = []
    lines.append(f"**Round {view['round']} — what the LLM saw for this agent only**")
    lines.append("")
    lines.append(f"- Agent: `{view['name']}`")
    annotation = view.get("annotation", "")
    if annotation:
        lines.append("- Annotation (excerpt):")
        lines.append("  ```text")
        for line in annotation.splitlines()[:12]:
            lines.append("  " + line)
        lines.append("  ```")
    lines.append(f"- Current state: `{view['current_state']}`, abundance: `{view['current_abundance']}`")
    if view.get("changed_neighbors"):
        lines.append("- Signals arriving (only the upstream regulators, no global view):")
        for source, info in view["changed_neighbors"].items():
            lines.append(f"  - `{source}` → state=`{info['state']}` abundance=`{info['abundance']}`")
    return lines


def _format_trace_block(label: str, traces: Dict[str, Dict], show_raw: bool) -> List[str]:
    lines: List[str] = []
    lines.append(f"### {label}")
    if not traces:
        lines.append("")
        lines.append("_no changed agents_")
        return lines
    for entity_id, payload in traces.items():
        lines.append("")
        lines.append(f"#### `{entity_id}` → state=`{payload['final_state']}`, abundance=`{payload['final_abundance']}`")
        for entry in payload["rounds"]:
            metadata = entry.get("metadata", {}) or {}
            lines.append("")
            lines.append(f"**Round {entry['round']}** — reason: `{entry['reason']}`")
            if metadata.get("deterministic_fallback"):
                lines.append(f"- **fallback triggered**: `{metadata.get('fallback_rule', '?')}`")
            if metadata.get("_error"):
                lines.append(f"- error: `{metadata.get('_error')}`")
            if metadata.get("_parse_diagnostics"):
                diag = metadata["_parse_diagnostics"]
                lines.append(
                    f"- parse: `{diag.get('final_method')}` "
                    f"(think stripped: `{diag.get('stripped_think')}`, "
                    f"fence stripped: `{diag.get('stripped_fence')}`, "
                    f"truncated repair: `{diag.get('repaired_truncated')}`)"
                )
            if show_raw:
                raw = metadata.get("llm_raw_content")
                if raw:
                    lines.append("")
                    lines.append("  ```text")
                    for raw_line in str(raw).splitlines()[:60]:
                        lines.append("  " + raw_line)
                    lines.append("  ```")
    return lines


def render_comparison_markdown(
    pattern_id: str,
    spec: Dict,
    perturbations: List[Dict],
    mock_traces: Dict[str, Dict],
    llm_traces: Dict[str, Dict],
    mock_local_views: Dict[str, Dict],
    llm_local_views: Dict[str, Dict],
    mock_refusal_summary: Dict[str, List[str]],
    mock_final_states: Dict[str, Dict[str, str]],
    llm_final_states: Dict[str, Dict[str, str]],
) -> str:
    expected_states = spec.get("expected_states", {}) or {}
    expected_abundance = spec.get("expected_abundance", {}) or {}
    description = (spec.get("description", "") or "").strip()
    signal_level = spec.get("signal_level", "L1")
    notes = (spec.get("notes", "") or "").strip()
    is_conflict_level = signal_level in {"L2", "L3", "L4"}
    expected_entities = sorted(set(expected_states.keys()) | set(expected_abundance.keys()))

    lines: List[str] = []
    lines.append(f"# Reasoning review: `{pattern_id}` ({signal_level})")
    lines.append("")
    if description:
        lines.append("## Pattern description")
        lines.append("")
        lines.append(description.strip())
        lines.append("")

    lines.append("## Global perturbation (the reviewer's view, NOT shown to the LLM)")
    lines.append("")
    if not perturbations:
        lines.append("_no perturbations — baseline pattern_")
    else:
        for p in perturbations:
            lines.append(f"- `{p['entity_id']}` → state=`{p['state']}` ({p.get('reason', '')})")
    lines.append("")

    lines.append("## Expected outcome")
    lines.append("")
    if expected_states:
        lines.append("| Entity | Expected state |")
        lines.append("| --- | --- |")
        for eid, st in expected_states.items():
            lines.append(f"| `{eid}` | `{st}` |")
    if expected_abundance:
        lines.append("")
        lines.append("| Entity | Expected abundance |")
        lines.append("| --- | --- |")
        for eid, ab in expected_abundance.items():
            lines.append(f"| `{eid}` | `{ab}` |")
    lines.append("")

    if expected_entities:
        lines.append("## Final states vs expected")
        lines.append("")
        lines.append("| Entity | Expected | Mock final | LLM final |")
        lines.append("| --- | --- | --- | --- |")
        for eid in expected_entities:
            expected = []
            if eid in expected_states:
                expected.append(f"state=`{expected_states[eid]}`")
            if eid in expected_abundance:
                expected.append(f"abundance=`{expected_abundance[eid]}`")
            expected_str = "<br>".join(expected) or "—"
            mock_row = mock_final_states.get(eid, {})
            llm_row = llm_final_states.get(eid, {})
            mock_str = _format_final_cell(mock_row)
            llm_str = _format_final_cell(llm_row)
            lines.append(f"| `{eid}` | {expected_str} | {mock_str} | {llm_str} |")
        lines.append("")

    if notes:
        lines.append("> " + notes.replace("\n", "\n> "))
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Design reminder")
    lines.append("")
    lines.append(
        "Each Agent's LLM only sees its own annotation, its own current state, and the signals arriving from its changed neighbours. It does **not** see the global perturbation. The local-view block below shows exactly what the LLM had to reason from."
    )
    lines.append("")

    if is_conflict_level:
        # ------------------------------------------------------------------
        # L2 / L3 framing: focus on LLM reasoning. Mock is expected to
        # be partial, so the comparison framing changes.
        # ------------------------------------------------------------------
        lines.append("## Mock run (expected to be INCOMPLETE for L2+ patterns)")
        lines.append("")
        if mock_refusal_summary:
            lines.append("Mock refused to act on the following conflict nodes:")
            for entity_id, reasons in mock_refusal_summary.items():
                lines.append(f"- `{entity_id}` — {', '.join(reasons)}")
            lines.append("")
        lines.append(
            "This is by design: the mock is not a priority judge. It deliberately *opts out* on direction-conflicting candidates and lets the LLM decide."
        )
        lines.append("")
        for trace_lines in [_format_trace_block("Mock reasoning trace (truncated)", mock_traces, show_raw=False)]:
            lines.extend(trace_lines)
        lines.append("")

        lines.append("## LLM run (the focus for L2+ patterns)")
        lines.append("")
        lines.append("### Local views — what each LLM actually saw")
        if not llm_local_views:
            lines.append("")
            lines.append("_no agents were awakened — the LLM was not consulted for this pattern_")
        for entity_id, view in llm_local_views.items():
            lines.append("")
            lines.append(f"#### `{entity_id}`")
            lines.append("")
            lines.extend(_format_local_view(view))
        lines.append("")
        for trace_lines in [_format_trace_block("LLM reasoning trace", llm_traces, show_raw=True)]:
            lines.extend(trace_lines)
    else:
        # ------------------------------------------------------------------
        # L0 / L1 framing: side-by-side reasoning comparison
        # ------------------------------------------------------------------
        lines.append("## Mock run")
        lines.append("")
        for trace_lines in [_format_trace_block("Mock reasoning trace", mock_traces, show_raw=False)]:
            lines.extend(trace_lines)
        lines.append("")

        lines.append("## LLM run")
        lines.append("")
        lines.append("### Local views — what each LLM actually saw")
        if not llm_local_views:
            lines.append("")
            lines.append("_no agents were awakened_")
        for entity_id, view in llm_local_views.items():
            lines.append("")
            lines.append(f"#### `{entity_id}`")
            lines.append("")
            lines.extend(_format_local_view(view))
        lines.append("")
        for trace_lines in [_format_trace_block("LLM reasoning trace", llm_traces, show_raw=True)]:
            lines.extend(trace_lines)

    lines.append("---")
    lines.append("")
    lines.append("## Review checklist")
    lines.append("")
    if is_conflict_level:
        lines.append("- [ ] Mock's refusal list matches the conflict nodes in the LLM run")
        lines.append("- [ ] LLM's reason references its own annotation (not the global perturbation)")
        lines.append("- [ ] LLM's direction matches the expected outcome")
        lines.append("- [ ] LLM did not invent new entities or relations")
        lines.append("- [ ] LLM did not assume it could see allolactose / lactose etc. directly")
    else:
        lines.append("- [ ] Mock and LLM final states agree (or LLM's deviation is justified)")
        lines.append("- [ ] LLM's reason is grounded in candidate rules and annotation")
        lines.append("- [ ] LLM's direction matches the expected outcome")
        lines.append("- [ ] LLM did not invent new entities or relations")
        lines.append("- [ ] No silent fallback was triggered without explanation")
    return "\n".join(lines) + "\n"


def _detect_mock_refusals(deps: Dict, traces: Dict[str, Dict]) -> Dict[str, List[str]]:
    """Look at trace metadata to find agents where mock refused due to conflict."""
    refusals: Dict[str, List[str]] = {}
    for entity_id, payload in traces.items():
        for entry in payload.get("rounds", []):
            metadata = entry.get("metadata", {}) or {}
            if not metadata.get("deterministic_fallback"):
                continue
            fallback_rule = metadata.get("fallback_rule", "")
            if "mock refused" in metadata.get("reason", "").lower():
                refusals.setdefault(entity_id, []).append(fallback_rule or "conflict_free_only")
            elif fallback_rule and "conflict" not in fallback_rule:
                # Mock did act — not a refusal
                continue
    return refusals


def main() -> int:
    args = parse_args()
    if not args.phenotype_db.exists():
        print(f"phenotype_db not found: {args.phenotype_db}")
        return 1
    patterns = load_patterns(args.phenotype_db)
    selected = filter_patterns(patterns, args.level, args.pattern)
    if not selected:
        print("no patterns matched the filter")
        return 0
    deps = build_dependencies(args)
    output_root: Path = args.output_root
    output_root.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    index_rows: List[Dict] = []
    for pattern_id, spec in selected:
        perturbations = derive_perturbations(spec)
        pattern_dir = output_root / f"{timestamp}_{pattern_id}"
        pattern_dir.mkdir(parents=True, exist_ok=True)
        mock_traces: Dict[str, Dict] = {}
        llm_traces: Dict[str, Dict] = {}
        mock_local_views: Dict[str, Dict] = {}
        llm_local_views: Dict[str, Dict] = {}
        mock_refusal_summary: Dict[str, List[str]] = {}
        mock_final_states: Dict[str, Dict[str, str]] = {}
        llm_final_states: Dict[str, Dict[str, str]] = {}
        if args.mode in ("mock", "both"):
            mock_root = pattern_dir / "mock"
            print(f"[mock] {pattern_id}  → {mock_root}")
            mock_state, mock_root = asyncio.run(
                run_one(deps, perturbations, mock_root, "mock", args)
            )
            mock_traces = _agent_traces_from_stage_reports(mock_root)
            mock_local_views = _rederive_local_views(mock_root, deps["graph"], deps["name_resolver"])
            mock_refusal_summary = _detect_mock_refusals(deps, mock_traces)
            mock_final_states = _final_state_overview(mock_root)
        if args.mode in ("llm", "both"):
            llm_root = pattern_dir / "llm"
            print(f"[llm ] {pattern_id}  → {llm_root}")
            try:
                llm_state, llm_root = asyncio.run(
                    run_one(deps, perturbations, llm_root, "llm", args)
                )
                llm_traces = _agent_traces_from_stage_reports(llm_root)
                llm_local_views = _rederive_local_views(llm_root, deps["graph"], deps["name_resolver"])
                llm_final_states = _final_state_overview(llm_root)
            except Exception as exc:
                print(f"  LLM run failed: {exc}")
                llm_traces = {}
                llm_local_views = {}
                llm_final_states = {}
        comparison = render_comparison_markdown(
            pattern_id=pattern_id,
            spec=spec,
            perturbations=perturbations,
            mock_traces=mock_traces,
            llm_traces=llm_traces,
            mock_local_views=mock_local_views,
            llm_local_views=llm_local_views,
            mock_refusal_summary=mock_refusal_summary,
            mock_final_states=mock_final_states,
            llm_final_states=llm_final_states,
        )
        (pattern_dir / "comparison.md").write_text(comparison, encoding="utf-8")
        index_rows.append(
            {
                "pattern_id": pattern_id,
                "signal_level": spec.get("signal_level", "?"),
                "comparison": str(pattern_dir / "comparison.md"),
                "mock_state": str(pattern_dir / "mock") if mock_traces else None,
                "llm_state": str(pattern_dir / "llm") if llm_traces else None,
            }
        )

    # Top-level INDEX.md
    index_lines = ["# Eval baseline index", "", f"Generated: {timestamp}", ""]
    for row in index_rows:
        index_lines.append(
            f"- `{row['pattern_id']}` ({row['signal_level']}) — [comparison]({row['comparison']})"
        )
    index_path = output_root / f"INDEX_{timestamp}.md"
    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"\nWrote {len(index_rows)} comparison files. Index: {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
