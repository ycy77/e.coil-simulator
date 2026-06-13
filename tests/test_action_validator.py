"""Unit tests for the action validator and its name resolution contract."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.llm import NameResolver  # noqa: E402
from ecoil_sim.models import Entity  # noqa: E402
from ecoil_sim.validation import ActionValidator  # noqa: E402


def _entities():
    return [
        Entity(
            entity_id="protein.P03023",
            entity_type="protein",
            name="LacI repressor",
            aliases=["LacI"],
            default_state="active",
            allowed_states=["active", "inhibited"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="",
        ),
        Entity(
            entity_id="gene.b0344",
            entity_type="gene",
            name="lacZ",
            aliases=["lacZ"],
            default_state="expressed",
            allowed_states=["expressed", "repressed"],
            annotation="",
            pathways="",
            subcellular_location="",
            source_database="",
            source_id="",
            external_ids="",
        ),
    ]


def test_valid_payload_accepted():
    validator = ActionValidator()
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "native.rep.1",
                "targets": ["protein.P03023"],
                "direction": "down",
                "strength": 1,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(payload, candidate_rule_ids={"native.rep.1"})
    assert len(result["actions"]) == 1


def test_rule_hint_resolved_to_canonical():
    validator = ActionValidator()
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "R#3",
                "targets": ["protein.P03023"],
                "direction": "down",
                "strength": 1,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(
        payload,
        candidate_rule_ids={"native.rep.1"},
        rule_hint_map={"R#3": "native.rep.1"},
    )
    assert len(result["actions"]) == 1
    assert result["actions"][0]["rule_id"] == "native.rep.1"


def test_rule_id_outside_candidate_set_rejected():
    validator = ActionValidator()
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "R#3",
                "targets": ["protein.P03023"],
                "direction": "down",
                "strength": 1,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(
        payload,
        candidate_rule_ids={"other.rule"},
        rule_hint_map={"R#3": "native.rep.1"},
    )
    assert result["actions"] == []


def test_strength_out_of_range_rejected():
    validator = ActionValidator()
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "native.rep.1",
                "targets": ["protein.P03023"],
                "direction": "down",
                "strength": 5,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(payload, candidate_rule_ids={"native.rep.1"})
    assert result["actions"] == []


def test_target_public_name_resolves_to_entity_id():
    resolver = NameResolver(_entities())
    validator = ActionValidator(name_resolver=resolver)
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "native.rep.1",
                "targets": ["LacI repressor (protein.P03023)"],
                "direction": "down",
                "strength": 1,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(payload, candidate_rule_ids={"native.rep.1"})
    assert result["actions"][0]["targets"] == ["protein.P03023"]


def test_target_unresolvable_rejected():
    resolver = NameResolver(_entities())
    validator = ActionValidator(name_resolver=resolver)
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "native.rep.1",
                "targets": ["Foo bar baz nonexistent entity"],
                "direction": "down",
                "strength": 1,
                "reason": "test",
            }
        ]
    }
    result = validator.validate(payload, candidate_rule_ids={"native.rep.1"})
    assert result["actions"] == []


def test_missing_required_key_rejected():
    validator = ActionValidator()
    payload = {
        "actions": [
            {
                "action_type": "change_activity",
                "rule_id": "native.rep.1",
                "targets": ["protein.P03023"],
                "direction": "down",
                # strength missing
                "reason": "test",
            }
        ]
    }
    result = validator.validate(payload, candidate_rule_ids={"native.rep.1"})
    assert result["actions"] == []


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
    print("all action_validator tests passed")
