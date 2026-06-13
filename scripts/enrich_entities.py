#!/usr/bin/env python3
"""Build enriched, traceable entity cards from normalized graph tables.

The normalized CSVs remain the canonical graph. This script creates a separate
JSONL layer that joins weak entity rows with nearby curated information such as
encoded protein function, EcoCyc comments, pathway membership, and local edge
context.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_ecocyc import clean_text, dblink_values, first, parse_dat, reaction_summary  # noqa: E402


CORE_FIELDS = [
    "entity_id",
    "entity_type",
    "display_name",
    "aliases",
    "summary",
    "functional_context",
    "biological_role",
    "subcellular_location",
    "default_state",
    "allowed_states",
    "evidence_sources",
    "source_database",
    "source_id",
    "external_ids",
    "linked_entities",
    "edge_context",
    "pathways",
    "raw_annotations",
    "quality",
]


PLACEHOLDER_PATTERNS = [
    re.compile(r"^NCBI RefSeq gene feature$", re.I),
    re.compile(r"^EcoCyc (complex|reaction|compound|protein) [A-Za-z0-9_.:+-]+$", re.I),
    re.compile(r"^KEGG compound", re.I),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=Path("data/normalized"))
    parser.add_argument("--ecocyc-dir", type=Path, default=Path("data/raw/ecocyc/current"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/enriched"))
    args = parser.parse_args()

    normalized = args.normalized_dir
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    entities = read_csv(normalized / "entities.csv")
    edges = read_csv(normalized / "edges.csv")
    pathways = {row["pathway_id"]: row for row in read_csv(normalized / "pathways.csv")}
    ecocyc_id_map = read_csv(normalized / "ecocyc_id_map.csv")

    enricher = EntityEnricher(
        entities=entities,
        edges=edges,
        pathways=pathways,
        ecocyc_id_map=ecocyc_id_map,
        ecocyc_dir=args.ecocyc_dir,
    )
    cards = enricher.build_cards()
    report = build_report(entities, cards)

    jsonl_path = output_dir / "entities_enriched.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for card in cards:
            handle.write(json.dumps(card, ensure_ascii=False, sort_keys=True) + "\n")

    lite_path = output_dir / "entities_enriched_lite.jsonl"
    with lite_path.open("w", encoding="utf-8") as handle:
        for card in cards:
            handle.write(json.dumps(lite_card(card), ensure_ascii=False, sort_keys=True) + "\n")

    summary_path = output_dir / "entities_enriched_summary.csv"
    write_summary_csv(summary_path, cards)

    report_path = output_dir / "enrichment_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {jsonl_path} rows={len(cards)}")
    print(f"wrote {lite_path} rows={len(cards)}")
    print(f"wrote {summary_path}")
    print(f"wrote {report_path}")
    print(f"informative summaries: {report['quality_after']['informative']}")
    print(f"placeholder summaries: {report['quality_after']['placeholder']}")
    return 0


class EntityEnricher:
    def __init__(
        self,
        entities: list[dict[str, str]],
        edges: list[dict[str, str]],
        pathways: dict[str, dict[str, str]],
        ecocyc_id_map: list[dict[str, str]],
        ecocyc_dir: Path,
    ) -> None:
        self.entities = entities
        self.entity_by_id = {row["entity_id"]: row for row in entities}
        self.edges = edges
        self.pathways = pathways
        self.out_edges: dict[str, list[dict[str, str]]] = defaultdict(list)
        self.in_edges: dict[str, list[dict[str, str]]] = defaultdict(list)
        for edge in edges:
            self.out_edges[edge["source_id"]].append(edge)
            self.in_edges[edge["target_id"]].append(edge)

        self.gene_to_protein = {
            edge["source_id"]: edge["target_id"]
            for edge in edges
            if edge.get("relation_type") == "encodes"
            and edge.get("source_id") in self.entity_by_id
            and edge.get("target_id") in self.entity_by_id
        }
        self.protein_to_gene: dict[str, list[str]] = defaultdict(list)
        for gene_id, protein_id in self.gene_to_protein.items():
            self.protein_to_gene[protein_id].append(gene_id)

        self.ecocyc_records = load_ecocyc_records(ecocyc_dir)
        self.ecocyc_by_entity = map_ecocyc_records_to_entities(ecocyc_id_map, self.ecocyc_records)

    def build_cards(self) -> list[dict[str, Any]]:
        return [self.build_card(row) for row in self.entities]

    def build_card(self, row: dict[str, str]) -> dict[str, Any]:
        entity_id = row["entity_id"]
        edge_context = self.edge_context(entity_id)
        linked_entities = self.linked_entities(row, edge_context)
        raw_annotations = self.raw_annotations(row, linked_entities)
        summary, functional_context, biological_role = self.enriched_text(row, linked_entities, raw_annotations, edge_context)
        summary = trim_sentence(summary, 1400)
        functional_context = trim_sentence(functional_context, 2200)
        biological_role = trim_sentence(biological_role, 1200)
        quality = {
            "raw_annotation_quality": classify_annotation(row.get("annotation", "")),
            "enriched_summary_quality": classify_annotation(summary),
            "enrichment_sources": sorted(raw_annotations.keys()),
        }
        return {
            "entity_id": entity_id,
            "entity_type": row.get("entity_type", ""),
            "display_name": row.get("name", "") or entity_id,
            "aliases": split_aliases(row.get("aliases", "")),
            "summary": summary,
            "functional_context": functional_context,
            "biological_role": biological_role,
            "subcellular_location": row.get("subcellular_location", ""),
            "default_state": row.get("default_state", ""),
            "allowed_states": split_multi(row.get("allowed_states", "")),
            "evidence_sources": evidence_sources(row, raw_annotations, edge_context),
            "source_database": row.get("source_database", ""),
            "source_id": row.get("source_id", ""),
            "external_ids": split_multi(row.get("external_ids", "")),
            "linked_entities": linked_entities,
            "edge_context": edge_context,
            "pathways": self.pathway_context(entity_id, linked_entities),
            "raw_annotations": raw_annotations,
            "quality": quality,
        }

    def linked_entities(self, row: dict[str, str], edge_context: dict[str, Any]) -> dict[str, Any]:
        entity_id = row["entity_id"]
        linked: dict[str, Any] = {}
        if row.get("entity_type") == "gene":
            protein_id = self.gene_to_protein.get(entity_id)
            if protein_id:
                linked["encoded_protein"] = entity_ref(self.entity_by_id.get(protein_id))
        elif row.get("entity_type") == "protein":
            genes = [entity_ref(self.entity_by_id.get(gene_id)) for gene_id in self.protein_to_gene.get(entity_id, [])]
            if genes:
                linked["encoding_genes"] = genes

        for key, rel in [
            ("catalyzed_reactions", "catalyzes"),
            ("component_of", "is_component_of"),
            ("critical_for", "is_critical_for"),
            ("transport_targets", "transports"),
        ]:
            values = [entity_ref(self.entity_by_id.get(edge["target_id"])) for edge in self.out_edges.get(entity_id, []) if edge["relation_type"] == rel]
            values = [item for item in values if item]
            if values:
                linked[key] = values[:50]

        if row.get("entity_type") == "reaction":
            linked["enzymes"] = edge_context.get("incoming_by_relation", {}).get("catalyzes", [])[:50]
            linked["substrates"] = edge_context.get("incoming_by_relation", {}).get("is_substrate_of", [])[:50]
            linked["products"] = edge_context.get("incoming_by_relation", {}).get("is_product_of", [])[:50]
        elif row.get("entity_type") == "small_molecule":
            linked["consumed_by_reactions"] = edge_context.get("outgoing_by_relation", {}).get("is_substrate_of", [])[:50]
            linked["produced_by_reactions"] = edge_context.get("outgoing_by_relation", {}).get("is_product_of", [])[:50]
            linked["binding_targets"] = edge_context.get("outgoing_by_relation", {}).get("binds", [])[:50]

        return {key: value for key, value in linked.items() if value}

    def raw_annotations(self, row: dict[str, str], linked_entities: dict[str, Any]) -> dict[str, Any]:
        entity_id = row["entity_id"]
        raw: dict[str, Any] = {
            "normalized_annotation": row.get("annotation", ""),
            "normalized_notes": row.get("notes", ""),
        }
        records = self.ecocyc_by_entity.get(entity_id, [])
        if records:
            raw["ecocyc_records"] = [record_summary(item["source_file"], item["ecocyc_id"], item["record"]) for item in records]

        encoded = linked_entities.get("encoded_protein")
        if isinstance(encoded, dict):
            protein = self.entity_by_id.get(encoded["entity_id"])
            if protein:
                raw["encoded_protein_annotation"] = {
                    "entity_id": protein["entity_id"],
                    "name": protein.get("name", ""),
                    "annotation": protein.get("annotation", ""),
                    "notes": protein.get("notes", ""),
                    "source_database": protein.get("source_database", ""),
                    "external_ids": protein.get("external_ids", ""),
                }
                protein_records = self.ecocyc_by_entity.get(protein["entity_id"], [])
                if protein_records:
                    raw["encoded_protein_ecocyc_records"] = [
                        record_summary(item["source_file"], item["ecocyc_id"], item["record"])
                        for item in protein_records
                    ]
        return raw

    def enriched_text(
        self,
        row: dict[str, str],
        linked_entities: dict[str, Any],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_type = row.get("entity_type", "")
        if entity_type == "gene":
            return self.gene_text(row, linked_entities, raw_annotations, edge_context)
        if entity_type in {"protein", "complex"}:
            return self.protein_or_complex_text(row, raw_annotations, edge_context)
        if entity_type == "reaction":
            return self.reaction_text(row, raw_annotations, edge_context)
        if entity_type == "small_molecule":
            return self.molecule_text(row, raw_annotations, edge_context)
        if entity_type == "rna":
            return self.generic_text(row, raw_annotations, edge_context)
        return self.generic_text(row, raw_annotations, edge_context)

    def gene_text(
        self,
        row: dict[str, str],
        linked_entities: dict[str, Any],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_id = row["entity_id"]
        name = row.get("name", "") or entity_id
        parts = [f"{name} ({entity_id}) is a gene entity."]
        functional = []
        role = []
        encoded = raw_annotations.get("encoded_protein_annotation")
        if encoded:
            protein_label = f"{encoded.get('name') or encoded['entity_id']} ({encoded['entity_id']})"
            parts.append(f"It encodes {protein_label}.")
            protein_annotation = clean_text(encoded.get("annotation", ""))
            if protein_annotation:
                parts.append(f"Encoded protein function: {protein_annotation}")
                functional.append(protein_annotation)
            protein_notes = clean_text(encoded.get("notes", ""))
            if protein_notes:
                functional.append(protein_notes)

        for record in raw_annotations.get("ecocyc_records", []):
            product = record["fields"].get("PRODUCT", [])
            synonyms = record["fields"].get("SYNONYMS", [])
            left = first_value(record["fields"].get("LEFT-END-POSITION", []))
            right = first_value(record["fields"].get("RIGHT-END-POSITION", []))
            if product:
                parts.append(f"EcoCyc product frame: {first_value(product)}.")
            if synonyms:
                parts.append(f"EcoCyc synonyms: {', '.join(synonyms[:8])}.")
            if left and right:
                parts.append(f"Genomic coordinates: {left}-{right}.")

        for record in raw_annotations.get("encoded_protein_ecocyc_records", []):
            comment = first_value(record["fields"].get("COMMENT", []))
            if comment:
                functional.append(comment)
                parts.append(f"EcoCyc protein note: {comment}")

        regulators = edge_context.get("incoming_by_relation", {})
        if regulators.get("represses"):
            role.append(f"Repressed by {format_refs(regulators['represses'], 8)}.")
        if regulators.get("activates"):
            role.append(f"Activated by {format_refs(regulators['activates'], 8)}.")
        summary = squash(" ".join(parts))
        return summary, squash(" ".join(unique_keep_order(functional))), squash(" ".join(role))

    def protein_or_complex_text(
        self,
        row: dict[str, str],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_id = row["entity_id"]
        name = row.get("name", "") or entity_id
        parts = [clean_text(row.get("annotation", ""))]
        functional = [clean_text(row.get("notes", ""))]
        role = []
        for record in raw_annotations.get("ecocyc_records", []):
            comment = first_value(record["fields"].get("COMMENT", []))
            common = first_value(record["fields"].get("COMMON-NAME", []))
            if common and common.lower() != name.lower():
                functional.append(f"EcoCyc common name: {common}.")
            if comment:
                functional.append(comment)
                parts.append(comment)
            synonyms = record["fields"].get("SYNONYMS", [])
            if synonyms:
                functional.append(f"EcoCyc synonyms: {', '.join(synonyms[:8])}.")

        outgoing = edge_context.get("outgoing_by_relation", {})
        incoming = edge_context.get("incoming_by_relation", {})
        if outgoing.get("catalyzes"):
            role.append(f"Catalyzes {format_refs(outgoing['catalyzes'], 8)}.")
        if outgoing.get("transports"):
            role.append(f"Transports {format_refs(outgoing['transports'], 8)}.")
        if outgoing.get("is_component_of"):
            role.append(f"Component of {format_refs(outgoing['is_component_of'], 8)}.")
        if incoming.get("binds"):
            role.append(f"Bound by {format_refs(incoming['binds'], 8)}.")
        if incoming.get("represses"):
            role.append(f"Repressed by {format_refs(incoming['represses'], 8)}.")
        if incoming.get("activates"):
            role.append(f"Activated by {format_refs(incoming['activates'], 8)}.")

        summary = squash(" ".join([item for item in parts if item])) or f"{name} ({entity_id}) is a {row.get('entity_type', 'entity')} entity."
        return summary, squash(" ".join(unique_keep_order(functional))), squash(" ".join(role))

    def reaction_text(
        self,
        row: dict[str, str],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_id = row["entity_id"]
        name = row.get("name", "") or entity_id
        parts = [clean_text(row.get("annotation", ""))]
        for record in raw_annotations.get("ecocyc_records", []):
            equation = reaction_summary(record["record"])
            comment = first_value(record["fields"].get("COMMENT", []))
            if equation:
                parts.append(f"EcoCyc reaction equation: {clean_text(equation)}.")
            if comment:
                parts.append(comment)
        incoming = edge_context.get("incoming_by_relation", {})
        role = []
        if incoming.get("catalyzes"):
            role.append(f"Catalyzed by {format_refs(incoming['catalyzes'], 8)}.")
        if incoming.get("is_substrate_of"):
            role.append(f"Substrates: {format_refs(incoming['is_substrate_of'], 10)}.")
        if incoming.get("is_product_of"):
            role.append(f"Products: {format_refs(incoming['is_product_of'], 10)}.")
        summary = squash(" ".join([item for item in parts if item])) or f"{name} ({entity_id}) is a reaction entity."
        return summary, summary, squash(" ".join(role))

    def molecule_text(
        self,
        row: dict[str, str],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_id = row["entity_id"]
        name = row.get("name", "") or entity_id
        parts = [clean_text(row.get("annotation", ""))]
        for record in raw_annotations.get("ecocyc_records", []):
            comment = first_value(record["fields"].get("COMMENT", []))
            common = first_value(record["fields"].get("COMMON-NAME", []))
            if common and common.lower() != name.lower():
                parts.append(f"EcoCyc common name: {common}.")
            if comment:
                parts.append(comment)
        outgoing = edge_context.get("outgoing_by_relation", {})
        role = []
        if outgoing.get("is_substrate_of"):
            role.append(f"Consumed as substrate in {len(outgoing['is_substrate_of'])} reaction(s).")
        if outgoing.get("is_product_of"):
            role.append(f"Produced in {len(outgoing['is_product_of'])} reaction(s).")
        if outgoing.get("binds"):
            role.append(f"Binds {format_refs(outgoing['binds'], 8)}.")
        summary = squash(" ".join([item for item in parts if item])) or f"{name} ({entity_id}) is a small molecule entity."
        return summary, summary, squash(" ".join(role))

    def generic_text(
        self,
        row: dict[str, str],
        raw_annotations: dict[str, Any],
        edge_context: dict[str, Any],
    ) -> tuple[str, str, str]:
        entity_id = row["entity_id"]
        name = row.get("name", "") or entity_id
        parts = [clean_text(row.get("annotation", ""))]
        for record in raw_annotations.get("ecocyc_records", []):
            comment = first_value(record["fields"].get("COMMENT", []))
            if comment:
                parts.append(comment)
        role = edge_role_sentence(edge_context)
        summary = squash(" ".join([item for item in parts if item])) or f"{name} ({entity_id}) is a {row.get('entity_type', 'entity')} entity."
        return summary, summary, role

    def edge_context(self, entity_id: str) -> dict[str, Any]:
        outgoing_by_relation = group_edge_refs(self.out_edges.get(entity_id, []), direction="out", entity_by_id=self.entity_by_id)
        incoming_by_relation = group_edge_refs(self.in_edges.get(entity_id, []), direction="in", entity_by_id=self.entity_by_id)
        return {
            "out_degree": len(self.out_edges.get(entity_id, [])),
            "in_degree": len(self.in_edges.get(entity_id, [])),
            "outgoing_relation_counts": dict(Counter(edge["relation_type"] for edge in self.out_edges.get(entity_id, []))),
            "incoming_relation_counts": dict(Counter(edge["relation_type"] for edge in self.in_edges.get(entity_id, []))),
            "outgoing_by_relation": outgoing_by_relation,
            "incoming_by_relation": incoming_by_relation,
        }

    def pathway_context(self, entity_id: str, linked_entities: dict[str, Any]) -> list[dict[str, str]]:
        pathway_ids = set()
        for edge in self.out_edges.get(entity_id, []):
            if edge["relation_type"] == "participates_in" and edge["target_id"] in self.pathways:
                pathway_ids.add(edge["target_id"])
        encoded = linked_entities.get("encoded_protein")
        if isinstance(encoded, dict):
            for edge in self.out_edges.get(encoded["entity_id"], []):
                if edge["relation_type"] == "participates_in" and edge["target_id"] in self.pathways:
                    pathway_ids.add(edge["target_id"])
        return [
            {
                "pathway_id": pathway_id,
                "pathway_name": self.pathways[pathway_id].get("pathway_name", ""),
                "source": self.pathways[pathway_id].get("source", ""),
            }
            for pathway_id in sorted(pathway_ids)
        ]


def load_ecocyc_records(ecocyc_dir: Path) -> dict[str, dict[str, dict[str, list[str]]]]:
    files = ["genes.dat", "proteins.dat", "compounds.dat", "reactions.dat", "pathways.dat", "regulation.dat"]
    return {filename: parse_dat(ecocyc_dir / filename) for filename in files}


def map_ecocyc_records_to_entities(
    id_map_rows: list[dict[str, str]],
    records_by_file: dict[str, dict[str, dict[str, list[str]]]],
) -> dict[str, list[dict[str, Any]]]:
    by_entity: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen = set()
    for row in id_map_rows:
        source_file = row.get("source_file", "")
        ecocyc_id = row.get("ecocyc_id", "")
        entity_id = row.get("entity_id", "")
        record = records_by_file.get(source_file, {}).get(ecocyc_id)
        if not record:
            continue
        key = (entity_id, source_file, ecocyc_id)
        if key in seen:
            continue
        seen.add(key)
        by_entity[entity_id].append({"source_file": source_file, "ecocyc_id": ecocyc_id, "record": record})
    return by_entity


def record_summary(source_file: str, ecocyc_id: str, record: dict[str, list[str]]) -> dict[str, Any]:
    keys = [
        "UNIQUE-ID",
        "COMMON-NAME",
        "TYPES",
        "ACCESSION-1",
        "PRODUCT",
        "GENE",
        "SYNONYMS",
        "COMMENT",
        "LEFT-END-POSITION",
        "RIGHT-END-POSITION",
        "REACTION-DIRECTION",
        "LEFT",
        "RIGHT",
    ]
    fields = {}
    for key in keys:
        values = [clean_text(item) for item in record.get(key, []) if clean_text(item)]
        if values:
            fields[key] = values
    db_links = dblink_values(record)
    if db_links:
        fields["DBLINKS"] = [f"{db}:{value}" for db, values in sorted(db_links.items()) for value in values[:8]]
    return {"source_file": source_file, "ecocyc_id": ecocyc_id, "fields": fields, "record": record}


def group_edge_refs(edges: list[dict[str, str]], direction: str, entity_by_id: dict[str, dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        other_id = edge["target_id"] if direction == "out" else edge["source_id"]
        other = entity_ref(entity_by_id.get(other_id)) or {"entity_id": other_id, "name": other_id, "entity_type": "pathway_or_external"}
        grouped[edge["relation_type"]].append(
            {
                **other,
                "evidence": edge.get("evidence", ""),
                "source_database": edge.get("source_database", ""),
                "notes": edge.get("notes", ""),
            }
        )
    for rel, values in grouped.items():
        grouped[rel] = dedupe_refs(values)
    return dict(grouped)


def entity_ref(row: dict[str, str] | None) -> dict[str, str] | None:
    if not row:
        return None
    return {
        "entity_id": row.get("entity_id", ""),
        "name": row.get("name", ""),
        "entity_type": row.get("entity_type", ""),
    }


def evidence_sources(row: dict[str, str], raw_annotations: dict[str, Any], edge_context: dict[str, Any]) -> list[str]:
    sources = set(split_multi(row.get("source_database", "")))
    for edge_group in ("outgoing_by_relation", "incoming_by_relation"):
        for refs in edge_context.get(edge_group, {}).values():
            for ref in refs:
                sources.update(split_multi(ref.get("source_database", "")))
    for record in raw_annotations.get("ecocyc_records", []):
        sources.add("EcoCyc")
    if raw_annotations.get("encoded_protein_annotation"):
        sources.add(raw_annotations["encoded_protein_annotation"].get("source_database", ""))
    for record in raw_annotations.get("encoded_protein_ecocyc_records", []):
        sources.add("EcoCyc")
    return sorted(source for source in sources if source)


def classify_annotation(text: str) -> str:
    text = clean_text(text)
    if not text:
        return "empty"
    if any(pattern.search(text) for pattern in PLACEHOLDER_PATTERNS):
        return "placeholder"
    if len(text) < 45 and not re.search(r"\b(function|cataly|regulat|transport|bind|enzyme|pathway|encod|essential)\b", text, re.I):
        return "placeholder"
    return "informative"


def build_report(entities: list[dict[str, str]], cards: list[dict[str, Any]]) -> dict[str, Any]:
    raw_quality = Counter(classify_annotation(row.get("annotation", "")) for row in entities)
    after_quality = Counter(card["quality"]["enriched_summary_quality"] for card in cards)
    by_type = Counter(card["entity_type"] for card in cards)
    raw_placeholder_by_type = Counter(row.get("entity_type", "") for row in entities if classify_annotation(row.get("annotation", "")) != "informative")
    after_placeholder_by_type = Counter(card["entity_type"] for card in cards if card["quality"]["enriched_summary_quality"] != "informative")
    gene_enriched_from_protein = sum(
        1
        for card in cards
        if card["entity_type"] == "gene" and "encoded_protein_annotation" in card["raw_annotations"]
    )
    ecocyc_record_attached = sum(1 for card in cards if card["raw_annotations"].get("ecocyc_records"))
    return {
        "entity_count": len(cards),
        "entity_types": dict(by_type),
        "quality_before": dict(raw_quality),
        "quality_after": dict(after_quality),
        "placeholder_or_empty_before_by_type": dict(raw_placeholder_by_type),
        "placeholder_or_empty_after_by_type": dict(after_placeholder_by_type),
        "gene_cards_with_encoded_protein_annotation": gene_enriched_from_protein,
        "cards_with_ecocyc_raw_records": ecocyc_record_attached,
        "example_cards": [
            {
                "entity_id": card["entity_id"],
                "entity_type": card["entity_type"],
                "display_name": card["display_name"],
                "summary": card["summary"][:500],
                "quality": card["quality"],
            }
            for card in cards
            if card["entity_id"] in {"gene.b0639", "protein.P0A752", "reaction.ecocyc.NICONUCADENYLYLTRAN-RXN", "protein.P03023"}
        ],
    }


def write_summary_csv(path: Path, cards: list[dict[str, Any]]) -> None:
    fieldnames = [
        "entity_id",
        "entity_type",
        "display_name",
        "raw_annotation_quality",
        "enriched_summary_quality",
        "evidence_sources",
        "summary",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for card in cards:
            writer.writerow(
                {
                    "entity_id": card["entity_id"],
                    "entity_type": card["entity_type"],
                    "display_name": card["display_name"],
                    "raw_annotation_quality": card["quality"]["raw_annotation_quality"],
                    "enriched_summary_quality": card["quality"]["enriched_summary_quality"],
                    "evidence_sources": "|".join(card["evidence_sources"]),
                    "summary": card["summary"],
                }
            )


def lite_card(card: dict[str, Any]) -> dict[str, Any]:
    edge_context = card.get("edge_context", {})
    return {
        "entity_id": card["entity_id"],
        "entity_type": card["entity_type"],
        "display_name": card["display_name"],
        "aliases": card["aliases"],
        "summary": card["summary"],
        "functional_context": card["functional_context"],
        "biological_role": card["biological_role"],
        "subcellular_location": card["subcellular_location"],
        "default_state": card["default_state"],
        "allowed_states": card["allowed_states"],
        "evidence_sources": card["evidence_sources"],
        "source_database": card["source_database"],
        "source_id": card["source_id"],
        "linked_entities": card["linked_entities"],
        "pathways": card["pathways"],
        "edge_context": {
            "out_degree": edge_context.get("out_degree", 0),
            "in_degree": edge_context.get("in_degree", 0),
            "outgoing_relation_counts": edge_context.get("outgoing_relation_counts", {}),
            "incoming_relation_counts": edge_context.get("incoming_relation_counts", {}),
        },
        "quality": card["quality"],
    }


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def split_multi(text: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|;]", text or "") if item.strip()]


def split_aliases(text: str) -> list[str]:
    parts: list[str] = []
    for item in re.split(r"[|;]", text or ""):
        item = item.strip()
        if not item:
            continue
        if re.fullmatch(r"[A-Za-z0-9_.-]+(?:\s+[A-Za-z0-9_.-]+){1,5}", item):
            parts.extend(item.split())
        else:
            parts.append(item)
    return unique_keep_order(parts)


def dedupe_refs(refs: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = set()
    result = []
    for ref in refs:
        key = (ref.get("entity_id", ""), ref.get("source_database", ""), ref.get("notes", ""))
        if key in seen:
            continue
        seen.add(key)
        result.append(ref)
    return result


def unique_keep_order(items: list[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        item = clean_text(item)
        folded = item.casefold()
        if not item or folded in seen:
            continue
        seen.add(folded)
        result.append(item)
    return result


def first_value(values: list[str]) -> str:
    return values[0] if values else ""


def format_refs(refs: list[dict[str, str]], limit: int) -> str:
    labels = []
    for ref in refs[:limit]:
        name = ref.get("name") or ref.get("entity_id", "")
        entity_id = ref.get("entity_id", "")
        labels.append(f"{name} ({entity_id})" if name and entity_id and name != entity_id else entity_id)
    suffix = "" if len(refs) <= limit else f", and {len(refs) - limit} more"
    return ", ".join(labels) + suffix


def edge_role_sentence(edge_context: dict[str, Any]) -> str:
    out_counts = edge_context.get("outgoing_relation_counts", {})
    in_counts = edge_context.get("incoming_relation_counts", {})
    parts = []
    if out_counts:
        parts.append("Outgoing relations: " + ", ".join(f"{key}={value}" for key, value in sorted(out_counts.items())) + ".")
    if in_counts:
        parts.append("Incoming relations: " + ", ".join(f"{key}={value}" for key, value in sorted(in_counts.items())) + ".")
    return " ".join(parts)


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", clean_text(text)).strip()


def trim_sentence(text: str, limit: int) -> str:
    text = squash(text)
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit(".", 1)[0].strip()
    if len(clipped) < limit * 0.5:
        clipped = text[:limit].rsplit(" ", 1)[0].strip()
    return clipped + "..."


if __name__ == "__main__":
    raise SystemExit(main())
