from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_yaml_like(path: Path) -> Dict[str, Any]:
    """Load a project YAML config via PyYAML.

    PyYAML is a hard dependency (see requirements.txt). The project config,
    initial-condition, phenotype and perturbation files use block scalars,
    flow mappings and lists that a hand-rolled mini-parser cannot read
    correctly. Per the project's #1 hard rule ("no silent fallback"), this
    refuses to guess: if PyYAML is missing we raise instead of returning a
    silently corrupted dict.
    """
    try:
        import yaml  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment guard
        raise RuntimeError(
            "PyYAML is required to load config files but is not installed. "
            "Install it with `pip install -r requirements.txt` (or `pip install PyYAML`). "
            f"Tried to load: {path}"
        ) from exc

    with path.open(encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(
            f"Expected a YAML mapping at the top level of {path}, got {type(loaded).__name__}."
        )
    return loaded


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
