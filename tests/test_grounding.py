"""Offline tests for entity grounding and the LLM perturbation parser.

The grounder runs against the real graph (no LLM). The parser is exercised with
a stub ``complete`` so the orchestration and deterministic guards are tested
without the vLLM endpoint.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.sim.grounding import EntityGrounder  # noqa: E402
from ecoil_sim.sim.llm_perturbation import LLMPerturbationParser  # noqa: E402

GRAPH_DIR = PROJECT_ROOT / "data" / "normalized" / "simulation"
PROMPTS_DIR = PROJECT_ROOT / "prompts"


@pytest.fixture(scope="module")
def graph() -> StaticGraph:
    return StaticGraph.from_normalized_dir(GRAPH_DIR)


@pytest.fixture(scope="module")
def grounder(graph: StaticGraph) -> EntityGrounder:
    return EntityGrounder(graph.entities.values())


def test_name_match_beats_annotation_mention(graph, grounder):
    # "recA" must ground to the recA entity itself, not to recB/recC whose
    # annotations merely cite recA.
    best = grounder.best("recA")
    assert best is not None
    assert best.name.lower() == "reca"
    assert best.matched_via in {"name_exact", "alias_exact", "alias_word", "name_word"}


def test_concept_grounds_via_annotation(grounder):
    # A drug's target concept grounds through the target's annotation.
    gyrase = {c.name for c in grounder.candidates("DNA gyrase", limit=5)}
    assert "gyrA" in gyrase or "gyrB" in gyrase

    pbps = {c.name for c in grounder.candidates("penicillin-binding protein", limit=8)}
    assert pbps & {"mrcA", "mrcB", "dacC"}


def test_unknown_mention_returns_nothing(grounder):
    assert grounder.candidates("definitely-not-an-ecoli-entity-xyz") == []


# --- parser orchestration with a stubbed LLM ------------------------------- #
def _make_parser(graph, grounder, intents, resolution):
    """Build a parser whose injected LLM returns canned JSON for each stage."""
    import json

    def complete(system, user, guided_json):
        # First call (intent extraction) sees the raw request; second call
        # (resolution) sees a JSON object containing "candidates".
        if '"candidates"' in user:
            return json.dumps(resolution)
        return json.dumps(intents)

    return LLMPerturbationParser(graph, grounder, complete, prompts_dir=PROMPTS_DIR)


def test_parser_grounds_and_builds_engine_changes(graph, grounder):
    recA = grounder.best("recA")
    assert recA is not None
    intents = {"intents": [{"mention": "knock out recA", "kind": "knockout"}]}
    resolution = {
        "perturbations": [
            {
                "entity_id": recA.entity_id,
                "target_state": "knocked_out" if "knocked_out" in recA.allowed_states else recA.allowed_states[0],
                "agent_mention": "knock out recA",
                "agent_kind": "endogenous",
                "evidence": "recA annotation",
                "confidence": 0.95,
                "reason": "direct knockout",
            }
        ],
        "unresolved": [],
    }
    parser = _make_parser(graph, grounder, intents, resolution)
    proposal = parser.parse_text("knock out recA")
    assert len(proposal.perturbations) == 1
    change = proposal.to_engine_changes()[0]
    assert change["entity_id"] == recA.entity_id
    assert change["input_source"] == "llm_perturbation"


def test_validate_rejects_bad_state_and_unknown_id(graph, grounder):
    recA = grounder.best("recA")
    intents = {"intents": [{"mention": "x", "kind": "knockout"}]}
    resolution = {
        "perturbations": [
            # invalid state for a real entity -> must be moved to unresolved
            {"entity_id": recA.entity_id, "target_state": "made_up_state",
             "agent_mention": "x", "agent_kind": "endogenous", "confidence": 0.5, "reason": ""},
            # nonexistent id -> must be moved to unresolved
            {"entity_id": "protein.DOES_NOT_EXIST", "target_state": "inhibited",
             "agent_mention": "y", "agent_kind": "endogenous", "confidence": 0.5, "reason": ""},
        ],
        "unresolved": [],
    }
    parser = _make_parser(graph, grounder, intents, resolution)
    proposal = parser.parse_text("...")
    assert proposal.perturbations == []
    assert len(proposal.unresolved) == 2
