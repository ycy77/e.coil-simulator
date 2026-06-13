from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_yaml_like(path: Path) -> Dict[str, Any]:
    """Tiny YAML reader for the simple config files used here.

    It prefers PyYAML when available. The fallback supports nested dicts and
    scalar values used by this project, so the core simulator has no hard
    dependency on PyYAML.
    """
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None
    if yaml is not None:
        with path.open(encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}

    root: Dict[str, Any] = {}
    stack: list[tuple[int, Dict[str, Any]]] = [(-1, root)]
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, value = line.strip().partition(":")
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value.strip() == "":
            node: Dict[str, Any] = {}
            parent[key] = node
            stack.append((indent, node))
        else:
            parent[key] = _parse_scalar(value.strip())
    return root


def _parse_scalar(value: str) -> Any:
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "None"}:
        return None
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value.strip('"').strip("'")


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
