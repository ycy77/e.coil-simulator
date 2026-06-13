"""Offline tests for the global-view LLM report agent (stubbed LLM)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.report.llm_report_agent import LLMReportAgent  # noqa: E402

SAMPLE_REPORT = {
    "rounds": 3,
    "changed_events": 4,
    "perturbation_sources": ["protein.P03023"],
    "events_by_round": {0: 1, 1: 3},
    "propagation_edges": [{"round": 1, "source": "protein.P03023", "target": "gene.b0344"}],
    "causal_chains": [["protein.P03023", "gene.b0344", "protein.P00722"]],
    "final_changed_states": {
        "gene.b0344": {"state": "expressed", "abundance_label": "", "round": 1},
        "protein.P00722": {"state": "active", "abundance_label": "high", "round": 2},
    },
    "response_pattern_match": {
        "matches": [
            {"pattern_id": "lac_operon_derepression_like", "similarity": 1.0,
             "matched": 3, "total": 3, "required_signals_present": True, "description": "L1"}
        ]
    },
}


def test_report_agent_passes_global_context_and_returns_text():
    captured = {}

    def complete(system, user, guided_json):
        captured["system"] = system
        captured["user"] = json.loads(user)
        captured["guided_json"] = guided_json
        return "## Perturbation\nLacI inhibited.\n"

    agent = LLMReportAgent(complete, prompt_path=PROJECT_ROOT / "prompts/report_agent.system.md")
    out = agent.write_report(SAMPLE_REPORT)

    assert "Perturbation" in out
    # The agent gets a GLOBAL view (not a single-entity local view).
    ctx = captured["user"]
    assert ctx["perturbation_sources"][0]["id"] == "protein.P03023"
    assert ctx["causal_chains"]
    assert ctx["final_changed_states"]
    assert ctx["phenotype_matches"][0]["pattern_id"] == "lac_operon_derepression_like"
    # Report is free text, so decoding is not schema-constrained.
    assert captured["guided_json"] is None


def test_report_agent_quiet_when_no_changes():
    def complete(system, user, guided_json):  # should not be called
        raise AssertionError("LLM must not be called when nothing changed")

    agent = LLMReportAgent(complete)
    out = agent.write_report({"changed_events": 0})
    assert "No changes" in out
