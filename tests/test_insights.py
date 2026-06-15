"""Regression tests for the diagnostic-UI insight readers.

These cover the parse logic and the graceful-degradation contract; they do
not require the FastAPI app, vLLM, or the real data files.
"""
from pathlib import Path

from web.backend import insights


class _Edge:
    def __init__(self, s, r, t):
        self.source_id, self.relation_type, self.target_id = s, r, t


class _Entity:
    def __init__(self, name):
        self.name = name
        self.display_name = name


class _Loader:
    def __init__(self, edges, entities):
        self._edges = edges
        self._entities = entities


def test_literature_overview_missing(tmp_path):
    out = insights.literature_overview(tmp_path, loader=None)
    assert out["available"] is False
    assert out["edges"] == []


def test_literature_overview_overlap(tmp_path):
    lit = tmp_path / "data" / "literature"
    lit.mkdir(parents=True)
    (lit / "literature_edges.overlay.csv").write_text(
        "source_id,relation_type,target_id,direction,evidence,source_database,source_record_id,notes,edge_weight,string_channel\n"
        "protein.A,represses,gene.B,directed,literature_direct,Literature,10.1/x,note one,,\n"
        "protein.C,activates,gene.D,directed,literature_direct,Literature,10.1/y,note two,,\n"
        "protein.E,represses,gene.UNRESOLVED,directed,literature_direct,Literature,10.1/z,note three,,\n",
        encoding="utf-8",
    )
    # The first edge already exists in the base graph; C->D is novel; E->? has
    # an endpoint missing from the entity table.
    loader = _Loader(
        edges=[_Edge("protein.A", "represses", "gene.B")],
        entities={
            "protein.A": _Entity("repressorA"),
            "gene.B": _Entity("geneB"),
            "protein.C": _Entity("regC"),
            "gene.D": _Entity("geneD"),
            "protein.E": _Entity("regE"),
        },
    )
    out = insights.literature_overview(tmp_path, loader=loader)
    assert out["available"] is True
    assert out["count"] == 3
    assert out["overlap"]["in_base_graph"] == 1
    assert out["overlap"]["novel"] == 2
    assert out["overlap"]["unresolved_endpoints"] == 1
    first = out["edges"][0]
    assert first["in_base_graph"] is True
    assert first["doi"] == "10.1/x"
    assert first["source_name"] == "repressorA"


def test_kg_validation_parse(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "KG_VALIDATION_20260614.md").write_text(
        "# KG validation\n"
        "- Regulators mappable to a graph entity: **95.1%** (6990/7352)\n"
        "- **Interactions present as a graph edge: 58.8% of all gold (4325/7352); "
        "62.0% of the mappable subset (4325/6974)**\n"
        "- **Sign agreement (activates+, represses-): 100.0% (4072/4072)**\n",
        encoding="utf-8",
    )
    out = insights.kg_validation_report(tmp_path)
    assert out["available"] is True
    assert out["parsed"]["recall"] == {"pct": 58.8, "count": 4325, "total": 7352}
    assert out["parsed"]["sign_accuracy"] == {"pct": 100.0, "count": 4072, "total": 4072}
    assert out["parsed"]["regulators_mappable"]["pct"] == 95.1


def test_scorecard_index_and_payload(tmp_path):
    assert insights.scorecard_index(tmp_path) == []
    assert insights.scorecard_payload(tmp_path) is None
    sc = tmp_path / "runs" / "_scorecard"
    (sc / "20260101_000000").mkdir(parents=True)
    (sc / "20260102_000000").mkdir(parents=True)
    (sc / "20260101_000000" / "scorecard.json").write_text('{"timestamp": "20260101_000000"}', encoding="utf-8")
    (sc / "20260102_000000" / "scorecard.json").write_text('{"timestamp": "20260102_000000"}', encoding="utf-8")
    idx = insights.scorecard_index(tmp_path)
    assert [i["timestamp"] for i in idx] == ["20260102_000000", "20260101_000000"]
    latest = insights.scorecard_payload(tmp_path, "latest")
    assert latest["timestamp"] == "20260102_000000"
    assert insights.scorecard_payload(tmp_path, "nope") is None
