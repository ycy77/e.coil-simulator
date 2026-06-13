#!/usr/bin/env python3
"""Build a first normalized entities.csv from public raw sources."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


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


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def index_by_entry(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        entry = row.get("Entry", "")
        if entry:
            result[entry] = row
    return result


def primary_gene(gene_names: str) -> str:
    parts = [p for p in gene_names.replace(";", " ").split() if p]
    return parts[0] if parts else ""


def build_protein_entities(raw_uniprot: Path) -> list[dict[str, str]]:
    core = read_tsv(raw_uniprot / "up000000625_core.tsv")
    function = index_by_entry(read_tsv(raw_uniprot / "up000000625_function.tsv"))
    go = index_by_entry(read_tsv(raw_uniprot / "up000000625_go.tsv"))
    pathway = index_by_entry(read_tsv(raw_uniprot / "up000000625_pathway.tsv"))

    entities: list[dict[str, str]] = []
    for row in core:
        accession = row.get("Entry", "")
        if not accession:
            continue
        fn = function.get(accession, {})
        go_row = go.get(accession, {})
        path_row = pathway.get(accession, {})
        gene_names = row.get("Gene Names", "")
        gene = primary_gene(gene_names)
        name = gene or row.get("Entry Name", accession)
        protein_name = row.get("Protein names", "")
        annotation = fn.get("Function [CC]", "") or protein_name
        external = []
        for label, col in [
            ("UniProt", "Entry"),
            ("KEGG", "KEGG"),
            ("GeneID", "GeneID"),
            ("GO", "Gene Ontology IDs"),
            ("EC", "EC number"),
        ]:
            value = row.get(col, "") or go_row.get(col, "")
            if value:
                external.append(f"{label}:{value}")
        entities.append(
            {
                "entity_id": f"protein.{accession}",
                "entity_type": "protein",
                "name": name,
                "aliases": gene_names,
                "default_state": "active",
                "allowed_states": "active|inhibited|degraded|sequestered",
                "annotation": annotation,
                "pathways": path_row.get("Pathway", ""),
                "subcellular_location": fn.get("Subcellular location [CC]", ""),
                "source_database": "UniProt",
                "source_id": accession,
                "external_ids": "|".join(external),
                "is_external": "false",
                "complex_type": "",
                "is_virtual": "",
                "components": "",
                "critical_components": "",
                "assembly_condition": "",
                "notes": protein_name,
            }
        )
    return entities


def build_compound_entities(raw_kegg: Path) -> list[dict[str, str]]:
    compounds_path = raw_kegg / "compounds_raw.tsv"
    if not compounds_path.exists():
        return []

    pathway_compounds: set[str] = set()
    members_path = raw_kegg / "pathway_members_raw.tsv"
    if members_path.exists():
        for row in read_tsv(members_path):
            if row.get("member_type") == "compound":
                pathway_compounds.add(row.get("member_id", ""))

    entities: list[dict[str, str]] = []
    with compounds_path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            compound_id, names = line.split("\t", 1)
            if pathway_compounds and compound_id not in pathway_compounds:
                continue
            name = names.split(";")[0].strip()
            entities.append(
                {
                    "entity_id": f"molecule.{compound_id}",
                    "entity_type": "small_molecule",
                    "name": name,
                    "aliases": names,
                    "default_state": "low",
                    "allowed_states": "absent|low|medium|high",
                    "annotation": f"KEGG compound: {names}",
                    "pathways": "",
                    "subcellular_location": "",
                    "source_database": "KEGG",
                    "source_id": compound_id,
                    "external_ids": f"KEGG:{compound_id}",
                    "is_external": "false",
                    "complex_type": "",
                    "is_virtual": "",
                    "components": "",
                    "critical_components": "",
                    "assembly_condition": "",
                    "notes": "Included because it appears in at least one E. coli KEGG pathway." if pathway_compounds else "From KEGG compound list.",
                }
            )
    return entities


def section(text: str, name: str) -> str:
    pattern = rf"^{name}\s+(.+?)(?=^[A-Z_]+\s|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def build_reaction_entities(raw_kegg: Path) -> list[dict[str, str]]:
    details = raw_kegg / "reaction_details"
    if not details.exists():
        return []
    entities: list[dict[str, str]] = []
    for path in sorted(details.glob("R*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        reaction_id = path.stem
        name = section(text, "NAME").splitlines()[0] if section(text, "NAME") else reaction_id
        definition = section(text, "DEFINITION")
        equation = section(text, "EQUATION")
        entities.append(
            {
                "entity_id": f"reaction.{reaction_id}",
                "entity_type": "reaction",
                "name": name,
                "aliases": reaction_id,
                "default_state": "active",
                "allowed_states": "active|blocked",
                "annotation": definition or equation or f"KEGG reaction {reaction_id}",
                "pathways": "",
                "subcellular_location": "",
                "source_database": "KEGG",
                "source_id": reaction_id,
                "external_ids": f"KEGG:{reaction_id}",
                "is_external": "false",
                "complex_type": "",
                "is_virtual": "true",
                "components": "",
                "critical_components": "",
                "assembly_condition": "",
                "notes": f"EQUATION: {equation}" if equation else "",
            }
        )
    return entities


def write_entities(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ENTITY_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def append_optional_csv(rows: list[dict[str, str]], path: Path) -> None:
    if not path.exists():
        return
    existing = {row["entity_id"] for row in rows}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            entity_id = row.get("entity_id", "")
            if not entity_id or entity_id in existing:
                continue
            rows.append({field: row.get(field, "") for field in ENTITY_FIELDS})
            existing.add(entity_id)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-uniprot", default="data/raw/uniprot")
    parser.add_argument("--raw-kegg", default="data/raw/kegg")
    parser.add_argument("--ncbi-entities", default="data/normalized/ncbi_entities.csv")
    parser.add_argument("--output", default="data/normalized/entities.csv")
    args = parser.parse_args()

    rows = []
    rows.extend(build_protein_entities(Path(args.raw_uniprot)))
    rows.extend(build_compound_entities(Path(args.raw_kegg)))
    rows.extend(build_reaction_entities(Path(args.raw_kegg)))
    append_optional_csv(rows, Path(args.ncbi_entities))
    write_entities(rows, Path(args.output))
    print(f"wrote {args.output} rows={len(rows)}")


if __name__ == "__main__":
    main()
