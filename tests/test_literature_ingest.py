"""Tests for the literature-edge ingest integrity rules (evidence gating + overlay shape).

Locks the enforced rules so they can't silently regress:
- only direct + peer-reviewed + K-12 is an eligible hard edge (rule 3);
- the overlay is tagged source_database=Literature (rule 1, separate accounting).
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def _load(name):
    path = PROJECT_ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ingest = _load("ingest_literature_edges.py")


def test_evidence_gating_enforced():
    ok = {"evidence_tier": "direct", "peer_reviewed": True, "strain": "K-12"}
    assert ingest.is_eligible_hard_edge(ok) is True
    # preprint -> not a hard edge
    assert ingest.is_eligible_hard_edge({**ok, "peer_reviewed": False}) is False
    # review / omics tier -> not a hard edge
    assert ingest.is_eligible_hard_edge({**ok, "evidence_tier": "review"}) is False
    assert ingest.is_eligible_hard_edge({**ok, "evidence_tier": "omics"}) is False
    # non-K-12 -> not a hard edge
    assert ingest.is_eligible_hard_edge({**ok, "strain": "ATCC-25922"}) is False
    assert ingest.is_eligible_hard_edge({**ok, "strain": "EHEC"}) is False


def test_overlay_is_tagged_literature_if_present():
    overlay = PROJECT_ROOT / "data" / "literature" / "literature_edges.overlay.csv"
    if not overlay.exists():
        import pytest
        pytest.skip("overlay not generated")
    with overlay.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert rows, "overlay should not be empty"
    # rule 1: every overlay edge is tagged Literature with a DOI, so KG-recall
    # validation (which reads edges.csv) never counts them.
    for r in rows:
        assert r["source_database"] == "Literature"
        assert r["source_record_id"], "literature edge must carry its DOI"
        assert r["source_id"].startswith(("protein.", "gene.", "complex.", "rna.", "molecule."))
        assert r["target_id"].startswith(("gene.", "protein."))


def test_lit_edges_file_parses_and_has_tiers():
    rows = ingest.load_lit(PROJECT_ROOT / "data" / "literature" / "regulatory_edges.jsonl")
    assert len(rows) >= 10
    for r in rows:
        assert r.get("relation") in ("activates", "represses")
        assert "evidence_tier" in r and "peer_reviewed" in r and "strain" in r
        assert r.get("doi") or r.get("pmid")
