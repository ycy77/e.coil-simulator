"""Offline tests for the co-expression validation helpers (pearson + loader).

Real numbers come from running validate_coexpression.py on the fetched Tjaden
2023 compendium; here we lock in the math and the matrix loader on a synthetic
matrix with known structure.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def _load_script(name):
    path = PROJECT_ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


vc = _load_script("validate_coexpression.py")


def test_pearson_basic():
    assert vc.pearson([1, 2, 3, 4], [2, 4, 6, 8]) == 1.0
    assert vc.pearson([1, 2, 3, 4], [8, 6, 4, 2]) == -1.0
    assert abs(vc.pearson([1, 2, 3, 4], [1, 2, 3, 4])) == 1.0
    assert vc.pearson([1, 1, 1], [1, 2, 3]) is None  # zero variance
    assert vc.pearson([1], [1]) is None  # too few points


def test_load_matrix_rows_orientation(tmp_path):
    # genes as rows: col0 = gene id, rest = samples
    f = tmp_path / "expr.tsv"
    f.write_text("gene\ts1\ts2\ts3\nlacz\t10\t20\t30\nlaci\t30\t20\t10\n", encoding="utf-8")
    expr = vc.load_matrix(f, orient="rows", log=False)
    assert set(expr) == {"lacz", "laci"}
    assert expr["lacz"] == [10.0, 20.0, 30.0]
    # positively/negatively correlated by construction
    assert vc.pearson(expr["lacz"], expr["laci"]) == -1.0


def test_load_matrix_cols_orientation(tmp_path):
    # genes as columns: header = gene ids, rows = samples
    f = tmp_path / "expr.tsv"
    f.write_text("sample\tlacz\tlaci\ns1\t10\t30\ns2\t20\t20\ns3\t30\t10\n", encoding="utf-8")
    expr = vc.load_matrix(f, orient="cols", log=False)
    assert expr["lacz"] == [10.0, 20.0, 30.0]
    assert expr["laci"] == [30.0, 20.0, 10.0]


def test_load_matrix_wanted_keys_filters(tmp_path):
    f = tmp_path / "expr.tsv"
    f.write_text("gene\ts1\ts2\nlacz\t1\t2\nlaci\t3\t4\ncrp\t5\t6\n", encoding="utf-8")
    expr = vc.load_matrix(f, orient="rows", log=False, wanted_keys={"lacz", "crp"})
    assert set(expr) == {"lacz", "crp"}


def test_log_transform_applied(tmp_path):
    import math
    f = tmp_path / "expr.tsv"
    f.write_text("gene\ts1\ts2\nlacz\t0\t99\n", encoding="utf-8")
    expr = vc.load_matrix(f, orient="rows", log=True)
    assert expr["lacz"][0] == 0.0  # log1p(0)
    assert abs(expr["lacz"][1] - math.log1p(99)) < 1e-9
