"""Tests for the scorer's efficiency axis and per-pattern initial_overrides merge.

These back the literature battery: activator-driven genes are scored on the
efficiency axis (two-axis model), and a pattern's resting-state overrides merge
onto the base initial profile.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def _load(name):
    path = PROJECT_ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sp = _load("score_phenotypes.py")


@dataclass
class _AS:
    state: str = "expressed"
    abundance_label: str = ""
    efficiency: str = ""


class _State:
    def __init__(self, states):
        self.states = states
        self.history = {}


def test_efficiency_axis_scored():
    spec = {"signal_level": "L2", "expected_efficiency": {"gene.x": "high"}}
    st = _State({"gene.x": _AS(state="expressed", efficiency="high")})
    res = sp.score_run(spec, st)
    assert res["efficiency_acc"] == 1.0
    assert res["pattern_score"] == 1.0
    # wrong efficiency -> miss
    st2 = _State({"gene.x": _AS(state="expressed", efficiency="")})
    assert sp.score_run(spec, st2)["pattern_score"] == 0.0


def test_mixed_state_and_efficiency_axes():
    spec = {"signal_level": "L2",
            "expected_states": {"gene.a": "repressed"},
            "expected_efficiency": {"gene.b": "high"}}
    st = _State({"gene.a": _AS(state="repressed"), "gene.b": _AS(state="expressed", efficiency="high")})
    res = sp.score_run(spec, st)
    assert res["pattern_score"] == 1.0  # 2/2 across two axes


def test_effective_profile_merges_overrides():
    deps = {"initial_profile": {"profile_id": "base", "overrides": {"gene.keep": {"state": "expressed"}}}}
    spec = {"initial_overrides": {"gene.x": "repressed", "gene.y": {"state": "inhibited"}}}
    prof = sp.effective_profile(deps, spec)
    ov = prof["overrides"]
    assert ov["gene.keep"] == {"state": "expressed"}        # base preserved
    assert ov["gene.x"] == {"state": "repressed"}            # scalar lifted to dict
    assert ov["gene.y"] == {"state": "inhibited"}
    # no overrides -> base profile returned unchanged
    assert sp.effective_profile(deps, {}) is deps["initial_profile"]
