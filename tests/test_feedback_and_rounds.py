"""Tests for feedback-loop detection and per-round reporting (this session's additions)."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.report.reporter import Reporter  # noqa: E402
from ecoil_sim.report.llm_report_agent import LLMReportAgent  # noqa: E402


def test_feedback_closure_on_source():
    # P (perturbed in round 0) is re-changed in round 2 -> loop closed on origin.
    events = [
        {"entity_id": "protein.P", "round": 0, "changed": True},
        {"entity_id": "gene.A", "round": 1, "changed": True},
        {"entity_id": "protein.P", "round": 2, "changed": True},
    ]
    fb = Reporter._feedback_events(events, perturbation_sources=["protein.P"])
    assert fb["has_feedback"] is True
    assert any(x["entity_id"] == "protein.P" for x in fb["closed_on_source"])
    assert any(x["entity_id"] == "protein.P" and x["rounds"] == [0, 2] for x in fb["reactivations"])


def test_no_feedback_when_linear():
    events = [
        {"entity_id": "protein.P", "round": 0, "changed": True},
        {"entity_id": "gene.A", "round": 1, "changed": True},
        {"entity_id": "gene.B", "round": 2, "changed": True},
    ]
    fb = Reporter._feedback_events(events, perturbation_sources=["protein.P"])
    assert fb["has_feedback"] is False
    assert fb["closed_on_source"] == []


def test_per_round_summaries_flags_feedback():
    reporter = Reporter(graph=None, phenotype_db=None, name_resolver=None)
    summary = {
        "perturbation_sources": ["protein.P"],
        "events": [
            {"entity_id": "protein.P", "round": 0, "state": "inhibited"},
            {"entity_id": "gene.A", "round": 1, "state": "expressed"},
            {"entity_id": "protein.P", "round": 2, "state": "active"},
        ],
        "propagation_edges": [
            {"round": 1, "source": "protein.P", "target": "gene.A"},
            {"round": 2, "source": "gene.A", "target": "protein.P"},
        ],
    }
    rounds = reporter.per_round_summaries(summary)
    by_round = {r["round"]: r for r in rounds}
    assert by_round[1]["feedback_closure"] == []          # round 1 doesn't touch a source
    assert by_round[2]["feedback_closure"] == ["protein.P"]  # round 2 loops back to origin


def test_write_round_report_uses_stub_llm():
    captured = {}

    def complete(system, user, guided_json):
        import json
        captured["ctx"] = json.loads(user)
        return "Round 2: the cascade fed back onto LacI."

    agent = LLMReportAgent(complete)  # no graph -> names fall back to ids
    out = agent.write_round_report({
        "round": 2,
        "changes": [{"entity_id": "protein.P", "state": "active", "reason": "feedback"}],
        "propagation_edges": [{"round": 2, "source": "gene.A", "target": "protein.P"}],
        "feedback_closure": ["protein.P"],
    })
    assert "fed back" in out
    assert captured["ctx"]["feedback_closure"] == ["protein.P"]
    # empty round short-circuits without calling the LLM
    assert "no changes" in agent.write_round_report({"round": 3, "changes": []}).lower()
