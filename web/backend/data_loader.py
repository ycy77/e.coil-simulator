"""In-memory data loader for the diagnostic UI.

Loads entities, edges, pathways, and rules from the project's normalized
CSV / JSONL files once at startup and indexes them in several ways so
that the FastAPI handlers can answer name / id / alias lookups in
constant time.

The loader is intentionally read-only: it never modifies the source
files. The data quality diagnosis is about understanding what is in
the files, not about cleaning them up at the loader level.
"""

from __future__ import annotations

import csv
import json
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

logger = logging.getLogger(__name__)


@dataclass
class EntityRecord:
    entity_id: str
    entity_type: str
    name: str
    aliases: List[str]
    default_state: str
    allowed_states: List[str]
    annotation: str
    pathways: str
    subcellular_location: str
    source_database: str
    source_id: str
    external_ids: str
    is_external: bool
    complex_type: str
    components: List[str]
    critical_components: List[str]
    assembly_condition: str
    notes: str
    family_key: str = ""
    is_exogenous: str = "false"
    merged_from: List[str] = field(default_factory=list)
    canonical_display_name: str = ""
    enriched: Optional["EnrichedRecord"] = None

    @property
    def annotation_length(self) -> int:
        return len(self.annotation or "")

    @property
    def display_name(self) -> str:
        """Public-facing name, preferring canonical v2 display_name."""
        if self.canonical_display_name:
            return self.canonical_display_name
        if self.enriched and self.enriched.display_name:
            return self.enriched.display_name
        return self.name or self.entity_id

    @property
    def display_summary(self) -> str:
        """Enriched summary when available, else raw annotation."""
        if self.enriched and self.enriched.summary:
            return self.enriched.summary
        return self.annotation or ""

    @property
    def quality_label(self) -> str:
        if self.enriched and self.enriched.quality:
            return self.enriched.quality_label
        if self.annotation_length == 0:
            return "empty"
        return "placeholder" if "EcoCyc" in self.annotation and len(self.annotation) < 30 else "informative"

    def to_dict(self, include_annotation: bool = True) -> Dict:
        data = {
            "entity_id": self.entity_id,
            "entity_type": self.entity_type,
            "name": self.name,
            "display_name": self.display_name,
            "aliases": self.aliases,
            "default_state": self.default_state,
            "allowed_states": self.allowed_states,
            "annotation_length": self.annotation_length,
            "annotation_empty": self.annotation_length == 0,
            "quality_label": self.quality_label,
            "pathways": self.pathways,
            "subcellular_location": self.subcellular_location,
            "source_database": self.source_database,
            "source_id": self.source_id,
            "external_ids": self.external_ids,
            "is_external": self.is_external,
            "complex_type": self.complex_type,
            "components": self.components,
            "critical_components": self.critical_components,
            "assembly_condition": self.assembly_condition,
            "notes": self.notes,
        }
        if include_annotation:
            data["annotation"] = self.annotation
        if self.enriched is not None:
            data["enriched"] = self.enriched.to_dict()
        return data


@dataclass
class EdgeRecord:
    source_id: str
    target_id: str
    relation_type: str
    semantic_relation_type: str = ""
    direction: str = "directed"
    evidence: str = ""
    source_database: str = ""
    source_record_id: str = ""
    notes: str = ""
    # Payload for flattened-reaction edges. Empty for the
    # non-conversion relations (encodes, activates, ...).
    # ``reactants`` and ``products`` are pipe-joined lists of
    # entity ids; the relationship direction is implied by
    # relation_type (produces -> target is product, consumes
    # -> target is substrate).
    reaction_id: str = ""
    reactants: str = ""
    products: str = ""
    ec_number: str = ""
    pathway: str = ""
    # Edge weight used by the simulation influence_score
    # (edge_weight * 0.7^rounds_unchanged * magnitude). 0.0
    # means "no signal"; 1.0 means maximum. Defaults to 0.40
    # for edges without an explicit weight.
    edge_weight: float = 0.40
    # STRING channel for PPI edges, blank otherwise. Allows
    # the UI to color / filter by evidence source.
    string_channel: str = ""

    def to_dict(self) -> Dict:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relation_type": self.relation_type,
            "semantic_relation_type": self.semantic_relation_type or self.relation_type,
            "direction": self.direction,
            "evidence": self.evidence,
            "source_database": self.source_database,
            "source_record_id": self.source_record_id,
            "notes": self.notes,
            "reaction_id": self.reaction_id,
            "reactants": self.reactants,
            "products": self.products,
            "ec_number": self.ec_number,
            "pathway": self.pathway,
            "edge_weight": self.edge_weight,
            "string_channel": self.string_channel,
        }


