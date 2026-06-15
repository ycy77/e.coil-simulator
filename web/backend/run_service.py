"""Read simulation run artifacts for the diagnostic UI.

Walks ``runs/<run_id>/`` and exposes meta, round-by-round stage
reports, and per-agent state histories. The reader is intentionally
read-only and tolerant of missing files: a half-written run still
loads what it can so the reviewer can see how far it got.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional


class RunService:
    def __init__(self, runs_root: Path) -> None:
        self.runs_root = runs_root

    def list_runs(self) -> List[Dict]:
        if not self.runs_root.exists():
            return []
        runs: List[Dict] = []
        for entry in sorted(self.runs_root.iterdir(), reverse=True):
            if not entry.is_dir():
                continue
            meta = self._read_json(entry / "meta.json") or {}
            if not meta:
                meta = self._read_json(entry / "graph_summary.json") or {}
            runs.append(
                {
                    "run_id": entry.name,
                    "path": str(entry),
                    "is_eval": entry.name.startswith("_"),
                    "has_meta": (entry / "meta.json").exists(),
                    "round_count": len(list((entry / "rounds").glob("round_*.json"))) if (entry / "rounds").exists() else 0,
                    "perturbations": meta.get("perturbations", []) or [],
                    "max_rounds": meta.get("max_rounds"),
                }
            )
        return runs

    def get_meta(self, run_id: str) -> Optional[Dict]:
        run_dir = self._safe_run_dir(run_id)
        if not run_dir:
            return None
        meta = self._read_json(run_dir / "meta.json")
        if meta is not None:
            meta["run_id"] = run_id
            meta["path"] = str(run_dir)
            return meta
        return None

    def get_timeline(self, run_id: str) -> List[Dict]:
        run_dir = self._safe_run_dir(run_id)
        if not run_dir:
            return []
        stages_dir = run_dir / "stage_reports"
        if not stages_dir.exists():
            return []
        timeline: List[Dict] = []
        for stage_path in sorted(stages_dir.glob("round_*.json")):
            data = self._read_json(stage_path) or {}
            timeline.append(
                {
                    "round": data.get("round"),
                    "candidate_agents": (data.get("summary") or {}).get("candidate_agents", 0),
                    "new_changed_agents": (data.get("summary") or {}).get("new_changed_agents", 0),
                    "stable_rounds": (data.get("steady_state") or {}).get("stable_rounds", 0),
                    "new_changes": data.get("new_changes", []) or [],
                }
            )
        return timeline

    def get_report(self, run_id: str) -> Optional[Dict]:
        """The run's full structured report (narrative, causal chains, phenotype
        matches, feedback_loops) saved by main.py. None for older runs."""
        run_dir = self._safe_run_dir(run_id)
        if not run_dir:
            return None
        return self._read_json(run_dir / "report.json")

    def get_agent_history(self, run_id: str, entity_id: str) -> Optional[Dict]:
        run_dir = self._safe_run_dir(run_id)
        if not run_dir:
            return None
        history_path = run_dir / "agents" / f"{entity_id}.json"
        if not history_path.exists():
            return None
        return self._read_json(history_path)

    def get_final_state(self, run_id: str, entity_id: str) -> Optional[Dict]:
        run_dir = self._safe_run_dir(run_id)
        if not run_dir:
            return None
        rounds_dir = run_dir / "rounds"
        if not rounds_dir.exists():
            return None
        snapshots = sorted(rounds_dir.glob("round_*.json"), key=lambda p: int(p.stem.split("_")[-1]))
        if not snapshots:
            return None
        for snap in reversed(snapshots):
            data = self._read_json(snap)
            if data is None:
                continue
            states = data.get("states") or {}
            if entity_id in states:
                return states[entity_id]
        return None

    def _safe_run_dir(self, run_id: str) -> Optional[Path]:
        if not run_id or run_id in {"", "."}:
            return None
        if "/" in run_id or ".." in run_id or run_id.startswith("__"):
            return None
        run_dir = self.runs_root / run_id
        if not run_dir.is_dir():
            return None
        return run_dir

    @staticmethod
    def _read_json(path: Path):
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError, OSError):
            return None
