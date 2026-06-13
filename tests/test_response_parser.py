"""Unit tests for ``ecoil_sim.llm.response_parser``."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.llm import parse_llm_output  # noqa: E402


def _actions(payload):
    return payload.get("actions", [])


def test_strict_json_passes_through():
    text = '{"actions": [{"action_type": "noop", "rule_id": "r1", "targets": [], "direction": "none", "strength": 0, "reason": "ok"}]}'
    parsed, diag = parse_llm_output(text)
    assert len(_actions(parsed)) == 1
    assert diag.final_method == "strict"
    assert diag.stripped_think is False
    assert diag.stripped_fence is False


def test_strips_think_block():
    text = (
        "<think>The model reasoned about the perturbation here.</think>\n"
        '{"actions": [{"action_type": "change_activity", "rule_id": "r2", '
        '"targets": ["a"], "direction": "up", "strength": 1, "reason": "x"}]}'
    )
    parsed, diag = parse_llm_output(text)
    assert diag.stripped_think is True
    assert len(_actions(parsed)) == 1
    assert _actions(parsed)[0]["rule_id"] == "r2"


def test_strips_markdown_fence():
    text = (
        "```json\n"
        '{"actions": [{"action_type": "produce", "rule_id": "r3", '
        '"targets": ["b"], "direction": "up", "strength": 1, "reason": "y"}]}\n'
        "```"
    )
    parsed, diag = parse_llm_output(text)
    assert diag.stripped_fence is True
    assert len(_actions(parsed)) == 1
    assert _actions(parsed)[0]["action_type"] == "produce"


def test_recovers_truncated_json():
    # Truncation point is after the inner action closes but before the
    # outer object and list are closed; this is the case that vLLM hits
    # most often when ``max_tokens`` runs out mid-emit.
    text = (
        '{"actions": [{"action_type": "change_activity", "rule_id": "r4", '
        '"targets": ["c"], "direction": "up", "strength": 1, "reason": "truncated"}]'
    )
    parsed, diag = parse_llm_output(text)
    assert diag.repaired_truncated is True
    assert len(_actions(parsed)) == 1
    assert _actions(parsed)[0]["rule_id"] == "r4"


def test_multiple_objects_keeps_last_valid():
    text = (
        '{"unrelated": true}\n'
        '{"actions": [{"action_type": "noop", "rule_id": "r5", "targets": [], "direction": "none", "strength": 0, "reason": "keep me"}]}'
    )
    parsed, diag = parse_llm_output(text)
    assert diag.multiple_objects is True
    assert len(_actions(parsed)) == 1


def test_missing_actions_key_inserted_empty():
    text = '{"other": "value"}'
    parsed, diag = parse_llm_output(text)
    assert "actions" in parsed
    assert parsed["actions"] == []


def test_actions_not_list_replaced_empty():
    text = '{"actions": "not a list"}'
    parsed, diag = parse_llm_output(text)
    assert parsed["actions"] == []


def test_empty_string_returns_empty_actions():
    parsed, diag = parse_llm_output("")
    assert parsed == {"actions": []}
    assert diag.original_length == 0


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
    print("all response_parser tests passed")
