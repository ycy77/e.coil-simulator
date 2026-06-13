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

    # Object scan handles trailing prose and multiple objects. But when the
    # output is truncated mid-wrapper, scanning only recovers an inner action
    # fragment (no top-level "actions" key) -- in that case we fall through to
    # truncation repair, which rebuilds the outer wrapper. We therefore prefer
    # whichever candidate actually carries an "actions" list.
    scanned = _scan_objects(cleaned, diag)
    if _has_actions_list(scanned):
        return _finalize(scanned, diag)

    repaired = _try_repair_truncated(cleaned, diag)
    if _has_actions_list(repaired):
        return _finalize(repaired, diag)

    if scanned is not None:
        return _finalize(scanned, diag)
    if repaired is not None:
        return _finalize(repaired, diag)

    diag.notes.append("no_valid_json_found")
    return {"actions": []}, diag


def _has_actions_list(value: Optional[Dict[str, Any]]) -> bool:
    return isinstance(value, dict) and isinstance(value.get("actions"), list)


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
    """Rebuild a wrapper object from output that was cut off mid-emit.

    Starting from the *outer* ``{`` (the wrapper, not the last fragment), we
    close any dangling string and unbalanced brackets. If the tail holds an
    incomplete element (``..., {"action_type": "ch``), we retry from each
    earlier closing bracket so the complete actions are kept and only the
    partial trailing element is dropped.
    """
    start = text.find("{")
    if start < 0:
        return None
    body = text[start:].rstrip()

    candidates = [_balance(body)]
    for cut in _close_boundaries(body):
        chunk = body[:cut].rstrip().rstrip(",").rstrip()
        if chunk:
            candidates.append(_balance(chunk))

    for candidate in candidates:
        try:
            value = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            diag.repaired_truncated = True
            diag.trimmed_trailing_prose = True
            diag.final_method = "truncated_repair"
            return value
    return None


def _balance(chunk: str) -> str:
    """Append the closers needed to make ``chunk`` syntactically complete."""
    stack: list = []
    in_string = False
    escape = False
    for ch in chunk:
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if stack:
                stack.pop()
    suffix = '"' if in_string else ""
    for opener in reversed(stack):
        suffix += "}" if opener == "{" else "]"
    return chunk + suffix


def _close_boundaries(chunk: str) -> list:
    """Indices just after each closing bracket (ignoring strings), descending.

    Used as retry cut points so a truncated trailing element can be dropped
    while keeping every element that was fully emitted before it.
    """
    boundaries = []
    in_string = False
    escape = False
    for idx, ch in enumerate(chunk):
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch in "}]":
            boundaries.append(idx + 1)
    return [b for b in sorted(set(boundaries), reverse=True) if b < len(chunk)]


def _finalize(parsed: Dict[str, Any], diag: ParseDiagnostics) -> Tuple[Dict[str, Any], ParseDiagnostics]:
    if "actions" not in parsed:
        diag.notes.append("missing_actions_key_inserted_empty")
        parsed["actions"] = []
    elif not isinstance(parsed.get("actions"), list):
        diag.notes.append("actions_not_list_replaced_empty")
        parsed["actions"] = []
    return parsed, diag
