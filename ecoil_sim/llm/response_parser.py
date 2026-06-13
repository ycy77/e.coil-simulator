"""Robust parsing of LLM JSON output.

The simulator must accept model output that may contain:
- `<think>...</think>` blocks (Qwen3 style reasoning)
- Markdown ```json``` fences
- Trailing prose after the JSON
- Truncated JSON when `max_tokens` is hit mid-list
- Multiple JSON objects (only the last valid one is kept)

The public entry point is :func:`parse_llm_output`. It returns a tuple of
``(parsed_dict, diagnostics)``. ``diagnostics`` is a dict of booleans that
describe which recovery steps were applied. It is used for telemetry and
unit tests, not for control flow.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple


_THINK_BLOCK = re.compile(r"<think>[\s\S]*?</think>", re.IGNORECASE)
_FENCE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)
_JSON_DECODER = json.JSONDecoder()


@dataclass
class ParseDiagnostics:
    stripped_think: bool = False
    stripped_fence: bool = False
    trimmed_trailing_prose: bool = False
    repaired_truncated: bool = False
    multiple_objects: bool = False
    final_method: str = "none"
    original_length: int = 0
    cleaned_length: int = 0
    notes: list = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stripped_think": self.stripped_think,
            "stripped_fence": self.stripped_fence,
            "trimmed_trailing_prose": self.trimmed_trailing_prose,
            "repaired_truncated": self.repaired_truncated,
            "multiple_objects": self.multiple_objects,
            "final_method": self.final_method,
            "original_length": self.original_length,
            "cleaned_length": self.cleaned_length,
            "notes": list(self.notes),
        }


def parse_llm_output(text: str) -> Tuple[Dict[str, Any], ParseDiagnostics]:
    """Parse LLM output into a dict, applying the documented recovery steps."""
    diag = ParseDiagnostics()
    if not text:
        return {"actions": []}, diag
    diag.original_length = len(text)
    cleaned = text

    cleaned, diag.stripped_think = _strip_think(cleaned)
    cleaned, diag.stripped_fence = _strip_fence(cleaned)
    cleaned = cleaned.strip()
    diag.cleaned_length = len(cleaned)

    parsed = _try_strict(cleaned, diag)
    if parsed is not None:
        return _finalize(parsed, diag)

    parsed = _scan_objects(cleaned, diag)
    if parsed is not None:
        return _finalize(parsed, diag)

    parsed = _try_repair_truncated(cleaned, diag)
    if parsed is not None:
        return _finalize(parsed, diag)

    diag.notes.append("no_valid_json_found")
    return {"actions": []}, diag


def _strip_think(text: str) -> Tuple[str, bool]:
    if _THINK_BLOCK.search(text):
        return _THINK_BLOCK.sub("", text), True
    return text, False


def _strip_fence(text: str) -> Tuple[str, bool]:
    match = _FENCE.search(text)
    if not match:
        return text, False
    inner = match.group(1).strip()
    prefix = text[: match.start()]
    suffix = text[match.end():]
    return (prefix + inner + suffix).strip(), True


def _try_strict(text: str, diag: ParseDiagnostics) -> Optional[Dict[str, Any]]:
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        diag.notes.append(f"strict_json_failed:{exc.msg}")
        return None
    if isinstance(value, dict):
        diag.final_method = "strict"
        return value
    diag.notes.append("strict_json_not_object")
    return None


def _scan_objects(text: str, diag: ParseDiagnostics) -> Optional[Dict[str, Any]]:
    last_value: Optional[Dict[str, Any]] = None
    last_end = -1
    idx = 0
    while idx < len(text):
        if text[idx] != "{":
            idx += 1
            continue
        try:
            value, end = _JSON_DECODER.raw_decode(text, idx)
        except json.JSONDecodeError:
            idx += 1
            continue
        if isinstance(value, dict):
            if last_value is not None:
                diag.multiple_objects = True
            last_value = value
            last_end = end
        idx = end
    if last_value is None:
        return None
    if last_end < len(text):
        diag.trimmed_trailing_prose = True
    if diag.final_method == "none":
        diag.final_method = "object_scan"
    return last_value


def _try_repair_truncated(text: str, diag: ParseDiagnostics) -> Optional[Dict[str, Any]]:
    last_brace = text.rfind("{")
    if last_brace < 0:
        return None
    candidate = text[last_brace:].rstrip()
    diag.trimmed_trailing_prose = True
    closing_string, _ = _detect_open_string(candidate)
    if closing_string is not None:
        candidate = candidate + closing_string
    closers = ("]}}", "}}", "]", "}")
    for closer in closers:
        repaired = candidate + closer
        try:
            value = json.loads(repaired)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            diag.repaired_truncated = True
            diag.final_method = "truncated_repair"
            return value
    return None


def _detect_open_string(text: str) -> Tuple[Optional[str], bool]:
    """Return a closing quote if ``text`` ends mid-string."""
    in_string = False
    escape = False
    for ch in text:
        if escape:
            escape = False
            continue
        if ch == "\\":
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
    if in_string:
        return '"', True
    return None, False


def _finalize(parsed: Dict[str, Any], diag: ParseDiagnostics) -> Tuple[Dict[str, Any], ParseDiagnostics]:
    if "actions" not in parsed:
        diag.notes.append("missing_actions_key_inserted_empty")
        parsed["actions"] = []
    elif not isinstance(parsed.get("actions"), list):
        diag.notes.append("actions_not_list_replaced_empty")
        parsed["actions"] = []
    return parsed, diag
