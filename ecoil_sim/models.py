from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


def split_pipe(value: str) -> List[str]:
    """Split a pipe-, semicolon-, or comma-separated value into a clean list.

    The normalized CSV files mix separators depending on the upstream
    source (KEGG uses ``;``, UniProt uses ``;``, NCBI uses ``|``), so
    we accept any of them and trim trailing punctuation.
    """
    if not value:
        return []
    parts = [part.strip() for part in value.replace(",", "|").replace(";", "|").split("|")]
    cleaned: List[str] = []
    for part in parts:
        part = part.strip().strip(";,").strip()
        if part:
            cleaned.append(part)
    return cleaned


def alias_list(value: str) -> List[str]:
    """Parse the aliases column, preserving multi-word aliases.

    The aliases column is usually space-joined single-token synonyms
    ("lacI b0345 JW0336"), but some sources contribute multi-word aliases
    ("DNA gyrase subunit A"). We split on the real separators (| ; ,) to keep
    multi-word chunks whole, then ALSO add each chunk's individual word tokens
    so single-token lookups ("lacI", "b0345") still resolve. Dedup, order
    preserved.
    """
    chunks = split_pipe(value)
    out: List[str] = []
    seen = set()

    def _add(item: str) -> None:
        item = item.strip()
        if item and item.lower() not in seen:
            seen.add(item.lower())
            out.append(item)

    for chunk in chunks:
        _add(chunk)
        for token in chunk.split():
            _add(token)
    return out


@dataclass(frozen=True)
class Entity:
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
    is_external: bool = False
    complex_type: str = ""
    is_virtual: bool = False
    components: List[str] = field(default_factory=list)
    critical_components: List[str] = field(default_factory=list)
    assembly_condition: str = ""
    notes: str = ""

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Entity":
        return cls(
            entity_id=row.get("entity_id", ""),
            entity_type=row.get("entity_type", ""),
            name=row.get("name", ""),
            aliases=alias_list(row.get("aliases", "")),
            default_state=row.get("default_state", ""),
            allowed_states=split_pipe(row.get("allowed_states", "")),
            annotation=row.get("annotation", ""),
            pathways=row.get("pathways", ""),
            subcellular_location=row.get("subcellular_location", ""),
            source_database=row.get("source_database", ""),
            source_id=row.get("source_id", ""),
            external_ids=row.get("external_ids", ""),
            is_external=row.get("is_external", "").lower() == "true",
            complex_type=row.get("complex_type", ""),
            is_virtual=row.get("is_virtual", "").lower() == "true",
            components=split_pipe(row.get("components", "").replace(",", "|")),
            critical_components=split_pipe(row.get("critical_components", "").replace(",", "|")),
            assembly_condition=row.get("assembly_condition", ""),
            notes=row.get("notes", ""),
        )


@dataclass(frozen=True)
class Edge:
    source_id: str
    relation_type: str
    target_id: str
    direction: str
    evidence: str
    source_database: str
    source_record_id: str
    notes: str = ""
    # Optional per-edge confidence (0..1), present on the simulation baseline
    # (e.g. STRING score-derived weights). 0.0 means "use the relation-type
    # default weight". ``string_channel`` records the STRING evidence channel
    # (experimental / database / coexpression) when applicable.
    edge_weight: float = 0.0
    string_channel: str = ""

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Edge":
        raw_weight = (row.get("edge_weight") or "").strip()
        try:
            edge_weight = float(raw_weight) if raw_weight else 0.0
        except ValueError:
            edge_weight = 0.0
        return cls(
            source_id=row.get("source_id", ""),
            relation_type=row.get("relation_type", ""),
            target_id=row.get("target_id", ""),
            direction=row.get("direction", ""),
            evidence=row.get("evidence", ""),
            source_database=row.get("source_database", ""),
            source_record_id=row.get("source_record_id", ""),
            notes=row.get("notes", ""),
            edge_weight=edge_weight,
            string_channel=(row.get("string_channel") or "").strip(),
        )


@dataclass(frozen=True)
class Pathway:
    pathway_id: str
    pathway_name: str
    source: str
    description: str
    organism: str

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Pathway":
        return cls(
            pathway_id=row.get("pathway_id", ""),
            pathway_name=row.get("pathway_name", ""),
            source=row.get("source", ""),
            description=row.get("description", ""),
            organism=row.get("organism", ""),
        )


@dataclass(frozen=True)
class Rule:
    rule_id: str
    priority_class: str
    rule_type: str
    source: Dict[str, Any]
    species_scope: str
    participants: Dict[str, Any]
    conditions: Dict[str, Any]
    effects: List[Dict[str, Any]]
    constraints: Dict[str, Any]
    confidence: str
    notes: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Rule":
        return cls(
            rule_id=data["rule_id"],
            priority_class=data["priority_class"],
            rule_type=data["rule_type"],
            source=data.get("source", {}),
            species_scope=data.get("species_scope", ""),
            participants=data.get("participants", {}),
            conditions=data.get("conditions", {}),
            effects=data.get("effects", []),
            constraints=data.get("constraints", {}),
            confidence=data.get("confidence", "low"),
            notes=data.get("notes", ""),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "priority_class": self.priority_class,
            "rule_type": self.rule_type,
            "source": self.source,
            "species_scope": self.species_scope,
            "participants": self.participants,
            "conditions": self.conditions,
            "effects": self.effects,
            "constraints": self.constraints,
            "confidence": self.confidence,
            "notes": self.notes,
        }


@dataclass
class AgentState:
    entity_id: str
    state: str
    abundance_label: str = ""
    efficiency: str = ""
    changed: bool = False
    reason: str = ""
    changed_neighbors: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "state": self.state,
            "abundance_label": self.abundance_label,
            "efficiency": self.efficiency,
            "changed": self.changed,
            "reason": self.reason,
            "changed_neighbors": self.changed_neighbors,
            "metadata": self.metadata,
        }
