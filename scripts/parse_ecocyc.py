#!/usr/bin/env python3
"""Normalize licensed EcoCyc flat files into E.coil CSV layers.

The parser is intentionally conservative: it maps EcoCyc frames to existing
UniProt/RefSeq/KEGG entity IDs whenever possible, and creates ecocyc-prefixed
entities only for frames that are not already represented.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ENTITY_FIELDS = [
    "entity_id",
    "entity_type",
    "name",
    "aliases",
    "default_state",
    "allowed_states",
    "annotation",
    "pathways",
    "subcellular_location",
    "source_database",
    "source_id",
    "external_ids",
    "is_external",
    "complex_type",
    "is_virtual",
    "components",
    "critical_components",
    "assembly_condition",
    "notes",
]

EDGE_FIELDS = [
    "source_id",
    "relation_type",
    "target_id",
    "direction",
    "evidence",
    "source_database",
    "source_record_id",
    "notes",
]

PATHWAY_FIELDS = ["pathway_id", "pathway_name", "source", "description", "organism"]
ID_MAP_FIELDS = ["ecocyc_id", "entity_id", "entity_type", "mapping_method", "source_file"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ecocyc-dir", default="data/raw/ecocyc/current")
    parser.add_argument("--normalized-dir", default="data/normalized")
    parser.add_argument("--output-prefix", default="ecocyc")
    parser.add_argument("--merge", action="store_true", help="Merge EcoCyc outputs into main normalized CSV files.")
    args = parser.parse_args()

    ecocyc_dir = Path(args.ecocyc_dir)
    normalized_dir = Path(args.normalized_dir)
    normalized_dir.mkdir(parents=True, exist_ok=True)

    existing_entities = read_csv(normalized_dir / "entities.csv")
    existing_edges = read_csv(normalized_dir / "edges.csv")
    existing_pathways = read_csv(normalized_dir / "pathways.csv")
    context = ExistingContext(existing_entities, existing_edges)

    parser_obj = EcoCycNormalizer(ecocyc_dir, context)
    outputs = parser_obj.build()

    entity_path = normalized_dir / f"{args.output_prefix}_entities.csv"
    edge_path = normalized_dir / f"{args.output_prefix}_edges.csv"
    pathway_path = normalized_dir / f"{args.output_prefix}_pathways.csv"
    id_map_path = normalized_dir / f"{args.output_prefix}_id_map.csv"
    report_path = normalized_dir / f"{args.output_prefix}_parse_report.json"

    write_csv(entity_path, ENTITY_FIELDS, outputs.entities)
    write_csv(edge_path, EDGE_FIELDS, outputs.edges)
    write_csv(pathway_path, PATHWAY_FIELDS, outputs.pathways)
    write_csv(id_map_path, ID_MAP_FIELDS, outputs.id_map)
    report = outputs.report
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {entity_path} rows={len(outputs.entities)}")
    print(f"wrote {edge_path} rows={len(outputs.edges)}")
    print(f"wrote {pathway_path} rows={len(outputs.pathways)}")
    print(f"wrote {id_map_path} rows={len(outputs.id_map)}")
    print(f"wrote {report_path}")

    if args.merge:
        merge_main(normalized_dir, existing_entities, existing_edges, existing_pathways, outputs)


class ExistingContext:
    def __init__(self, entities: list[dict[str, str]], edges: list[dict[str, str]]) -> None:
        self.entity_ids = {row["entity_id"] for row in entities}
        self.gene_to_protein: dict[str, str] = {}
        self.external_index: dict[tuple[str, str], str] = {}
        for row in edges:
            if row.get("relation_type") == "encodes":
                self.gene_to_protein.setdefault(row.get("source_id", ""), row.get("target_id", ""))
        for row in entities:
            entity_id = row.get("entity_id", "")
            source_db = row.get("source_database", "")
            source_id = row.get("source_id", "")
            if source_db and source_id:
                self.external_index[(source_db.upper(), source_id)] = entity_id
            for item in re.split(r"[|;]", row.get("external_ids", "")):
                if ":" not in item:
                    continue
                db, value = item.split(":", 1)
                value = value.strip()
                if value:
                    self.external_index[(db.upper(), value)] = entity_id


class Outputs:
    def __init__(self) -> None:
        self.entities: list[dict[str, str]] = []
        self.edges: list[dict[str, str]] = []
        self.pathways: list[dict[str, str]] = []
        self.id_map: list[dict[str, str]] = []
        self.report: dict[str, Any] = {}


class EcoCycNormalizer:
    def __init__(self, ecocyc_dir: Path, context: ExistingContext) -> None:
        self.dir = ecocyc_dir
        self.context = context
        self.genes = parse_dat(ecocyc_dir / "genes.dat")
        self.proteins = parse_dat(ecocyc_dir / "proteins.dat")
        self.compounds = parse_dat(ecocyc_dir / "compounds.dat")
        self.reactions = parse_dat(ecocyc_dir / "reactions.dat")
        self.enzrxns = parse_dat(ecocyc_dir / "enzrxns.dat")
        self.pathways = parse_dat(ecocyc_dir / "pathways.dat")
        self.regulation = parse_dat(ecocyc_dir / "regulation.dat")
        self.protligand = parse_dat(ecocyc_dir / "protligandcplxes.dat")
        self.protcplx_rows = parse_col(ecocyc_dir / "protcplxs.col")
        self.transporter_rows = parse_col(ecocyc_dir / "transporters.col")

        self.gene_frame_to_entity: dict[str, str] = {}
        self.product_frame_to_gene: dict[str, str] = {}
        self.protein_frame_to_entity: dict[str, str] = {}
        self.compound_frame_to_entity: dict[str, str] = {}
        self.reaction_frame_to_entity: dict[str, str] = {}
        self.pathway_frame_to_entity: dict[str, str] = {}
        self.enzrxn_to_reaction: dict[str, str] = {}
        self.enzrxn_to_enzyme: dict[str, str] = {}
        self.compound_name_index: dict[str, str] = {}

    def build(self) -> Outputs:
        outputs = Outputs()
        self._build_maps(outputs)
        outputs.pathways = self._build_pathways()
        outputs.entities = self._build_entities()
        outputs.edges = self._build_edges()
        outputs.id_map = dedupe_rows(outputs.id_map, ID_MAP_FIELDS)
        outputs.entities = dedupe_rows(outputs.entities, ENTITY_FIELDS, key_fields=["entity_id"])
        outputs.edges = dedupe_rows(
            outputs.edges,
            EDGE_FIELDS,
            key_fields=["source_id", "relation_type", "target_id", "source_database", "source_record_id", "notes"],
        )
        outputs.pathways = dedupe_rows(outputs.pathways, PATHWAY_FIELDS, key_fields=["pathway_id"])
        outputs.report = self._report(outputs)
        return outputs

    def _build_maps(self, outputs: Outputs) -> None:
        for uid, record in self.genes.items():
            accession = first(record, "ACCESSION-1")
            entity_id = f"gene.{accession}" if re.fullmatch(r"b\d{4}", accession or "") else ""
            if entity_id and entity_id in self.context.entity_ids:
                self.gene_frame_to_entity[uid] = entity_id
                self._map(outputs, uid, entity_id, "gene", "ACCESSION-1", "genes.dat")
            product = first(record, "PRODUCT")
            if product and entity_id:
                self.product_frame_to_gene[product] = entity_id

        for uid, record in self.compounds.items():
            dblink = dblink_values(record)
            kegg_id = first_match(dblink.get("LIGAND-CPD", []), r"C\d{5}")
            entity_id = f"molecule.{kegg_id}" if kegg_id and f"molecule.{kegg_id}" in self.context.entity_ids else ecocyc_id("molecule", uid)
            self.compound_frame_to_entity[uid] = entity_id
            method = "DBLINKS LIGAND-CPD" if entity_id.startswith("molecule.C") else "EcoCyc compound fallback"
            self._map(outputs, uid, entity_id, "small_molecule", method, "compounds.dat")

        for uid, record in self.proteins.items():
            is_complex = is_complex_record(uid, record)
            dblink = dblink_values(record)
            uniprot = first_match(dblink.get("UNIPROT", []) + dblink.get("ALPHAFOLD", []) + dblink.get("SMR", []), r"[A-Z0-9]{6,10}")
            entity_id = ""
            if uniprot and f"protein.{uniprot}" in self.context.entity_ids:
                entity_id = f"protein.{uniprot}"
                method = "DBLINKS UNIPROT"
            else:
                gene_frame = first(record, "GENE")
                gene_id = self.gene_frame_to_entity.get(gene_frame) or self.product_frame_to_gene.get(uid, "")
                if gene_id and self.context.gene_to_protein.get(gene_id) in self.context.entity_ids:
                    entity_id = self.context.gene_to_protein[gene_id]
                    method = "EcoCyc gene PRODUCT to existing encodes"
                elif is_complex:
                    entity_id = ecocyc_id("complex", uid)
                    method = "EcoCyc protein complex"
                else:
                    entity_id = ecocyc_id("protein", uid)
                    method = "EcoCyc protein fallback"
            self.protein_frame_to_entity[uid] = entity_id
            self._map(outputs, uid, entity_id, "complex" if is_complex else "protein", method, "proteins.dat")

        for row in self.protcplx_rows:
            uid = row.get("UNIQUE-ID", "")
            if uid and uid not in self.protein_frame_to_entity:
                entity_id = ecocyc_id("complex", uid)
                self.protein_frame_to_entity[uid] = entity_id
                self._map(outputs, uid, entity_id, "complex", "EcoCyc protcplxs.col", "protcplxs.col")

        for uid in self.protligand:
            if uid and uid not in self.protein_frame_to_entity:
                entity_id = ecocyc_id("complex", uid)
                self.protein_frame_to_entity[uid] = entity_id
                self._map(outputs, uid, entity_id, "complex", "EcoCyc protein-ligand complex", "protligandcplxes.dat")

        for uid in self.reactions:
            entity_id = f"reaction.{uid}" if uid in self.context.entity_ids else ecocyc_id("reaction", uid)
            self.reaction_frame_to_entity[uid] = entity_id
            self._map(outputs, uid, entity_id, "reaction", "EcoCyc reaction", "reactions.dat")

        for uid in self.pathways:
            entity_id = f"ecocyc.{uid}"
            self.pathway_frame_to_entity[uid] = entity_id
            self._map(outputs, uid, entity_id, "pathway", "EcoCyc pathway", "pathways.dat")

        for uid, record in self.enzrxns.items():
            rxn = first(record, "REACTION")
            enzyme = first(record, "ENZYME")
            if rxn:
                self.enzrxn_to_reaction[uid] = self.reaction_frame_to_entity.get(rxn, ecocyc_id("reaction", rxn))
            if enzyme:
                self.enzrxn_to_enzyme[uid] = self.protein_frame_to_entity.get(enzyme, ecocyc_id("protein", enzyme))

        for uid, entity_id in self.compound_frame_to_entity.items():
            record = self.compounds[uid]
            names = [first(record, "COMMON-NAME"), *record.get("SYNONYMS", []), uid]
            for name in names:
                norm = normalize_name(name)
                if norm:
                    self.compound_name_index.setdefault(norm, entity_id)

    def _build_pathways(self) -> list[dict[str, str]]:
        rows = []
        for uid, record in self.pathways.items():
            rows.append(
                {
                    "pathway_id": self.pathway_frame_to_entity[uid],
                    "pathway_name": clean_text(first(record, "COMMON-NAME") or uid),
                    "source": "EcoCyc",
                    "description": trim(clean_text(first(record, "COMMENT")), 1000),
                    "organism": "Escherichia coli K-12 MG1655",
                }
            )
        return rows

    def _build_entities(self) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for uid, record in self.compounds.items():
            entity_id = self.compound_frame_to_entity[uid]
            if entity_id in self.context.entity_ids:
                continue
            rows.append(
                entity_row(
                    entity_id=entity_id,
                    entity_type="small_molecule",
                    name=clean_text(first(record, "COMMON-NAME") or uid),
                    aliases="|".join(clean_text(v) for v in record.get("SYNONYMS", [])[:20]),
                    default_state="low",
                    allowed_states="absent|low|medium|high",
                    annotation=trim(clean_text(first(record, "COMMENT")) or f"EcoCyc compound {uid}", 1800),
                    source_id=uid,
                    external_ids=external_ids(record, uid),
                    notes=trim(clean_text(first(record, "CHEMICAL-FORMULA")), 300),
                )
            )

        for uid, record in self.reactions.items():
            entity_id = self.reaction_frame_to_entity[uid]
            if entity_id in self.context.entity_ids:
                continue
            rows.append(
                entity_row(
                    entity_id=entity_id,
                    entity_type="reaction",
                    name=clean_text(first(record, "COMMON-NAME") or first(record, "SYSTEMATIC-NAME") or uid),
                    aliases="|".join(record.get("SYNONYMS", [])[:20]),
                    default_state="active",
                    allowed_states="active|blocked",
                    annotation=trim(clean_text(first(record, "COMMENT")) or reaction_summary(record), 1800),
                    pathways="|".join(self.pathway_frame_to_entity.get(p, f"ecocyc.{p}") for p in record.get("IN-PATHWAY", [])),
                    subcellular_location="|".join(record.get("RXN-LOCATIONS", [])),
                    source_id=uid,
                    external_ids=external_ids(record, uid),
                    is_virtual="true",
                    notes=reaction_summary(record),
                )
            )

        seen_complexes = {
            uid for uid, record in self.proteins.items()
            if is_complex_record(uid, record)
        } | {row.get("UNIQUE-ID", "") for row in self.protcplx_rows if row.get("UNIQUE-ID")} | set(self.protligand)
        for uid in sorted(seen_complexes):
            record = self.proteins.get(uid) or self.protligand.get(uid) or {}
            entity_id = self.protein_frame_to_entity.get(uid, ecocyc_id("complex", uid))
            if entity_id in self.context.entity_ids:
                continue
            components = self._components_for(uid, record)
            component_ids = [entity for entity, _coeff in components if entity]
            rows.append(
                entity_row(
                    entity_id=entity_id,
                    entity_type="complex",
                    name=clean_text(first(record, "COMMON-NAME") or name_from_col(self.protcplx_rows, uid) or uid),
                    aliases="|".join(record.get("SYNONYMS", [])[:20]),
                    default_state="active",
                    allowed_states="active|impaired|disrupted|assembled|disassembled|inhibited",
                    annotation=trim(clean_text(first(record, "COMMENT")) or f"EcoCyc complex {uid}", 1800),
                    pathways="",
                    subcellular_location="|".join(record.get("LOCATIONS", [])),
                    source_id=uid,
                    external_ids=external_ids(record, uid),
                    complex_type=complex_type(record, uid),
                    is_virtual="true" if complex_type(record, uid) == "structural" else "false",
                    components="|".join(component_ids),
                    critical_components="",
                    assembly_condition="EcoCyc component composition",
                    notes=component_note(components),
                )
            )

        for uid, record in self.proteins.items():
            entity_id = self.protein_frame_to_entity[uid]
            if entity_id in self.context.entity_ids or entity_id.startswith("complex."):
                continue
            rows.append(
                entity_row(
                    entity_id=entity_id,
                    entity_type="protein",
                    name=clean_text(first(record, "ABBREV-NAME") or first(record, "COMMON-NAME") or uid),
                    aliases="|".join(record.get("SYNONYMS", [])[:20]),
                    default_state="active",
                    allowed_states="active|inhibited|degraded|sequestered",
                    annotation=trim(clean_text(first(record, "COMMENT")) or f"EcoCyc protein {uid}", 1800),
                    subcellular_location="|".join(record.get("LOCATIONS", [])),
                    source_id=uid,
                    external_ids=external_ids(record, uid),
                    notes=clean_text(first(record, "COMMON-NAME") or ""),
                )
            )
        return rows

    def _build_edges(self) -> list[dict[str, str]]:
        rows: list[dict[str, str]] = []
        for uid, record in self.genes.items():
            gene_id = self.gene_frame_to_entity.get(uid)
            product = first(record, "PRODUCT")
            product_id = self.protein_frame_to_entity.get(product)
            if gene_id and product_id:
                rows.append(edge(gene_id, "encodes", product_id, uid, "EcoCyc gene PRODUCT"))

        for uid, record in self.reactions.items():
            reaction_id = self.reaction_frame_to_entity[uid]
            for left in record.get("LEFT", []):
                molecule = self.compound_frame_to_entity.get(left)
                if molecule:
                    rows.append(edge(molecule, "is_substrate_of", reaction_id, uid, "EcoCyc reaction LEFT"))
            for right in record.get("RIGHT", []):
                molecule = self.compound_frame_to_entity.get(right)
                if molecule:
                    rows.append(edge(molecule, "is_product_of", reaction_id, uid, "EcoCyc reaction RIGHT"))
            for pathway in record.get("IN-PATHWAY", []):
                rows.append(edge(reaction_id, "participates_in", self.pathway_frame_to_entity.get(pathway, f"ecocyc.{pathway}"), uid, "EcoCyc reaction IN-PATHWAY"))

        for uid, record in self.enzrxns.items():
            enzyme = self.protein_frame_to_entity.get(first(record, "ENZYME"))
            reaction_id = self.reaction_frame_to_entity.get(first(record, "REACTION"))
            if enzyme and reaction_id:
                rows.append(edge(enzyme, "catalyzes", reaction_id, uid, "EcoCyc enzymatic reaction"))
            for cofactor in record.get("COFACTORS", []):
                molecule = self.compound_frame_to_entity.get(cofactor)
                if molecule and enzyme:
                    rows.append(edge(molecule, "binds", enzyme, uid, "EcoCyc enzymatic reaction cofactor"))

        for uid in sorted({*self.proteins.keys(), *self.protligand.keys()}):
            record = self.proteins.get(uid) or self.protligand.get(uid) or {}
            complex_id = self.protein_frame_to_entity.get(uid)
            if not complex_id or not complex_id.startswith("complex."):
                continue
            for component_id, coeff in self._components_for(uid, record):
                if component_id:
                    rows.append(edge(component_id, "is_component_of", complex_id, uid, f"EcoCyc component coefficient={coeff or ''}"))

        for row in self.protcplx_rows:
            uid = row.get("UNIQUE-ID", "")
            complex_id = self.protein_frame_to_entity.get(uid)
            for component_id, coeff in parse_subunit_composition(row.get("SUBUNIT-COMPOSITION", ""), self.protein_frame_to_entity):
                if component_id and complex_id:
                    rows.append(edge(component_id, "is_component_of", complex_id, uid, f"EcoCyc protcplxs.col coefficient={coeff or ''}"))

        for row in self.transporter_rows:
            transporter = self.protein_frame_to_entity.get(row.get("UNIQUE-ID", ""))
            if not transporter:
                continue
            for component_id, coeff in parse_subunit_composition(row.get("SUBUNIT-COMPOSITION", ""), self.protein_frame_to_entity):
                if component_id and transporter.startswith("complex."):
                    rows.append(edge(component_id, "is_component_of", transporter, row.get("UNIQUE-ID", ""), f"EcoCyc transporter component coefficient={coeff or ''}"))
            for molecule in self._transported_molecules(row.get("REACTION-EQUATION", "")):
                rows.append(edge(transporter, "transports", molecule, row.get("UNIQUE-ID", ""), "EcoCyc transporters.col equation"))

        for uid, record in self.regulation.items():
            relation = {"+" : "activates", "-" : "represses"}.get(first(record, "MODE"))
            if not relation:
                continue
            regulator = self._map_any(first(record, "REGULATOR"))
            regulated = self._map_regulated(first(record, "REGULATED-ENTITY"))
            if regulator and regulated:
                rows.append(edge(regulator, relation, regulated, uid, f"EcoCyc regulation TYPES={';'.join(record.get('TYPES', []))}"))

        for uid, record in self.pathways.items():
            pathway_id = self.pathway_frame_to_entity[uid]
            for reaction_frame in record.get("REACTION-LIST", []):
                reaction_id = self.reaction_frame_to_entity.get(strip_quotes(reaction_frame))
                if reaction_id:
                    rows.append(edge(reaction_id, "participates_in", pathway_id, uid, "EcoCyc pathway REACTION-LIST"))
        return rows

    def _components_for(self, uid: str, record: dict[str, list[str]]) -> list[tuple[str, str]]:
        components = []
        coeffs = record.get("^COEFFICIENT", [])
        for ix, component in enumerate(record.get("COMPONENTS", [])):
            component_id = self._map_any(component)
            coeff = coeffs[ix] if ix < len(coeffs) else ""
            if component_id:
                components.append((component_id, coeff))
        if not components:
            for row in self.protcplx_rows:
                if row.get("UNIQUE-ID") == uid:
                    components.extend(parse_subunit_composition(row.get("SUBUNIT-COMPOSITION", ""), self.protein_frame_to_entity))
        return components

    def _map_any(self, frame: str) -> str:
        frame = strip_quotes(frame)
        return (
            self.protein_frame_to_entity.get(frame)
            or self.compound_frame_to_entity.get(frame)
            or self.gene_frame_to_entity.get(frame)
            or self.reaction_frame_to_entity.get(frame)
            or self.enzrxn_to_reaction.get(frame)
            or ""
        )

    def _map_regulated(self, frame: str) -> str:
        frame = strip_quotes(frame)
        if frame in self.enzrxn_to_reaction:
            return self.enzrxn_to_reaction[frame]
        return self._map_any(frame)

    def _transported_molecules(self, equation: str) -> list[str]:
        found = []
        for token in re.split(r"\s+\+|\+|\s+<--?>|\s+--?>|\s+<-->\s+", clean_text(equation)):
            token = re.sub(r"\[[^\]]+\]", "", token).strip()
            token = re.sub(r"\s+", " ", token)
            if not token or token in {"ATP", "ADP", "H2O", "H+", "phosphate"}:
                continue
            entity_id = self.compound_name_index.get(normalize_name(token))
            if entity_id:
                found.append(entity_id)
        return sorted(set(found))

    def _map(self, outputs: Outputs, ecocyc_uid: str, entity_id: str, entity_type: str, method: str, source_file: str) -> None:
        if not ecocyc_uid or not entity_id:
            return
        outputs.id_map.append(
            {
                "ecocyc_id": ecocyc_uid,
                "entity_id": entity_id,
                "entity_type": entity_type,
                "mapping_method": method,
                "source_file": source_file,
            }
        )

    def _report(self, outputs: Outputs) -> dict[str, Any]:
        return {
            "input_records": {
                "genes": len(self.genes),
                "proteins": len(self.proteins),
                "compounds": len(self.compounds),
                "reactions": len(self.reactions),
                "enzrxns": len(self.enzrxns),
                "pathways": len(self.pathways),
                "regulation": len(self.regulation),
                "protligandcplxes": len(self.protligand),
                "protcplxs_col": len(self.protcplx_rows),
                "transporters_col": len(self.transporter_rows),
            },
            "outputs": {
                "entities": len(outputs.entities),
                "edges": len(outputs.edges),
                "pathways": len(outputs.pathways),
                "id_mappings": len(outputs.id_map),
            },
            "entities_by_type": dict(Counter(row["entity_type"] for row in outputs.entities)),
            "edges_by_relation": dict(Counter(row["relation_type"] for row in outputs.edges)),
            "id_map_methods": dict(Counter(row["mapping_method"] for row in outputs.id_map)),
        }


def parse_dat(path: Path) -> dict[str, dict[str, list[str]]]:
    records: dict[str, dict[str, list[str]]] = {}
    if not path.exists():
        return records
    current: dict[str, list[str]] = defaultdict(list)
    uid = ""
    last_key = ""
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        if line == "//":
            if uid:
                records[uid] = dict(current)
            current = defaultdict(list)
            uid = ""
            last_key = ""
            continue
        if line.startswith("/") and last_key:
            current[last_key][-1] = current[last_key][-1] + "\n" + line.lstrip("/")
            continue
        if " - " not in line:
            continue
        key, value = line.split(" - ", 1)
        key = key.strip()
        value = value.strip()
        current[key].append(value)
        last_key = key
        if key == "UNIQUE-ID":
            uid = value
    if uid:
        records[uid] = dict(current)
    return records


def parse_col(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    lines = [line.rstrip("\n") for line in path.open(encoding="utf-8", errors="replace") if line.strip() and not line.startswith("#")]
    if not lines:
        return []
    reader = csv.DictReader(lines, delimiter="\t")
    return [{key: value for key, value in row.items() if key} for row in reader]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fieldnames} for row in rows)


def merge_main(normalized_dir: Path, entities: list[dict[str, str]], edges: list[dict[str, str]], pathways: list[dict[str, str]], outputs: Outputs) -> None:
    backup(normalized_dir / "entities.csv")
    backup(normalized_dir / "edges.csv")
    backup(normalized_dir / "pathways.csv")
    merged_entities = dedupe_rows([*entities, *outputs.entities], ENTITY_FIELDS, key_fields=["entity_id"])
    merged_edges = dedupe_rows(
        [*edges, *outputs.edges],
        EDGE_FIELDS,
        key_fields=["source_id", "relation_type", "target_id", "source_database", "source_record_id", "notes"],
    )
    merged_pathways = dedupe_rows([*pathways, *outputs.pathways], PATHWAY_FIELDS, key_fields=["pathway_id"])
    write_csv(normalized_dir / "entities.csv", ENTITY_FIELDS, merged_entities)
    write_csv(normalized_dir / "edges.csv", EDGE_FIELDS, merged_edges)
    write_csv(normalized_dir / "pathways.csv", PATHWAY_FIELDS, merged_pathways)
    print(f"merged data/normalized/entities.csv rows={len(merged_entities)}")
    print(f"merged data/normalized/edges.csv rows={len(merged_edges)}")
    print(f"merged data/normalized/pathways.csv rows={len(merged_pathways)}")


def backup(path: Path) -> None:
    if not path.exists():
        return
    backup_path = path.with_suffix(path.suffix + ".pre_ecocyc")
    if not backup_path.exists():
        backup_path.write_bytes(path.read_bytes())


def entity_row(**kwargs: str) -> dict[str, str]:
    row = {field: "" for field in ENTITY_FIELDS}
    row.update(
        {
            "source_database": "EcoCyc",
            "is_external": "false",
        }
    )
    row.update(kwargs)
    return row


def edge(source: str, relation: str, target: str, record_id: str, notes: str) -> dict[str, str]:
    return {
        "source_id": source,
        "relation_type": relation,
        "target_id": target,
        "direction": "directed",
        "evidence": "database",
        "source_database": "EcoCyc",
        "source_record_id": record_id,
        "notes": notes,
    }


def first(record: dict[str, list[str]], key: str) -> str:
    values = record.get(key, [])
    return values[0] if values else ""


def dblink_values(record: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for line in record.get("DBLINKS", []):
        match = re.match(r"\(([A-Za-z0-9_-]+)\s+\"([^\"]+)\"", line)
        if match:
            result[match.group(1).upper()].append(match.group(2))
    return dict(result)


def first_match(values: list[str], pattern: str) -> str:
    for value in values:
        match = re.search(pattern, value)
        if match:
            return match.group(0)
    return ""


def external_ids(record: dict[str, list[str]], uid: str) -> str:
    items = [f"EcoCyc:{uid}"]
    for db, values in dblink_values(record).items():
        for value in values[:8]:
            items.append(f"{db}:{value}")
    return "|".join(items)


def is_complex_record(uid: str, record: dict[str, list[str]]) -> bool:
    types = set(record.get("TYPES", []))
    return "Protein-Complexes" in types or bool(record.get("COMPONENTS")) or uid.endswith("-CPLX") or uid.startswith("CPLX")


def complex_type(record: dict[str, list[str]], uid: str) -> str:
    text = " ".join([uid, first(record, "COMMON-NAME"), first(record, "COMMENT")]).lower()
    if uid.startswith("PC") or any(word in text for word in ["transcription", "dna-binding", "regulator", "repressor", "activator"]):
        return "regulatory"
    return "structural"


def parse_subunit_composition(text: str, protein_map: dict[str, str]) -> list[tuple[str, str]]:
    components = []
    for part in (text or "").split(","):
        part = part.strip()
        if not part:
            continue
        match = re.match(r"(?:(\d+)\*)?(.+)", part)
        if not match:
            continue
        coeff = match.group(1) or ""
        frame = match.group(2).strip()
        entity_id = protein_map.get(frame)
        if entity_id:
            components.append((entity_id, coeff))
    return components


def name_from_col(rows: list[dict[str, str]], uid: str) -> str:
    for row in rows:
        if row.get("UNIQUE-ID") == uid:
            return clean_text(row.get("NAME", ""))
    return ""


def component_note(components: list[tuple[str, str]]) -> str:
    return "|".join(f"{coeff}*{entity}" if coeff else entity for entity, coeff in components)


def reaction_summary(record: dict[str, list[str]]) -> str:
    left = " + ".join(record.get("LEFT", []))
    right = " + ".join(record.get("RIGHT", []))
    direction = first(record, "REACTION-DIRECTION")
    if left or right:
        return f"{left} -> {right}; direction={direction}"
    return direction


def ecocyc_id(prefix: str, uid: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", uid.strip())
    return f"{prefix}.ecocyc.{safe}"


def clean_text(text: str) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\|FRAME:\s*([^|]+)\|", r"\1", text)
    text = re.sub(r"\|CITS?:\s*[^|]+\|", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_name(text: str) -> str:
    text = clean_text(text).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def strip_quotes(text: str) -> str:
    return (text or "").strip().strip('"')


def trim(text: str, limit: int) -> str:
    return text[:limit] if len(text) > limit else text


def dedupe_rows(rows: list[dict[str, str]], fieldnames: list[str], key_fields: list[str] | None = None) -> list[dict[str, str]]:
    key_fields = key_fields or fieldnames
    seen = set()
    result = []
    for row in rows:
        normalized = {field: row.get(field, "") for field in fieldnames}
        key = tuple(normalized.get(field, "") for field in key_fields)
        if key in seen:
            continue
        seen.add(key)
        result.append(normalized)
    return result


if __name__ == "__main__":
    main()
