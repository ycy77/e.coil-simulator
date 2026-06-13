"""Unit tests for ``ecoil_sim.rules.fallback_policy`` and the deterministic
fallback path in :class:`ecoil_sim.actions.ActionInterpreter`."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.actions import ActionInterpreter  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.models import AgentState  # noqa: E402
from ecoil_sim.retrieval import RetrievedContext  # noqa: E402
from ecoil_sim.rules import FallbackPolicy  # noqa: E402
from ecoil_sim.state import TemporalState  # noqa: E402


def _build_state(graph, **overrides):
    state = TemporalState.initialize(graph.entities.values())
    for entity_id, spec in overrides.items():
        agent = state.states[entity_id]
        new = AgentState(
            entity_id=entity_id,
            state=spec.get("state", agent.state),
            abundance_label=spec.get("abundance_label", agent.abundance_label),
            changed=True,
            reason="test override",
        )
        state.apply_changes([new], reason_prefix="test")
    return state


def _retrieve_context(entity_id, edges, rules=None, changed_neighbors=None):
    return RetrievedContext(
        entity_id=entity_id,
        score=1.0,
        edges=edges,
        rules=rules or [],
        changed_neighbors=changed_neighbors or [],
    )


def test_empty_policy_disables_fallback():
    policy = FallbackPolicy.empty()
    assert policy.enabled is False
    assert policy.match("represses") is None


def test_represses_fallback_inhibits_target_when_source_active():
    from ecoil_sim.models import Edge, Rule

    graph = StaticGraph.from_normalized_dir()
    target_id = "gene.b0342"
    source_id = "protein.P03023"
    edge = Edge(
        source_id=source_id,
        relation_type="represses",
        target_id=target_id,
        direction="directed",
        evidence="test",
        source_database="test",
        source_record_id="",
    )
    rule = Rule(
        rule_id="r.rep.1",
        priority_class="native",
        rule_type="transcription_regulation",
        source={},
        species_scope="Escherichia coli K-12 MG1655",
        participants={"source_id": source_id, "target_id": target_id, "relation_type": "represses"},
        conditions={},
        effects=[],
        constraints={},
        confidence="high",
    )
    policy = FallbackPolicy.from_config(PROJECT_ROOT / "configs/fallback_rules.yaml")
    interpreter = ActionInterpreter(graph, fallback_policy=policy)
    state = _build_state(
        graph,
        **{source_id: {"state": "active"}},
    )
    ctx = _retrieve_context(target_id, [edge], rules=[rule], changed_neighbors=[source_id])
    fallback = interpreter._fallback_action(state, ctx)
    assert fallback is not None
    assert fallback["action_type"] == "change_activity"
    assert fallback["direction"] == "down"


def test_encodes_fallback_changes_protein_abundance():
    from ecoil_sim.models import Edge, Rule

    graph = StaticGraph.from_normalized_dir()
    gene_id = "gene.b0344"
    protein_id = "protein.P00722"
    edge = Edge(
        source_id=gene_id,
        relation_type="encodes",
        target_id=protein_id,
        direction="directed",
        evidence="test",
        source_database="test",
        source_record_id="",
    )
    rule = Rule(
        rule_id="r.enc.1",
        priority_class="native",
        rule_type="translation_effect",
        source={},
        species_scope="Escherichia coli K-12 MG1655",
        participants={"source_id": gene_id, "target_id": protein_id, "relation_type": "encodes"},
        conditions={},
        effects=[],
        constraints={},
        confidence="high",
    )
    policy = FallbackPolicy.from_config(PROJECT_ROOT / "configs/fallback_rules.yaml")
    interpreter = ActionInterpreter(graph, fallback_policy=policy)
    state = _build_state(graph, **{gene_id: {"state": "repressed"}})
    ctx = _retrieve_context(protein_id, [edge], rules=[rule], changed_neighbors=[gene_id])
    fallback = interpreter._fallback_action(state, ctx)
    assert fallback is not None
    assert fallback["action_type"] == "change_abundance"
    assert fallback["direction"] == "down"


def test_fallback_disabled_returns_none():
    from ecoil_sim.models import Edge, Rule

    graph = StaticGraph.from_normalized_dir()
    target_id = "gene.b0342"
    source_id = "protein.P03023"
    edge = Edge(
        source_id=source_id,
        relation_type="represses",
        target_id=target_id,
        direction="directed",
        evidence="test",
        source_database="test",
        source_record_id="",
    )
    rule = Rule(
        rule_id="r.rep.1",
        priority_class="native",
        rule_type="transcription_regulation",
        source={},
        species_scope="Escherichia coli K-12 MG1655",
        participants={"source_id": source_id, "target_id": target_id, "relation_type": "represses"},
        conditions={},
        effects=[],
        constraints={},
        confidence="high",
    )
    interpreter = ActionInterpreter(graph, fallback_policy=FallbackPolicy.empty())
    state = _build_state(graph, **{source_id: {"state": "active"}})
    ctx = _retrieve_context(target_id, [edge], rules=[rule], changed_neighbors=[source_id])
    assert interpreter._fallback_action(state, ctx) is None


if __name__ == "__main__":
    failures = []
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok    {name}")
            except AssertionError as exc:
                failures.append((name, str(exc)))
                print(f"  FAIL  {name}: {exc}")
    if failures:
        raise SystemExit(1)
    print("all fallback_policy tests passed")
