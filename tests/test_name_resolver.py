"""Unit tests for ``ecoil_sim.llm.name_resolver``."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.llm import NameResolver  # noqa: E402
from ecoil_sim.models import Entity  # noqa: E402


def _make_entities():
    return [
        Entity(
            entity_id="protein.P03023",
            entity_type="protein",
            name="lacI",
            aliases=["LacI repressor", "LacI", "b0345"],
            default_state="active",
            allowed_states=["active", "inhibited"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="UniProt:P03023",
        ),
        Entity(
            entity_id="gene.b0345",
            entity_type="gene",
            name="lacI",
            aliases=["lacI", "b0345"],
            default_state="expressed",
            allowed_states=["expressed", "repressed"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="",
        ),
        Entity(
            entity_id="molecule.C00031",
            entity_type="small_molecule",
            name="D-Glucose",
            aliases=["D-Glucose", "Glucose", "Dextrose"],
            default_state="medium",
            allowed_states=["absent", "low", "medium", "high"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="KEGG:C00031",
        ),
        Entity(
            entity_id="molecule.C22855",
            entity_type="small_molecule",
            name="Glucose monomycolate",
            aliases=["Glucose monomycolate", "Glucose", "GMM"],
            default_state="medium",
            allowed_states=["absent", "low", "medium", "high"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="",
        ),
    ]


def test_to_public_includes_id_hint():
    resolver = NameResolver(_make_entities())
    rendered = resolver.to_public("protein.P03023")
    assert "lacI" in rendered
    assert "(protein.P03023)" in rendered


def test_id_hint_extraction_resolves_canonical_id():
    resolver = NameResolver(_make_entities())
    resolved = resolver.from_public("LacI repressor (protein.P03023)")
    assert resolved is not None
    assert resolved.entity_id == "protein.P03023"
    assert resolved.matched_via == "id_hint"


def test_exact_name_lowercase():
    resolver = NameResolver(_make_entities())
    resolved = resolver.from_public("d-glucose")
    assert resolved is not None
    assert resolved.entity_id == "molecule.C00031"


def test_ambiguous_alias_prefers_shortest_name():
    resolver = NameResolver(_make_entities())
    resolved = resolver.from_public("glucose")
    assert resolved is not None
    assert resolved.entity_id == "molecule.C00031"
    assert resolved.name == "D-Glucose"


def test_unknown_query_returns_none():
    resolver = NameResolver(_make_entities())
    assert resolver.from_public("asdfqwerty") is None


def test_fuzzy_candidates_returns_ranked_list():
    resolver = NameResolver(_make_entities())
    candidates = resolver.fuzzy_candidates("lacI", limit=5)
    assert candidates
    ids = [c.entity_id for c in candidates]
    assert "protein.P03023" in ids
    assert "gene.b0345" in ids


def test_word_boundary_keeps_compound_words_apart():
    resolver = NameResolver(_make_entities())
    # Hyphens are treated as word separators, so "udp-glucose" still contains
    # "glucose" as a separate word — which is the intended behaviour for
    # hyphenated chemical names that share a common fragment.
    assert resolver._word_boundary_contains("udp-glucose", "glucose") is True
    assert resolver._word_boundary_contains("alpha-d-glucose", "glucose") is True
    assert resolver._word_boundary_contains("glucose", "glucose") is True
    # Alphanumeric adjacency is what blocks accidental substrings.
    assert resolver._word_boundary_contains("betaglucose", "glucose") is False
    assert resolver._word_boundary_contains("glucosemono", "glucose") is False


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
    print("all name_resolver tests passed")
