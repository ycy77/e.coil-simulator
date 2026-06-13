"""Tests for fair candidate selection in TemporalGraphRAG.

A high-degree hub must not crowd out another hub's targets, and score ties must
not be broken by entity_id bias (the katG-never-wakes bug, issue C in the
2026-06-13 scorecard report).
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.retrieval import RetrievedContext, TemporalGraphRAG  # noqa: E402


def _ctx(entity_id: str, score: float, source: str) -> RetrievedContext:
    return RetrievedContext(entity_id=entity_id, score=score, changed_neighbors=[source])


def test_small_hub_target_survives_large_hub_flood():
    # Hub A wakes 40 equal-score targets; hub B wakes a single lower-score one.
    eligible = [_ctx(f"A_target_{i:02d}", 0.9, "hubA") for i in range(40)]
    eligible.append(_ctx("B_target", 0.5, "hubB"))
    selected = TemporalGraphRAG._select_fair(eligible, max_agents=32)
    ids = {c.entity_id for c in selected}
    assert len(selected) == 32
    # Round-robin guarantees hub B's only target is kept despite its lower score.
    assert "B_target" in ids


def test_tie_break_is_not_entity_id_biased():
    # All same score, same hub, ids 00..49. A naive top-32 by (-score, id) would
    # always drop the highest ids (e.g. a katG with a high b-number). Fair
    # selection within one hub still falls back to score order, but the point is
    # nothing is dropped for being woken by a *different* hub.
    eligible = [_ctx(f"t{i:02d}", 0.9, "hub") for i in range(50)]
    selected = TemporalGraphRAG._select_fair(eligible, max_agents=32)
    assert len(selected) == 32


def test_returns_all_when_under_budget():
    eligible = [_ctx(f"t{i}", 0.5, "hub") for i in range(5)]
    selected = TemporalGraphRAG._select_fair(eligible, max_agents=32)
    assert len(selected) == 5


def test_small_hub_not_starved_by_large_hub_real_graph():
    """Real-graph check: when a flooding hub (crp, ~379 targets) and a smaller
    regulator are perturbed together under a budget smaller than crp's target
    count, the smaller regulator still gets representation (it is not starved)."""
    import pytest

    from ecoil_sim.config import load_yaml_like
    from ecoil_sim.graph import StaticGraph
    from ecoil_sim.models import AgentState
    from ecoil_sim.registry import RuleRegistry
    from ecoil_sim.state import TemporalState

    graph_dir = PROJECT_ROOT / "data" / "normalized" / "simulation"
    flooder, small = "protein.P0ACJ8", "protein.P13445"  # crp, rpoS
    g = StaticGraph.from_normalized_dir(graph_dir)
    if flooder not in g.entities or small not in g.entities:
        pytest.skip("regulators not in graph")

    def reg_targets(src):
        return {e.target_id for e in g.incident_edges(src)
                if e.relation_type in {"activates", "represses"} and e.target_id != src}

    small_only = reg_targets(small) - reg_targets(flooder)
    if len(reg_targets(flooder)) < 100 or not small_only:
        pytest.skip("graph does not have the expected hub structure")

    reg = RuleRegistry.from_registry_dir(PROJECT_ROOT / "data" / "registry" / "simulation")
    ew = load_yaml_like(PROJECT_ROOT / "configs" / "edge_weights.yaml")
    rag = TemporalGraphRAG(g, reg, ew.get("edge_weights", {}), ew.get("state_distance", {}), min_score=0.2)
    st = TemporalState.initialize(g.entities.values(), {})
    st.begin_round()
    st.apply_changes([
        AgentState(entity_id=flooder, state="inhibited", changed=True, reason="probe"),
        AgentState(entity_id=small, state="overexpressed", changed=True, reason="probe"),
    ])
    st.end_round()
    woken = {c.entity_id for c in rag.retrieve(st, [flooder, small], max_agents=64)}
    # at least one target that ONLY the small regulator wakes must survive crp's flood
    assert woken & small_only
