"""End-to-end integration test for the simulation engine.

Unlike the other tests (which exercise individual parsers/validators), this
loads the real canonical graph + initial-condition profile and runs the full
per-round loop with the deterministic ``RuleBasedMockLLM``. It locks in the
canonical biology the simulator must reproduce: under glucose log phase the lac
operon starts repressed; inhibiting the repressor LacI derepresses the lacZYA
structural genes one round later, and their proteins then accumulate.

This mirrors how ``main.py`` wires the engine (same normalized dir + initial
profile as ``configs/simulation.yaml``). Kept deterministic (mock LLM, no
network) so it runs in CI without vLLM.
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

# Canonical lac operon ids in the normalized graph.
LACI_PROTEIN = "protein.P03023"
LACZYA_GENES = ["gene.b0344", "gene.b0343", "gene.b0342"]  # lacZ, lacY, lacA
LACZYA_PROTEINS = ["protein.P00722", "protein.P02920", "protein.P07464"]

# Match configs/simulation.yaml: the engine runs on the curated simulation
# baseline (STRING-integrated, endogenous-only) seeded by the glucose-log-phase
# initial profile.
NORMALIZED_DIR = PROJECT_ROOT / "data" / "normalized" / "simulation"
REGISTRY_DIR = PROJECT_ROOT / "data" / "registry" / "simulation"
INITIAL_PROFILE = PROJECT_ROOT / "data" / "initial_conditions" / "glucose_log_phase.yaml"


@pytest.fixture(scope="module")
def graph() -> StaticGraph:
    g = StaticGraph.from_normalized_dir(NORMALIZED_DIR)
    if LACI_PROTEIN not in g.entities:
        pytest.skip(f"{LACI_PROTEIN} not present in normalized graph")
    return g


@pytest.fixture(scope="module")
def profile() -> dict:
    return load_yaml_like(INITIAL_PROFILE) if INITIAL_PROFILE.exists() else {}


def _build_engine(graph: StaticGraph, store_root: Path) -> SimulationEngine:
    registry = RuleRegistry.from_registry_dir(REGISTRY_DIR)
    edge_cfg = load_yaml_like(PROJECT_ROOT / "configs" / "edge_weights.yaml")
    retriever = TemporalGraphRAG(
        graph=graph,
        registry=registry,
        edge_weights=edge_cfg.get("edge_weights", {}),
        state_distance=edge_cfg.get("state_distance", {}),
        min_score=0.2,
    )
    name_resolver = NameResolver(graph.entities.values())
    fallback = FallbackPolicy.from_config(PROJECT_ROOT / "configs" / "fallback_rules.yaml")
    return SimulationEngine(
        graph=graph,
        registry=registry,
        retriever=retriever,
        prompt_builder=PromptBuilder(PROJECT_ROOT / "prompts" / "agent_decision.system.md"),
        store=SimulationStore(store_root),
        llm_client=RuleBasedMockLLM(),
        name_resolver=name_resolver,
        action_interpreter=ActionInterpreter(graph, fallback_policy=fallback),
        validator=ActionValidator(name_resolver=name_resolver),
    )


def _first_change_round(history: list) -> int | None:
    for item in history:
        if item.get("changed"):
            return item["round"]
    return None


def test_lac_operon_derepression(graph: StaticGraph, profile: dict, tmp_path: Path):
    engine = _build_engine(graph, tmp_path / "run")
    perturbations = [
        {
            "entity_id": LACI_PROTEIN,
            "state": "inhibited",
            "source": "database",
            "input_source": "test",
            "reason": "inhibit lac repressor",
        }
    ]
    state = run_sync(
        engine,
        perturbations=perturbations,
        max_rounds=4,
        max_active_agents=64,
        initial_profile=profile,
    )

    # The perturbation holds.
    assert state.states[LACI_PROTEIN].state == "inhibited"

    # Genes start repressed (glucose log phase) and derepress one round later.
    for gene_id in LACZYA_GENES:
        history = state.history[gene_id]
        assert history[0]["state"] == "repressed", f"{gene_id} should start repressed"
        assert state.states[gene_id].state == "expressed", (
            f"{gene_id} expected 'expressed', got '{state.states[gene_id].state}'"
        )
        # Causal, not instantaneous: the change lands after the perturbation round.
        assert _first_change_round(history) == 1, f"{gene_id} should change in round 1"

    # The encoded proteins then accumulate (active / high abundance).
    for protein_id in LACZYA_PROTEINS:
        observed = state.states.get(protein_id)
        assert observed is not None, f"{protein_id} missing from final state"
        assert observed.state == "active", f"{protein_id} expected active, got {observed.state}"


def test_no_perturbation_is_quiet(graph: StaticGraph, profile: dict, tmp_path: Path):
    """Negative control: with no perturbation, nothing should change."""
    engine = _build_engine(graph, tmp_path / "run")
    state = run_sync(
        engine,
        perturbations=[],
        max_rounds=3,
        max_active_agents=64,
        initial_profile=profile,
    )
    changed = [
        entity_id
        for entity_id, history in state.history.items()
        if any(item.get("changed") for item in history)
    ]
    assert changed == [], f"expected no changes without a perturbation, got {changed[:10]}"
