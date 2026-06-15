"""Overflow spill: max_active_agents is a throughput cap, not a correctness knob.

When a round wakes more candidates than the budget, the overflow must carry to
later rounds (discrete turn-based), so a tight budget over more rounds covers the
same agents as a large budget. Regression for the dropped-overflow bug that made
the Cra budget artifact.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.actions import ActionInterpreter  # noqa: E402
from ecoil_sim.agents import PromptBuilder  # noqa: E402
from ecoil_sim.config import load_yaml_like  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.llm import NameResolver, RuleBasedMockLLM  # noqa: E402
from ecoil_sim.registry import RuleRegistry  # noqa: E402
from ecoil_sim.retrieval import TemporalGraphRAG  # noqa: E402
from ecoil_sim.rules import FallbackPolicy  # noqa: E402
from ecoil_sim.sim.engine import SimulationEngine, run_sync  # noqa: E402
from ecoil_sim.storage import SimulationStore  # noqa: E402
from ecoil_sim.validation import ActionValidator  # noqa: E402

GRAPH_DIR = PROJECT_ROOT / "data" / "normalized" / "simulation"
HUB = "protein.P0ACP1"  # Cra — ~78 regulatory targets, far more than a tiny budget


@pytest.fixture(scope="module")
def graph():
    g = StaticGraph.from_normalized_dir(GRAPH_DIR)
    if HUB not in g.entities:
        pytest.skip("Cra not in graph")
    return g


def _engine(graph, store_root):
    reg = RuleRegistry.from_registry_dir(PROJECT_ROOT / "data" / "registry" / "simulation")
    ew = load_yaml_like(PROJECT_ROOT / "configs" / "edge_weights.yaml")
    nr = NameResolver(graph.entities.values())
    fb = FallbackPolicy.from_config(PROJECT_ROOT / "configs" / "fallback_rules.yaml")
    return SimulationEngine(
        graph=graph, registry=reg,
        retriever=TemporalGraphRAG(graph, reg, ew.get("edge_weights", {}), ew.get("state_distance", {}), min_score=0.2),
        prompt_builder=PromptBuilder(PROJECT_ROOT / "prompts" / "agent_decision.system.md"),
        store=SimulationStore(store_root), llm_client=RuleBasedMockLLM(),
        name_resolver=nr, action_interpreter=ActionInterpreter(graph, fallback_policy=fb),
        validator=ActionValidator(name_resolver=nr),
    )


def _cra_targets(graph):
    return {e.target_id for e in graph.out_edges.get(HUB, []) if e.relation_type in ("activates", "represses")}


def _covered(graph, tmp_path, budget, rounds):
    state = run_sync(
        _engine(graph, tmp_path / f"b{budget}r{rounds}"),
        perturbations=[{"entity_id": HUB, "state": "inhibited", "source": "t", "input_source": "t", "reason": "probe"}],
        max_rounds=rounds, max_active_agents=budget,
    )
    changed = {e for e, h in state.history.items() if any(i.get("changed") for i in h)}
    return changed & _cra_targets(graph)


def test_overflow_spills_to_later_rounds(graph, tmp_path):
    targets = _cra_targets(graph)
    assert len(targets) > 8, "hub should have more targets than the tiny budget"
    few = _covered(graph, tmp_path, budget=4, rounds=2)
    many = _covered(graph, tmp_path, budget=4, rounds=20)
    # With the same tiny budget, more rounds must cover MORE targets (overflow
    # spilled instead of being dropped).
    assert len(many) > len(few)
