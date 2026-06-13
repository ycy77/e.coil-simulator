"""Enriched-entity loader.

Reads ``data/enriched/entities_enriched_lite.jsonl`` (the lighter
variant without the per-database raw annotation block) and exposes
the structured fields the diagnostic UI and the LLM prompt builder
need:

- ``display_name`` — canonical readable name (replaces entity.name
  for display)
- ``summary`` — enriched paragraph
- ``functional_context`` — concise role description
- ``linked_entities`` — cross-references (encoded_protein,
  encoding_genes, etc.)
- ``edge_context`` — local in/out degree summary
- ``evidence_sources`` — list of contributing DBs
- ``quality`` — ``informative`` / ``placeholder`` / ``empty`` flag

The loader is a thin pass-through: it never modifies the source
files, only reads them. Internal connections still use the canonical
``entity_id``; this layer only affects what the user sees and what
the LLM is told.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class EnrichedRecord:
    entity_id: str
    display_name: str
    summary: str
    functional_context: str
    biological_role: str
    linked_entities: Dict
    edge_context: Dict
    evidence_sources: List[str]
    quality: Dict[str, str]
    pathways: str
    subcellular_location: str
    source_database: str
    aliases: List[str] = field(default_factory=list)
    family_key: str = ""
    is_exogenous: str = "false"
    merged_from: List[str] = field(default_factory=list)
    source_databases: List[str] = field(default_factory=list)

    @property
    def quality_label(self) -> str:
        return self.quality.get("enriched_summary_quality", "unknown")

    def to_dict(self) -> Dict:
        return {
            "entity_id": self.entity_id,
            "display_name": self.display_name,
            "summary": self.summary,
            "functional_context": self.functional_context,
            "biological_role": self.biological_role,
            "linked_entities": self.linked_entities,
            "edge_context": self.edge_context,
            "evidence_sources": self.evidence_sources,
            "quality": self.quality,
            "quality_label": self.quality_label,
            "pathways": self.pathways,
            "subcellular_location": self.subcellular_location,
            "source_database": self.source_database,
            "aliases": self.aliases,
            "family_key": self.family_key,
            "is_exogenous": self.is_exogenous,
            "merged_from": self.merged_from,
            "source_databases": self.source_databases,
        }


class EnrichedLoader:
    """In-memory load + index for the enriched entity cards."""

    def __init__(self, enriched_path: Path) -> None:
        self.enriched_path = enriched_path
        self._by_id: Dict[str, EnrichedRecord] = {}
        self._summary_count = 0

    def load(self) -> None:
        if not self.enriched_path.exists():
            logger.warning("enriched file not found: %s", self.enriched_path)
            return
        with self.enriched_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                data = json.loads(line)
                record = self._parse(data)
                if record.summary:
                    self._summary_count += 1
                self._by_id[record.entity_id] = record
        logger.info(
            "EnrichedLoader loaded %d cards (with summary: %d)",
            len(self._by_id),
            self._summary_count,
        )

    @staticmethod
    def _parse(data: Dict) -> EnrichedRecord:
        return EnrichedRecord(
            entity_id=data.get("entity_id", ""),
            display_name=data.get("display_name", "") or data.get("canonical_name", ""),
            summary=data.get("summary", "") or "",
            functional_context=data.get("functional_context", "") or "",
            biological_role=data.get("biological_role", "") or "",
            linked_entities=data.get("linked_entities", {}) or {},
            edge_context=data.get("edge_context", {}) or {},
            evidence_sources=data.get("evidence_sources", []) or [],
            quality=data.get("quality", {}) or {},
            pathways=data.get("pathways", "") or "",
            subcellular_location=data.get("subcellular_location", "") or "",
            source_database=data.get("source_database", "") or "",
            aliases=data.get("aliases", []) or [],
            family_key=data.get("family_key", "") or "",
            is_exogenous=str(data.get("is_exogenous", "false")),
            merged_from=data.get("merged_from", []) or [],
            source_databases=data.get("source_databases", []) or [],
        )

    def get(self, entity_id: str) -> Optional[EnrichedRecord]:
        return self._by_id.get(entity_id)

    def quality_distribution(self) -> Dict[str, int]:
        out: Dict[str, int] = {}
        for record in self._by_id.values():
            label = record.quality_label
            out[label] = out.get(label, 0) + 1
        return out

    def count_with_summary(self) -> int:
        return self._summary_count
