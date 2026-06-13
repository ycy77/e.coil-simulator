"""Global-view report agent.

The per-entity agents each see only their local neighbourhood (that locality is
what makes the conflict reasoning honest). After the run converges, a *single*
report agent is given the whole picture and writes the biological narrative.

It is deliberately the only place with a global view: perturbation sources,
round-by-round propagation, causal chains, final changed states, and phenotype
matches (from `Reporter.summarize_changes`). It pulls the annotations of the
entities involved so the narrative is grounded in real function, not invented.

The LLM is injected as ``complete(system, user, guided_json) -> str`` so this is
unit-testable offline with a stub; the real vLLM call (free text, no guided_json)
runs on the GPU host. There is no deterministic fallback narrative here — if no
LLM is available, the caller keeps the deterministic `Reporter.render_narrative`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Dict, List, Optional

from ecoil_sim.graph import StaticGraph

CompleteFn = Callable[[str, str, Optional[dict]], str]


class LLMReportAgent:
    def __init__(
        self,
        complete: CompleteFn,
        *,
        graph: Optional[StaticGraph] = None,
        prompt_path: Optional[Path] = None,
        annotation_chars: int = 600,
        max_entities: int = 60,
    ) -> None:
        self.complete = complete
        self.graph = graph
        self.prompt_path = Path(prompt_path) if prompt_path else None
        self.annotation_chars = annotation_chars
        self.max_entities = max_entities

    def write_report(self, structured_report: Dict) -> str:
        """Produce a Markdown biological report from the run summary."""
        if not structured_report.get("changed_events"):
            return "No changes propagated from the perturbation; nothing to report."
        system = self._system_prompt()
        user = json.dumps(self._build_context(structured_report), ensure_ascii=False)
        return (self.complete(system, user, None) or "").strip()

    # ---------------------------------------------------------------- helpers
    def _build_context(self, report: Dict) -> Dict:
        """Assemble the global view + annotations for the entities involved."""
        final_states = report.get("final_changed_states", {}) or {}
        sources = report.get("perturbation_sources", []) or []
        # Which entities to annotate: sources + final changed (capped).
        involved: List[str] = list(dict.fromkeys(list(sources) + list(final_states.keys())))
        involved = involved[: self.max_entities]
        return {
            "perturbation_sources": [self._entity_brief(eid) for eid in sources],
            "rounds": report.get("rounds"),
            "events_by_round": report.get("events_by_round", {}),
            "propagation_edges": report.get("propagation_edges", []),
            "causal_chains": [
                [self._name(eid) for eid in chain]
                for chain in report.get("causal_chains", [])
            ],
            "final_changed_states": {
                self._name(eid): payload for eid, payload in final_states.items()
            },
            "phenotype_matches": [
                {
                    "pattern_id": m.get("pattern_id"),
                    "similarity": m.get("similarity"),
                    "matched": m.get("matched"),
                    "total": m.get("total"),
                    "required_signals_present": m.get("required_signals_present"),
                    "description": (m.get("description", "") or "").strip(),
                }
                for m in (report.get("response_pattern_match", {}) or {}).get("matches", [])
            ],
            "annotations": {self._name(eid): self._annotation(eid) for eid in involved},
        }

    def _entity_brief(self, entity_id: str) -> Dict:
        return {"id": entity_id, "name": self._name(entity_id), "annotation": self._annotation(entity_id)}

    def _name(self, entity_id: str) -> str:
        if self.graph and entity_id in self.graph.entities:
            entity = self.graph.entities[entity_id]
            display = entity.name or entity_id
            return f"{display} ({entity_id})"
        return entity_id

    def _annotation(self, entity_id: str) -> str:
        if self.graph and entity_id in self.graph.entities:
            entity = self.graph.entities[entity_id]
            return (entity.annotation or entity.notes or "")[: self.annotation_chars]
        return ""

    def _system_prompt(self) -> str:
        if self.prompt_path and self.prompt_path.exists():
            return self.prompt_path.read_text(encoding="utf-8")
        return "Write a grounded biological report of this E. coli simulation run."
