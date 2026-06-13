from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from ecoil_sim.config import dump_json
from ecoil_sim.state import TemporalState


class SimulationStore:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.agents_dir = root / "agents"
        self.rounds_dir = root / "rounds"
        self.stage_reports_dir = root / "stage_reports"
        self.agents_dir.mkdir(parents=True, exist_ok=True)
        self.rounds_dir.mkdir(parents=True, exist_ok=True)
        self.stage_reports_dir.mkdir(parents=True, exist_ok=True)

    def write_meta(self, meta: Dict) -> None:
        dump_json(self.root / "meta.json", meta)

    def write_round(self, state: TemporalState) -> None:
        dump_json(self.rounds_dir / f"round_{state.current_round}.json", state.snapshot())

    def write_stage_report(self, round_number: int, report: Dict) -> None:
        dump_json(self.stage_reports_dir / f"round_{round_number}.json", report)

    def write_agent_histories(self, state: TemporalState) -> None:
        for entity_id, history in state.history.items():
            if len(history) <= 1:
                continue
            safe = entity_id.replace("/", "_").replace(":", "_")
            dump_json(self.agents_dir / f"{safe}.json", {"entity_id": entity_id, "history": history})

    def write_graph_summary(self, summary: Dict) -> None:
        dump_json(self.root / "graph_summary.json", summary)
