"""Retrieval-level test for STRING PPI propagation on the simulation baseline.

The curated baseline integrates ~26k STRING protein-protein interaction edges
(``interacts``). These carry no deterministic direction, so they must still
*wake* a perturbed protein's interaction partners (handing the decision to the
LLM) with a retrieval score modulated by the per-edge STRING confidence.

This guards the engine<->graph relation reconciliation: if ``interacts`` ever
loses its retrieval weight again, PPI partners stop waking and this fails.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.config import load_yaml_like  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.models import AgentState  # noqa: E402
from ecoil_sim.registry import RuleRegistry  # noqa: E402
from ecoil_sim.retrieval import TemporalGraphRAG  # noqa: E402
from ecoil_sim.state import TemporalState  # noqa: E402

BASELINE = PROJECT_ROOT / "data" / "normalized" / "simulation"
REGISTRY = PROJECT_ROOT / "data" / "registry" / "simulation"


@pytest.fixture(scope="module")
def retriever_and_graph():
    if not (BASELINE / "edges.csv").exists():
        pytest.skip("simulation baseline not built")
    graph = StaticGraph.from_normalized_dir(BASELINE)
    registry = RuleRegistry.from_registry_dir(REGISTRY)
    edge_cfg = load_yaml_like(PROJECT_ROOT / "configs" / "edge_weights.yaml")
    rag = TemporalGraphRAG(
        graph=graph,
        registry=registry,
        edge_weights=edge_cfg.get("edge_weights", {}),
        state_distance=edge_cfg.get("state_distance", {}),
        min_score=0.2,
    )
    return rag, graph


def _ppi_hub(graph: StaticGraph) -> str:
    counts: dict[str, int] = {}
    for edge in graph.edges:
        if edge.relation_type == "interacts":
            counts[edge.source_id] = counts.get(edge.source_id, 0) + 1
            counts[edge.target_id] = counts.get(edge.target_id, 0) + 1
    if not counts:
        pytest.skip("no interacts edges in baseline")
    return max(counts, key=counts.get)


def test_ppi_partners_are_woken(retriever_and_graph):
    rag, graph = retriever_and_graph
    hub = _ppi_hub(graph)

    state = TemporalState.initialize(graph.entities.values(), {})
    state.begin_round()
    state.apply_changes([AgentState(entity_id=hub, state="inhibited", changed=True, reason="probe")])
    state.end_round()

    contexts = rag.retrieve(state, [hub], max_agents=50)
    assert contexts, "perturbing a PPI hub should wake neighbours"

    via_ppi = [c for c in contexts if any(e.relation_type == "interacts" for e in c.edges)]
    assert via_ppi, "interacts edges must wake PPI partners (STRING network is live)"

    # Scores are sorted descending and strictly positive (signal propagates).
    scores = [c.score for c in contexts]
    assert scores == sorted(scores, reverse=True)
    assert all(s > 0 for s in scores)


def test_string_confidence_modulates_score(retriever_and_graph):
    """A higher per-edge STRING confidence yields a higher retrieval score."""
    rag, graph = retriever_and_graph
    hub = _ppi_hub(graph)

    # Find two single-edge PPI partners of the hub with different confidences.
    partners = {}
    for edge in graph.incident_edges(hub):
        if edge.relation_type != "interacts":
            continue
        other = edge.target_id if edge.source_id == hub else edge.source_id
        partners.setdefault(other, edge.edge_weight)

    confidences = sorted(set(partners.values()))
    if len(confidences) < 2:
        pytest.skip("baseline hub lacks PPI edges of differing confidence")

    state = TemporalState.initialize(graph.entities.values(), {})
    state.begin_round()
    state.apply_changes([AgentState(entity_id=hub, state="inhibited", changed=True, reason="probe")])
    state.end_round()

    scored = {c.entity_id: c.score for c in rag.retrieve(state, [hub], max_agents=4096)}
    low_partner = next(p for p, w in partners.items() if w == confidences[0] and p in scored)
    high_partner = next(p for p, w in partners.items() if w == confidences[-1] and p in scored)
    assert scored[high_partner] > scored[low_partner]
