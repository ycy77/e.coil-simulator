"""Unit tests for the natural-language perturbation parser."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.llm import NameResolver  # noqa: E402
from ecoil_sim.sim.perturbation import NaturalLanguagePerturbationParser  # noqa: E402


def test_english_perturbation_resolves_known_entity():
    graph = StaticGraph.from_normalized_dir()
    parser = NaturalLanguagePerturbationParser(
        graph,
        name_resolver=NameResolver(graph.entities.values()),
    )
    result = parser.parse("inhibit LacI")
    assert result.changes
    entity_ids = {change["entity_id"] for change in result.changes}
    # "LacI" can refer to either the gene or the protein; both are
    # valid resolutions. The NameResolver currently prefers the
    # protein because "LacI" is a protein name.
    assert entity_ids & {"gene.b0345", "protein.P03023"}


def test_perturbation_strips_intent_verb_to_avoid_name_collision():
    graph = StaticGraph.from_normalized_dir()
    parser = NaturalLanguagePerturbationParser(
        graph,
        name_resolver=NameResolver(graph.entities.values()),
    )
    result = parser.parse("add lactose")
    assert result.changes
    entity_ids = {change["entity_id"] for change in result.changes}
    assert "molecule.C00243" in entity_ids


def test_remove_glucose_resolves_d_glucose():
    graph = StaticGraph.from_normalized_dir()
    parser = NaturalLanguagePerturbationParser(
        graph,
        name_resolver=NameResolver(graph.entities.values()),
    )
    result = parser.parse("remove glucose")
    assert result.changes
    entity_ids = {change["entity_id"] for change in result.changes}
    assert "molecule.C00031" in entity_ids


def test_unknown_intent_yields_unresolved_clause():
    graph = StaticGraph.from_normalized_dir()
    parser = NaturalLanguagePerturbationParser(
        graph,
        name_resolver=NameResolver(graph.entities.values()),
    )
    result = parser.parse("make pancakes out of glucose")
    assert not result.changes
    assert result.unresolved


def test_chinese_intent_resolves_known_entity():
    graph = StaticGraph.from_normalized_dir()
    parser = NaturalLanguagePerturbationParser(
        graph,
        name_resolver=NameResolver(graph.entities.values()),
    )
    result = parser.parse("抑制 LacI 蛋白")
    assert result.changes
    entity_ids = {change["entity_id"] for change in result.changes}
    assert entity_ids & {"gene.b0345", "protein.P03023"}


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
    print("all perturbation parser tests passed")
