"""Lightweight enriched-data service for the simulation engine.

The simulation engine and the diagnostic UI both need to look up
the enriched ``summary`` / ``linked_entities`` block that was built
by the offline enrichment step (``data/enriched/entities_enriched.jsonl``).
This loader reads the *lite* variant and exposes a tiny
``get(entity_id)`` method.

The service never modifies any in-memory graph data — it is a
read-through cache that the prompt builder queries per Agent.

Why a separate service (not on the :class:`ecoil_sim.models.Entity`)?
The simulator's :class:`Entity` is loaded from
``data/normalized/entities.csv``; attaching the enriched card at
graph-build time would couple the graph loader to the enriched
file. The service lets us load the enriched data lazily and
keeps the two concerns separate.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class EnrichedCard:
    entity_id: str
    display_name: str
    summary: str
    functional_context: str
    biological_role: str
    linked_entities: Dict
    evidence_sources: List[str] = field(default_factory=list)
    quality_label: str = "unknown"
    pathways: str = ""
    subcellular_location: str = ""
    source_database: str = ""
    aliases: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "entity_id": self.entity_id,
            "display_name": self.display_name,
            "summary": self.summary,
            "functional_context": self.functional_context,
            "biological_role": self.biological_role,
            "linked_entities": self.linked_entities,
            "evidence_sources": self.evidence_sources,
            "quality_label": self.quality_label,
            "pathways": self.pathways,
            "subcellular_location": self.subcellular_location,
            "source_database": self.source_database,
            "aliases": self.aliases,
        }


class EnrichedService:
    """Read-through cache for enriched entity cards."""

    def __init__(self, enriched_path: Optional[Path] = None) -> None:
        self.enriched_path = enriched_path
        self._cards: Dict[str, EnrichedCard] = {}
        self._loaded = False

    def load(self) -> None:
        if self._loaded or not self.enriched_path or not self.enriched_path.exists():
            return
        with self.enriched_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                card = EnrichedCard(
                    entity_id=data.get("entity_id", ""),
                    display_name=data.get("display_name", "") or "",
                    summary=data.get("summary", "") or "",
                    functional_context=data.get("functional_context", "") or "",
                    biological_role=data.get("biological_role", "") or "",
                    linked_entities=data.get("linked_entities", {}) or {},
                    evidence_sources=data.get("evidence_sources", []) or [],
                    quality_label=(data.get("quality") or {}).get("enriched_summary_quality", "unknown"),
                    pathways=data.get("pathways", "") or "",
                    subcellular_location=data.get("subcellular_location", "") or "",
                    source_database=data.get("source_database", "") or "",
                    aliases=data.get("aliases", []) or [],
                )
                self._cards[card.entity_id] = card
        self._loaded = True
        logger.info("EnrichedService loaded %d cards", len(self._cards))

    def get(self, entity_id: str) -> Optional[EnrichedCard]:
        if not self._loaded:
            self.load()
        return self._cards.get(entity_id)

    def count(self) -> int:
        if not self._loaded:
            self.load()
        return len(self._cards)
