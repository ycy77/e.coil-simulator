"""Tests for the KG-validation and perturbation-benchmark logic (pure parts).

The scripts themselves run simulations / write reports; here we lock in the
parsing and the two-axis direction logic that the numbers depend on, without
running a full battery.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import importlib.util  # noqa: E402


def _load(script_name):
    path = PROJECT_ROOT / "scripts" / script_name
    spec = importlib.util.spec_from_file_location(script_name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bench = _load("benchmark_perturbation.py")
valkg = _load("validate_kg.py")


@dataclass
class _S:
    state: str = "expressed"
    efficiency: str = ""
    abundance_label: str = ""


def test_direction_folds_efficiency_axis():
    # gene repressed -> down
    assert bench.direction_of(_S(state="repressed")) == "down"
    # activator loss: still 'expressed' but efficiency low -> DOWN (the key case)
    assert bench.direction_of(_S(state="expressed", efficiency="low")) == "down"
    # overexpressed or high efficiency -> up
    assert bench.direction_of(_S(state="overexpressed")) == "up"
    assert bench.direction_of(_S(state="expressed", efficiency="high")) == "up"
    # plain expressed -> up
    assert bench.direction_of(_S(state="expressed")) == "up"
    # metabolite abundance
    assert bench.direction_of(_S(state="", abundance_label="low")) == "down"
    assert bench.direction_of(_S(state="", abundance_label="high")) == "up"
    assert bench.direction_of(None) == "none"


def test_state_signature_includes_efficiency():
    sig = bench.state_signature(_S(state="expressed", efficiency="low", abundance_label=""))
    assert sig == ("expressed", "low", "")
    # an efficiency-only change is detected as movement
    assert bench.state_signature(_S(state="expressed", efficiency="low")) != \
        bench.state_signature(_S(state="expressed", efficiency=""))


def test_gold_loader_parses_regulondb():
    gold_path = PROJECT_ROOT / "data" / "regulationDB" / "NetworkRegulatorGene.tsv"
    if not gold_path.exists():
        import pytest
        pytest.skip("RegulonDB gold standard not present")
    rows = valkg.load_gold(gold_path)
    assert len(rows) > 1000  # the network has thousands of interactions
    # The file mixes in a column-description line; the vast majority of rows are
    # real (regulator, target, +/-) interactions.
    signed = [r for r in rows if r[2] in ("+", "-")]
    assert len(signed) > 0.9 * len(rows)
    # benchmark's stricter loader keeps only +/- rows
    bench_rows = bench.load_gold(gold_path)
    assert all(s in ("+", "-") for _, _, s in bench_rows)
