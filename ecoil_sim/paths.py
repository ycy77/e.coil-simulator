from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
NORMALIZED_DIR = DATA_DIR / "normalized"
REGISTRY_DIR = DATA_DIR / "registry"
RUNS_DIR = PROJECT_ROOT / "runs"


def project_path(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)
