"""Offline tests for the vLLM request payload and guided-decoding wiring.

These do not hit a live endpoint; they assert that the request body the client
builds is shaped the way vLLM's OpenAI-compatible server expects (extension
fields at the top level, guided_json present only when configured).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.llm import AsyncVLLMClient, load_guided_json  # noqa: E402

MESSAGES = [{"role": "user", "content": "hi"}]


def test_payload_without_guided_json():
    client = AsyncVLLMClient(base_url="http://x", model="m")
    payload = client._build_payload(MESSAGES)
    assert payload["model"] == "m"
    assert payload["messages"] == MESSAGES
    # thinking is disabled via the top-level chat_template_kwargs (not nested
    # under an extra_body key that a raw POST would drop).
    assert payload["chat_template_kwargs"] == {"enable_thinking": False}
    assert "extra_body" not in payload
    assert "guided_json" not in payload
    assert "response_format" not in payload


def test_payload_with_guided_json_uses_response_format():
    # Schema-constrained decoding goes through response_format/json_schema (what
    # the deployed vLLM honors), NOT a top-level guided_json (silently ignored).
    schema = {"type": "object", "required": ["actions"]}
    client = AsyncVLLMClient(base_url="http://x", model="m", guided_json=schema)
    payload = client._build_payload(MESSAGES)
    assert "guided_json" not in payload
    rf = payload["response_format"]
    assert rf["type"] == "json_schema"
    assert rf["json_schema"]["schema"] == schema


def test_load_guided_json_disabled():
    assert load_guided_json({}, PROJECT_ROOT) is None
    assert load_guided_json({"structured_output": {"require_json": False}}, PROJECT_ROOT) is None


def test_load_guided_json_enabled_loads_action_schema():
    cfg = {"structured_output": {"require_json": True, "schema_file": "schemas/action.schema.json"}}
    schema = load_guided_json(cfg, PROJECT_ROOT)
    assert isinstance(schema, dict)
    assert "actions" in schema["properties"]


def test_action_schema_covers_validator_action_types():
    """The guided schema must allow every action the validator accepts, or
    guided decoding would forbid valid actions (e.g. change_efficiency)."""
    from ecoil_sim.validation import ActionValidator

    schema = json.loads((PROJECT_ROOT / "schemas" / "action.schema.json").read_text())
    enum = set(schema["properties"]["actions"]["items"]["properties"]["action_type"]["enum"])
    assert ActionValidator.ACTION_TYPES <= enum, (
        f"schema missing action types: {ActionValidator.ACTION_TYPES - enum}"
    )