@dataclass
class PathwayRecord:
    pathway_id: str
    pathway_name: str
    source: str
    description: str
    organism: str

    def to_dict(self) -> Dict:
        return {
            "pathway_id": self.pathway_id,
            "pathway_name": self.pathway_name,
            "source": self.source,
            "description": self.description,
            "organism": self.organism,
        }


@dataclass
class DataQualityReport:
    entity_count: int
    edge_count: int
    pathway_count: int
    rule_count: int
    type_distribution: Dict[str, int]
    relation_distribution: Dict[str, int]
    source_database_distribution: Dict[str, int]
    empty_annotation_count: int
    empty_annotation_ratio: float
    duplicate_pairs: int

    def to_dict(self) -> Dict:
        return {
            "entity_count": self.entity_count,
            "edge_count": self.edge_count,
            "pathway_count": self.pathway_count,
            "rule_count": self.rule_count,
            "type_distribution": dict(sorted(self.type_distribution.items())),
            "relation_distribution": dict(sorted(self.relation_distribution.items())),
            "source_database_distribution": dict(sorted(self.source_database_distribution.items())),
            "empty_annotation_count": self.empty_annotation_count,
            "empty_annotation_ratio": round(self.empty_annotation_ratio, 4),
            "duplicate_pairs": self.duplicate_pairs,
        }


