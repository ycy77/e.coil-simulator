"""Tests for the DE-grounded benchmark's pure logic (no sim run, no LLM)."""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))  # benchmark_expression imports benchmark_perturbation


def _load(name):
    path = PROJECT_ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


be = _load("benchmark_expression.py")


@dataclass
class _AS:
    state: str = "expressed"
    efficiency: str = ""
    abundance_label: str = ""


def test_measured_direction():
    assert be.measured_direction(2.0) == "up"
    assert be.measured_direction(-1.5) == "down"


def test_load_de_table(tmp_path):
    f = tmp_path / "de.tsv"
    f.write_text("perturbation_id\tgene\tlog2fc\tpadj\n"
                 "delta_fnr\tb1234\t-2.1\t1e-8\n"
                 "delta_fnr\tB5678\t3.0\t0.001\n"
                 "delta_crp\tb1111\t0.2\t0.9\n", encoding="utf-8")
    de = be.load_de_table(f)
    assert set(de) == {"delta_fnr", "delta_crp"}
    assert de["delta_fnr"]["b1234"] == (-2.1, 1e-8)
    assert de["delta_fnr"]["b5678"][0] == 3.0   # gene key lowercased


def test_conflict_genes_detects_opposing_regulators():
    edges = [
        SimpleNamespace(relation_type="activates", source_id="protein.A", target_id="gene.x"),
        SimpleNamespace(relation_type="represses", source_id="protein.B", target_id="gene.x"),  # x: conflict
        SimpleNamespace(relation_type="activates", source_id="protein.A", target_id="gene.y"),  # y: only activated
    ]
    g = SimpleNamespace(edges=edges)
    cg = be.conflict_genes(g)
    assert cg == {"gene.x"}


def test_score_against_de_overall_and_conflict_split():
    # measured: gx up (significant), gy down (significant), gz up but not significant
    de_for_pert = {"gx": (2.0, 1e-5), "gy": (-2.0, 1e-5), "gz": (3.0, 0.5)}
    final_states = {
        "gene.gx": _AS(state="expressed", efficiency="high"),   # predicted up  -> matches up
        "gene.gy": _AS(state="repressed"),                       # predicted down -> matches down
    }
    idx = {"gx": {"gene.gx"}, "gy": {"gene.gy"}, "gz": {"gene.gz"}}
    conflict = {"gene.gx"}  # gx is a conflict gene
    overall, conf = be.score_against_de(None, final_states, de_for_pert, idx,
                                        lfc_thr=1.0, padj_thr=0.05, conflict_set=conflict)
    assert overall == [2, 2]      # gx, gy both correct; gz excluded (not significant)
    assert conf == [1, 1]         # only gx is in the conflict subset


def test_score_skips_unmoved_genes():
    de_for_pert = {"gx": (2.0, 1e-5)}
    final_states = {"gene.gx": _AS(state="expressed", efficiency="")}  # direction_of -> 'up'? expressed default
    # 'expressed' with no efficiency counts as 'up' per direction_of; use a truly-neutral case:
    final_states_neutral = {"gene.gx": _AS(state="unknown", efficiency="", abundance_label="")}
    idx = {"gx": {"gene.gx"}}
    overall, _ = be.score_against_de(None, final_states_neutral, de_for_pert, idx, 1.0, 0.05, set())
    assert overall == [0, 0]      # gene didn't move -> not scored as a direction call
