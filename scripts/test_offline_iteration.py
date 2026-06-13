#!/usr/bin/env python3
"""Offline regression test for the lac operon propagation chain.

This test seeds LacI in its active form, runs three rounds, and verifies
the deterministic fallback propagates correctly across the new state
model where genes and proteins use independent axes:

* gene.b0342/b0343/b0344 should become ``repressed`` (LacI represses them)
* protein.P00722/P02920/P07464 should drop to ``abundance_label=low``
  while keeping their default ``active`` state — abundance and activity
  are tracked as separate axes.

The script also exercises the new :class:`NameResolver` and
:class:`FallbackPolicy` end-to-end, so it is a strong smoke test.
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.actions import ActionInterpreter
from ecoil_sim.agents import PromptBuilder
from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm import NameResolver, RuleBasedMockLLM
from ecoil_sim.paths import PROJECT_ROOT
from ecoil_sim.registry import RuleRegistry
from ecoil_sim.retrieval import TemporalGraphRAG
from ecoil_sim.rules import FallbackPolicy
from ecoil_sim.sim.engine import SimulationEngine, run_sync
from ecoil_sim.sim.enriched_service import EnrichedService
from ecoil_sim.storage import SimulationStore
from ecoil_sim.validation import ActionValidator


def main() -> int:
    graph = StaticGraph.from_normalized_dir()
    registry = RuleRegistry.from_registry_dir()
    edge_config = load_yaml_like(PROJECT_ROOT / "configs/edge_weights.yaml")
    weights = edge_config.get("edge_weights", {})
    retriever = TemporalGraphRAG(
        graph=graph,
        registry=registry,
        edge_weights=weights,
        state_distance=edge_config.get("state_distance", {}),
        min_score=0.2,
    )
    prompt_builder = PromptBuilder(PROJECT_ROOT / "prompts/agent_decision.system.md")
    name_resolver = NameResolver(graph.entities.values())
    fallback_policy = FallbackPolicy.from_config(PROJECT_ROOT / "configs/fallback_rules.yaml")
    validator = ActionValidator(name_resolver=name_resolver)
    action_interpreter = ActionInterpreter(graph, fallback_policy=fallback_policy)
    store = SimulationStore(PROJECT_ROOT / "runs" / "_offline_iteration_test")
    enriched_service = EnrichedService(PROJECT_ROOT / "data" / "enriched" / "entities_enriched_lite.jsonl")
    enriched_service.load()
    engine = SimulationEngine(
        graph=graph,
        registry=registry,
        retriever=retriever,
        prompt_builder=prompt_builder,
        store=store,
        llm_client=RuleBasedMockLLM(),
        name_resolver=name_resolver,
        action_interpreter=action_interpreter,
        validator=validator,
        enriched_service=enriched_service,
    )
    state = run_sync(
        engine,
        perturbations=[{"entity_id": "protein.P03023", "state": "active", "reason": "offline iteration test"}],
        max_rounds=3,
        max_active_agents=32,
        steady_state_patience=2,
    )

    expected_gene_states = {
        "gene.b0342": "repressed",
        "gene.b0343": "repressed",
        "gene.b0344": "repressed",
    }
    expected_protein_abundance = {
        "protein.P00722": "low",
        "protein.P02920": "low",
        "protein.P07464": "low",
    }
    failures = []
    for entity_id, wanted in expected_gene_states.items():
        got = state.states[entity_id].state
        if got != wanted:
            failures.append(f"{entity_id}: expected state={wanted}, got {got}")
    for entity_id, wanted in expected_protein_abundance.items():
        got = state.states[entity_id].abundance_label
        if got != wanted:
            failures.append(f"{entity_id}: expected abundance={wanted}, got {got}")

    if failures:
        print("FAILED")
        for failure in failures:
            print(failure)
        return 1
    print("offline iteration ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