class DataLoader:
    """In-memory load + index for the diagnostic UI."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root
        self.normalized_dir = project_root / "data" / "normalized"
        self.registry_dir = project_root / "data" / "registry"
        self._entities: Dict[str, EntityRecord] = {}
        self._edges: List[EdgeRecord] = []
        self._pathways: Dict[str, PathwayRecord] = {}
        self._rules: List[Dict] = []
        self._name_to_ids: Dict[str, Set[str]] = defaultdict(set)
        self._alias_to_ids: Dict[str, Set[str]] = defaultdict(set)
        self._type_index: Dict[str, Set[str]] = defaultdict(set)
        self._edges_by_source: Dict[str, List[int]] = defaultdict(list)
        self._edges_by_target: Dict[str, List[int]] = defaultdict(list)
        self._edges_by_pair: Dict[Tuple[str, str], List[int]] = defaultdict(list)
        self._name_index: Dict[str, List[str]] = {}
        self._alias_duplicate_counts: Dict[str, int] = {}

    def load(self) -> None:
        self._load_entities()
        self._load_edges()
        self._load_pathways()
        self._load_rules()
        self._build_indices()
        logger.info(
            "DataLoader loaded %d entities, %d edges, %d pathways, %d rules",
            len(self._entities),
            len(self._edges),
            len(self._pathways),
            len(self._rules),
        )

    def _load_entities(self) -> None:
        path = self.normalized_dir / "entities.csv"
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("entity_id"):
                    continue
                entity = self._parse_entity_row(row)
                self._entities[entity.entity_id] = entity

    @staticmethod
    def _parse_entity_row(row: Dict) -> EntityRecord:
        return EntityRecord(
            entity_id=row.get("entity_id", "").strip(),
            entity_type=row.get("entity_type", "").strip(),
            name=row.get("name", "").strip(),
            canonical_display_name=row.get("display_name", "").strip() or row.get("name", "").strip(),
            aliases=_dedupe_list(_split_list(row.get("aliases", ""))),
            default_state=row.get("default_state", "").strip(),
            allowed_states=_split_list(row.get("allowed_states", "")),
            annotation=(row.get("annotation") or "").strip(),
            pathways=row.get("pathways", "").strip(),
            subcellular_location=row.get("subcellular_location", "").strip(),
            source_database=row.get("source_database", "").strip(),
            source_id=row.get("source_id", "").strip(),
            external_ids=row.get("external_ids", "").strip(),
            is_external=str(row.get("is_external", "")).lower() == "true",
            complex_type=row.get("complex_type", "").strip(),
            components=_split_list(row.get("components", "").replace(",", "|")),
            critical_components=_split_list(row.get("critical_components", "").replace(",", "|")),
            assembly_condition=row.get("assembly_condition", "").strip(),
            notes=row.get("notes", "").strip(),
            family_key=row.get("family_key", "").strip(),
            is_exogenous=str(row.get("is_exogenous", "false")),
            merged_from=_dedupe_list(_split_list(row.get("merged_from", ""))),
        )

    def _load_edges(self) -> None:
        path = self.normalized_dir / "edges.csv"
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("source_id") or not row.get("target_id"):
                    continue
                relation_type = row.get("relation_type", "").strip()
                source_id = row["source_id"].strip()
                target_id = row["target_id"].strip()
                source_db = row.get("source_database", "").strip()
                # Add a *semantic* (derived) relation type alongside
                # the raw experimental one. EcoCyc uses ``represses``
                # for both transcriptional regulation and small-
                # molecule enzyme inhibition; the two have very
                # different biological meaning. We keep the raw
                # relation_type (with its provenance) but expose
                # ``semantic_relation_type`` for UI, fallback rules,
                # and the LLM prompt builder.
                semantic = self._derive_semantic_relation(
                    source_id=source_id,
                    target_id=target_id,
                    relation_type=relation_type,
                )
                self._edges.append(
                    EdgeRecord(
                        source_id=source_id,
                        target_id=target_id,
                        relation_type=relation_type,
                        semantic_relation_type=semantic,
                        direction=row.get("direction", "directed").strip(),
                        evidence=row.get("evidence", "").strip(),
                        source_database=source_db,
                        source_record_id=row.get("source_record_id", "").strip(),
                        notes=row.get("notes", "").strip(),
                        # Flattened-reaction payload. Older CSVs
                        # do not carry these columns; ``.get`` with
                        # a default of "" keeps the loader
                        # backwards-compatible.
                        reaction_id=row.get("reaction_id", "").strip(),
                        reactants=row.get("reactants", "").strip(),
                        products=row.get("products", "").strip(),
                        ec_number=row.get("ec_number", "").strip(),
                        pathway=row.get("pathway", "").strip(),
                        # Edge weight is a float so the influence_score
                        # can multiply it. Default 0.40 keeps older
                        # edges from vanishing in the simulation.
                        edge_weight=float(row.get("edge_weight") or 0.40),
                        string_channel=row.get("string_channel", "").strip(),
                    )
                )

    def _derive_semantic_relation(
        self,
        source_id: str,
        target_id: str,
        relation_type: str,
    ) -> str:
        """Map a raw relation to a biology-meaningful semantic name.

        The raw ``relation_type`` column is left untouched so its
        experimental provenance stays traceable. The semantic
        version is what the UI / fallback rules / LLM prompt see.
        """
        if relation_type == "represses" and self._is_small_molecule(source_id):
            return "inhibits_enzyme"
        if relation_type == "represses":
            return "represses_transcription"
        return relation_type

    def _load_pathways(self) -> None:
        path = self.normalized_dir / "pathways.csv"
        if not path.exists():
            return
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("pathway_id"):
                    continue
                rec = PathwayRecord(
                    pathway_id=row["pathway_id"].strip(),
                    pathway_name=row.get("pathway_name", "").strip(),
                    source=row.get("source", "").strip(),
                    description=row.get("description", "").strip(),
                    organism=row.get("organism", "").strip(),
                )
                self._pathways[rec.pathway_id] = rec

    def _load_rules(self) -> None:
        path = self.registry_dir / "native_rules.jsonl"
        if not path.exists():
            return
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    self._rules.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    def _build_indices(self) -> None:
        for entity in self._entities.values():
            if entity.name:
                self._name_to_ids[entity.name.lower()].add(entity.entity_id)
                self._name_index.setdefault(entity.name, []).append(entity.entity_id)
            for alias in entity.aliases:
                if alias:
                    self._alias_to_ids[alias.lower()].add(entity.entity_id)
            self._type_index[entity.entity_type].add(entity.entity_id)
        for idx, edge in enumerate(self._edges):
            self._edges_by_source[edge.source_id].append(idx)
            self._edges_by_target[edge.target_id].append(idx)
            pair = (edge.source_id, edge.target_id)
            self._edges_by_pair[pair].append(idx)

    def same_name_siblings(self, entity_id: str) -> List[Dict]:
        """Return all entities that share the same primary name.

        Same primary name across multiple entity IDs is the most
        common EcoCyc alignment quirk — different MONOMER ids often
        share a functional name. Surfacing the siblings lets the
        reviewer click through the alternatives and decide which one
        is the canonical handle.
        """
        entity = self._entities.get(entity_id)
        if entity is None or not entity.name:
            return []
        siblings: List[Dict] = []
        for sibling_id in self._name_index.get(entity.name, []):
            if sibling_id == entity_id:
                continue
            sibling = self._entities[sibling_id]
            siblings.append(
                {
                    "entity_id": sibling_id,
                    "entity_type": sibling.entity_type,
                    "source_database": sibling.source_database,
                    "annotation_length": sibling.annotation_length,
                }
            )
        return siblings

    def duplicate_name_report(self, min_count: int = 2, limit: int = 100) -> Dict:
        """Aggregate the worst duplicate-name offenders.

        Returns the top ``limit`` names that are shared by ``>= min_count``
        entities, plus a roll-up of how many total entities are affected
        by this pattern. This is the headline diagnostic for
        "EcoCyc entities with the same name but different ids".
        """
        affected_total = 0
        groups: List[Dict] = []
        for name, ids in self._name_index.items():
            if len(ids) < min_count:
                continue
            affected_total += len(ids)
            types = sorted({self._entities[eid].entity_type for eid in ids})
            dbs = sorted({self._entities[eid].source_database for eid in ids})
            groups.append(
                {
                    "name": name,
                    "entity_count": len(ids),
                    "entity_types": types,
                    "source_databases": dbs,
                    "sample_ids": ids[:6],
                }
            )
        groups.sort(key=lambda g: (-g["entity_count"], g["name"]))
        return {
            "min_count": min_count,
            "groups_returned": len(groups[:limit]),
            "affected_entity_count": affected_total,
            "groups": groups[:limit],
        }

    # ------------------------------------------------------------------
    # Read accessors
    # ------------------------------------------------------------------

    def get_entity(self, entity_id: str) -> Optional[EntityRecord]:
        return self._entities.get(entity_id)

    def search(self, query: str, limit: int = 20) -> List[EntityRecord]:
        q = (query or "").strip().lower()
        if not q:
            return []
        results: Dict[str, int] = {}
        if q in self._entities:
            results[q] = 100
        if q in self._name_to_ids:
            for eid in self._name_to_ids[q]:
                results[eid] = max(results.get(eid, 0), 95)
        if q in self._alias_to_ids:
            for eid in self._alias_to_ids[q]:
                results[eid] = max(results.get(eid, 0), 90)
        for token in q.split():
            if token in self._name_to_ids:
                for eid in self._name_to_ids[token]:
                    results.setdefault(eid, 80)
            if token in self._alias_to_ids:
                for eid in self._alias_to_ids[token]:
                    results.setdefault(eid, 70)
        for entity in self._entities.values():
            if q in entity.entity_id.lower():
                results.setdefault(entity.entity_id, 60)
            if q in entity.annotation.lower():
                results.setdefault(entity.entity_id, 50)
        ranked = sorted(results.items(), key=lambda item: (-item[1], item[0]))
        out: List[EntityRecord] = []
        for entity_id, _ in ranked[:limit]:
            entity = self._entities.get(entity_id)
            if entity:
                out.append(entity)
        return out

    def edges_of(self, entity_id: str) -> Iterable[EdgeRecord]:
        seen = set()
        for idx in self._edges_by_source.get(entity_id, []):
            if idx not in seen:
                seen.add(idx)
                yield self._edges[idx]
        for idx in self._edges_by_target.get(entity_id, []):
            if idx in seen:
                continue
            seen.add(idx)
            yield self._edges[idx]

    def edges_between(self, source_id: str, target_id: str) -> List[EdgeRecord]:
        return [self._edges[idx] for idx in self._edges_by_pair.get((source_id, target_id), [])]

    def neighbors(self, entity_id: str, hops: int = 1) -> Set[str]:
        visited: Set[str] = {entity_id}
        frontier: Set[str] = {entity_id}
        for _ in range(hops):
            next_frontier: Set[str] = set()
            for node in frontier:
                for edge in self.edges_of(node):
                    if edge.source_id not in visited:
                        next_frontier.add(edge.source_id)
                    if edge.target_id not in visited:
                        next_frontier.add(edge.target_id)
            visited.update(next_frontier)
            frontier = next_frontier
        return visited

    def reconciliation_for_entity(self, entity_id: str) -> Dict:
        """Surface cross-source edge conflicts for an entity.

        For every (source, target) pair touching this entity we list
        the contributing edges with their ``relation_type`` and
        ``source_database`` so the reviewer can spot relations that
        disagree (e.g. one source says ``activates`` while another
        says ``represses``).
        """
        pair_conflicts: List[Dict] = []
        for edge in self.edges_of(entity_id):
            pair = (edge.source_id, edge.target_id)
            for other_idx in self._edges_by_pair.get(pair, []):
                if other_idx >= len(self._edges):
                    continue
                other = self._edges[other_idx]
                same_relation = other.relation_type == edge.relation_type
                if same_relation:
                    continue
                pair_conflicts.append(
                    {
                        "source_id": pair[0],
                        "target_id": pair[1],
                        "conflicting_edges": [edge.to_dict(), other.to_dict()],
                    }
                )
        # dedupe by pair
        seen = set()
        deduped = []
        for conflict in pair_conflicts:
            key = (conflict["source_id"], conflict["target_id"])
            if key in seen:
                continue
            seen.add(key)
            deduped.append(conflict)
        by_source_db: Dict[str, int] = defaultdict(int)
        for edge in self.edges_of(entity_id):
            by_source_db[edge.source_database or "unknown"] += 1
        return {
            "entity_id": entity_id,
            "out_edge_count": len(self._edges_by_source.get(entity_id, [])),
            "in_edge_count": len(self._edges_by_target.get(entity_id, [])),
            "by_source_database": dict(sorted(by_source_db.items())),
            "cross_source_conflicts": deduped,
        }

    def _is_small_molecule(self, entity_id: str) -> bool:
        entity = self._entities.get(entity_id)
        return entity is not None and entity.entity_type == "small_molecule"

    def attach_enriched(self, enriched_by_id: Dict[str, "object"]) -> None:
        """Hook the EnrichedLoader's records into each EntityRecord.

        The diagnostic UI and the LLM prompt builder should
        preferentially show the enriched ``display_name`` /
        ``summary`` when available. We store the enriched record on
        the :class:`EntityRecord` instance so callers can ask
        ``entity.enriched`` and get the structured view.

        Passing the raw dict rather than the loader object breaks
        the circular import between this module and
        :mod:`enriched_loader`.
        """
        attached = 0
        for entity in self._entities.values():
            if entity.entity_id in enriched_by_id:
                entity.enriched = enriched_by_id[entity.entity_id]
                attached += 1
        logger.info("attached %d enriched records onto entities", attached)

    def data_quality_report(self) -> DataQualityReport:
        type_dist: Dict[str, int] = defaultdict(int)
        empty = 0
        for entity in self._entities.values():
            type_dist[entity.entity_type] += 1
            if not entity.annotation:
                empty += 1
        relation_dist: Dict[str, int] = defaultdict(int)
        db_dist: Dict[str, int] = defaultdict(int)
        for edge in self._edges:
            relation_dist[edge.relation_type or "unknown"] += 1
            db_dist[edge.source_database or "unknown"] += 1
        seen = set()
        duplicates = 0
        for edge in self._edges:
            key = (edge.source_id, edge.target_id, edge.relation_type)
            if key in seen:
                duplicates += 1
            else:
                seen.add(key)
        return DataQualityReport(
            entity_count=len(self._entities),
            edge_count=len(self._edges),
            pathway_count=len(self._pathways),
            rule_count=len(self._rules),
            type_distribution=dict(type_dist),
            relation_distribution=dict(relation_dist),
            source_database_distribution=dict(db_dist),
            empty_annotation_count=empty,
            empty_annotation_ratio=empty / max(1, len(self._entities)),
            duplicate_pairs=duplicates,
        )


def _split_list(value: str) -> List[str]:
    if not value:
        return []
    parts = [p.strip() for p in value.replace(",", "|").replace(";", "|").split("|")]
    return [p for p in parts if p]


def _dedupe_list(items: List[str]) -> List[str]:
    """Drop duplicate strings while preserving first-occurrence order.

    The EcoCyc-derived CSVs sometimes carry the same alias multiple
    times (e.g. ``aliases="b0345;lacI;lacI"``). For the diagnostic UI
    we want a clean list so the user can read it, while still showing
    them that the data has the issue via the
    ``/api/diagnostics/duplicate-names`` endpoint.
    """
    if not items:
        return []
    seen: Set[str] = set()
    out: List[str] = []
    for item in items:
        key = item.strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out
