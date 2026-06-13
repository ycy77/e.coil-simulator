"""Unit tests for the direction-conflict detector."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.llm import build_conflict_report, compute_signals  # noqa: E402
from ecoil_sim.llm.signal_direction import Signal  # noqa: E402
from ecoil_sim.models import Edge  # noqa: E402


def _state(state_obj, entity_id, state_value, abundance="medium"):
    state_obj.states[entity_id].state = state_value
    state_obj.states[entity_id].abundance_label = abundance


def test_single_repression_no_conflict():
    signals = [
        Signal(source="lacI", relation_type="represses", direction="up", source_state="inhibited"),
    ]
    report = build_conflict_report(signals)
    assert report.conflict is False
    assert report.axis_summary.get("up") == 1


def test_repression_release_vs_activation_loss_is_a_conflict():
    signals = [
        Signal(source="lacI", relation_type="represses", direction="up", source_state="inhibited"),
        Signal(source="CRP", relation_type="activates", direction="down", source_state="low"),
    ]
    report = build_conflict_report(signals)
    assert report.conflict is True
    assert "功能注释" in report.hint or "annotation" in report.hint


def test_two_activations_is_not_a_conflict():
    signals = [
        Signal(source="CRP", relation_type="activates", direction="up", source_state="high"),
        Signal(source="MalT", relation_type="activates", direction="up", source_state="medium"),
    ]
    report = build_conflict_report(signals)
    assert report.conflict is False
    assert "饱和" in report.hint or report.hint == ""


def test_abundance_conflict_detected():
    signals = [
        Signal(source="geneA", relation_type="encodes", direction="abundance_up", source_state="expressed"),
        Signal(source="geneB", relation_type="encodes", direction="abundance_down", source_state="repressed"),
    ]
    report = build_conflict_report(signals)
    assert report.conflict is True
    assert "丰度" in report.hint or "abundance" in report.hint


def test_state_and_abundance_axes_do_not_conflict():
    signals = [
        Signal(source="LacI", relation_type="represses", direction="up", source_state="inhibited"),
        Signal(source="geneA", relation_type="encodes", direction="abundance_up", source_state="expressed"),
    ]
    report = build_conflict_report(signals)
    assert report.conflict is False


def test_compute_signals_with_real_edges():
    from ecoil_sim.state import TemporalState
    from ecoil_sim.graph import StaticGraph

    graph = StaticGraph.from_normalized_dir()
    state = TemporalState.initialize(graph.entities.values())
    _state(state, "protein.P03023", "inhibited")  # LacI
    _state(state, "protein.P0ACJ8", "low", abundance="low")  # CRP
    _state(state, "gene.b0344", "repressed")  # lacZ (the candidate)
    edges = [
        Edge(
            source_id="protein.P03023",
            relation_type="represses",
            target_id="gene.b0344",
            direction="directed",
            evidence="test",
            source_database="test",
            source_record_id="",
        ),
        Edge(
            source_id="protein.P0ACJ8",
            relation_type="activates",
            target_id="gene.b0344",
            direction="directed",
            evidence="test",
            source_database="test",
            source_record_id="",
        ),
    ]
    signals = compute_signals(
        state,
        "gene.b0344",
        ["protein.P03023", "protein.P0ACJ8"],
        edges,
    )
    report = build_conflict_report(signals)
    directions = sorted(s.direction for s in signals)
    assert directions == ["down", "up"]
    assert report.conflict is True
    assert report.hint


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
    print("all signal_direction tests passed")
