"""Perturbation intake front door for the diagnostic UI.

Wraps the existing offline scaffolding (``EntityGrounder`` +
``LLMPerturbationParser``) so the web layer can:

  * ``parse(text)``  — chat/file text -> LLM-grounded ``PerturbationProposal``
    serialized for the confirm UI (the human-judgment boundary).
  * ``ground_preview(text)`` — offline grounding candidates only, no vLLM.
  * ``run(changes)`` — launch a real simulation over the confirmed changes by
    spawning ``main.py --perturbation-json`` as a detached subprocess (so a
    minutes-long GPU run never blocks the API worker).

Nothing runs automatically: ``parse`` proposes, the user confirms in the UI,
then ``run`` is an explicit second call. The heavy graph/grounder objects are
built lazily on first use to keep backend startup fast.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import Entity
from ecoil_sim.sim.grounding import EntityGrounder
from ecoil_sim.sim.llm_perturbation import LLMPerturbationParser, VLLMJsonCompleter


class PerturbationService:
    def __init__(
        self,
        project_root: Path,
        config_path: Path = Path("configs/simulation.yaml"),
        model_config_path: Path = Path("configs/model.qwen35_9b.yaml"),
        intake_schema_path: Path = Path("schemas/perturbation_intake.schema.json"),
    ) -> None:
        self.root = project_root
        self.config_path = config_path
        self.model_config_path = model_config_path
        self.intake_schema_path = intake_schema_path
        self._graph: Optional[StaticGraph] = None
        self._grounder: Optional[EntityGrounder] = None
        self._parser: Optional[LLMPerturbationParser] = None

    # -- lazy construction -------------------------------------------------- #
    def _ensure_grounder(self) -> None:
        if self._grounder is not None:
            return
        config = load_yaml_like(self.root / self.config_path)
        graph_cfg = config.get("graph", {})
        graph = StaticGraph.from_normalized_dir(
            self.root / graph_cfg.get("normalized_dir", "data/normalized")
        )
        perturbagen_csv = self.root / "data" / "normalized" / "perturbagens" / "entities.csv"
        perturbagens: List[Entity] = []
        if perturbagen_csv.exists():
            with perturbagen_csv.open(newline="", encoding="utf-8") as handle:
                perturbagens = [Entity.from_row(row) for row in csv.DictReader(handle)]
        self._graph = graph
        self._grounder = EntityGrounder(graph.entities.values(), perturbagens)

    def _ensure_parser(self) -> None:
        if self._parser is not None:
            return
        self._ensure_grounder()
        model_config = load_yaml_like(self.root / self.model_config_path)
        llm_cfg = model_config.get("llm", {})
        completer = VLLMJsonCompleter(
            base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
            model=llm_cfg.get("model", ""),
            api_key=llm_cfg.get("api_key", "EMPTY"),
        )
        intake_schema = None
        schema_abs = self.root / self.intake_schema_path
        if schema_abs.exists():
            intake_schema = json.loads(schema_abs.read_text(encoding="utf-8"))
        self._parser = LLMPerturbationParser(
            self._graph, self._grounder, completer,
            prompts_dir=self.root / "prompts", intake_schema=intake_schema,
        )

    # -- public API --------------------------------------------------------- #
    def ground_preview(self, text: str) -> Dict[str, Any]:
        """Offline grounding candidates per clause (no vLLM)."""
        self._ensure_grounder()
        mentions = [m.strip() for m in re.split(r",|;|\band\b|\n", text) if m.strip()]
        out = []
        for mention in mentions:
            ranked = self._grounder.candidates(mention, limit=5)
            out.append({
                "mention": mention,
                "candidates": [
                    {
                        "entity_id": c.entity_id,
                        "name": c.name,
                        "matched_via": c.matched_via,
                        "allowed_states": list(c.allowed_states),
                        "is_exogenous": c.is_exogenous,
                    }
                    for c in ranked
                ],
            })
        return {"mode": "dry_run", "clauses": out}

    def parse(self, text: str) -> Dict[str, Any]:
        """LLM-grounded proposal, serialized for the confirm UI."""
        self._ensure_parser()
        proposal = self._parser.parse_text(text)
        return {
            "perturbations": [
                {
                    "entity_id": p.entity_id,
                    "target_state": p.target_state,
                    "agent_mention": p.agent_mention,
                    "agent_kind": p.agent_kind,
                    "evidence": p.evidence,
                    "confidence": p.confidence,
                    "reason": p.reason,
                }
                for p in proposal.perturbations
            ],
            "unresolved": proposal.unresolved,
            "engine_changes": proposal.to_engine_changes(),
            "render": proposal.render(),
        }

    def run(self, changes: List[Dict[str, Any]], rounds: int = 5, use_llm: bool = True) -> Dict[str, Any]:
        """Launch a simulation over confirmed changes as a detached subprocess."""
        if not changes:
            raise ValueError("no changes to run")
        intake_dir = self.root / "runs" / "_intake"
        intake_dir.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d_%H%M%S")
        changes_file = intake_dir / f"intake_{stamp}.json"
        changes_file.write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding="utf-8")
        log_file = intake_dir / f"intake_{stamp}.log"

        cmd = [
            sys.executable, "main.py",
            "--mock-llm" if not use_llm else "--use-llm",
            "--perturbation-json", str(changes_file),
            "--rounds", str(rounds),
        ]
        with log_file.open("w", encoding="utf-8") as log:
            subprocess.Popen(
                cmd, cwd=str(self.root), stdout=log, stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        return {
            "launched": True,
            "changes_file": str(changes_file.relative_to(self.root)),
            "log_file": str(log_file.relative_to(self.root)),
            "command": " ".join(cmd),
            "note": "run started in background; watch the run list for the new run dir",
        }
