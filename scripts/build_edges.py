#!/usr/bin/env python3
"""Build first normalized edges.csv from UniProt and KEGG public data."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


FIELDS = [
    "source_id",
    "relation_type",
    "target_id",
    "direction",
    "evidence",
    "source_database",
    "source_record_id",
    "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def build_kegg_to_uniprot(raw_uniprot: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    rows = read_tsv(raw_uniprot / "up000000625_core.tsv")
    for row in rows:
        accession = row.get("Entry", "")
        for item in row.get("KEGG", "").split(";"):
            item = item.strip()
            if item.startswith("eco:"):
                mapping[item] = f"protein.{accession}"
    return mapping


def build_uniprot_to_gene(raw_uniprot: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    rows = read_tsv(raw_uniprot / "up000000625_core.tsv")
    for row in rows:
        accession = row.get("Entry", "")
        match = re.search(r"\bb\d{4}\b", row.get("Gene Names", ""))
        if accession and match:
            mapping[f"protein.{accession}"] = f"gene.{match.group(0)}"
    return mapping


def add_edge(rows: list[dict[str, str]], source: str, rel: str, target: str, source_db: str, record_id: str = "", evidence: str = "database", notes: str = "") -> None:
    if not source or not target:
        return
    rows.append(
        {
            "source_id": source,
            "relation_type": rel,
            "target_id": target,
            "direction": "directed",
            "evidence": evidence,
            "source_database": source_db,
            "source_record_id": record_id,
            "notes": notes,
        }
    )


def append_optional_edges(rows: list[dict[str, str]], path: Path) -> None:
    if not path.exists():
        return
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append({field: row.get(field, "") for field in FIELDS})


def section(text: str, name: str) -> str:
    pattern = rf"^{name}\s+(.+?)(?=^[A-Z_]+\s|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def parse_equation(equation: str) -> tuple[list[str], list[str]]:
    if not equation:
        return [], []
    if "<=>" in equation:
        left, right = equation.split("<=>", 1)
    elif "=>" in equation:
        left, right = equation.split("=>", 1)
    else:
        return [], []
    return re.findall(r"C\d{5}", left), re.findall(r"C\d{5}", right)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-uniprot", default="data/raw/uniprot")
    parser.add_argument("--raw-kegg", default="data/raw/kegg")
    parser.add_argument("--regulondb-edges", default="data/normalized/regulondb_edges.csv")
    parser.add_argument("--output", default="data/normalized/edges.csv")
    args = parser.parse_args()

    raw_uniprot = Path(args.raw_uniprot)
    raw_kegg = Path(args.raw_kegg)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    kegg_to_protein = build_kegg_to_uniprot(raw_uniprot)
    protein_to_gene = build_uniprot_to_gene(raw_uniprot)
    edges: list[dict[str, str]] = []

    # NCBI/UniProt gene-to-protein encoding links.
    for protein_id, gene_id in protein_to_gene.items():
        add_edge(edges, gene_id, "encodes", protein_id, "UniProt", protein_id.replace("protein.", ""))

    # Gene/protein to pathway membership from KEGG.
    for line in (raw_kegg / "gene_pathways_raw.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        gene_id, pathway_id = line.split("\t")
        protein_id = kegg_to_protein.get(gene_id)
        pathway_id = pathway_id.replace("path:", "")
        add_edge(edges, protein_id or gene_id.replace("eco:", "gene."), "participates_in", pathway_id, "KEGG", gene_id)

    # Protein to EC relation from KEGG.
    gene_ec_pairs: list[tuple[str, str, str]] = []
    for line in (raw_kegg / "gene_ec_raw.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        gene_id, ec_id = line.split("\t")
        gene_ec_pairs.append((gene_id, ec_id.replace("ec:", ""), ec_id))
        protein_id = kegg_to_protein.get(gene_id)
        add_edge(edges, protein_id or gene_id.replace("eco:", "gene."), "catalyzes", ec_id, "KEGG", gene_id, notes="KEGG gene-to-EC link")

    ec_to_reactions: dict[str, set[str]] = {}
    ec_reactions_path = raw_kegg / "ec_reactions_raw.tsv"
    if ec_reactions_path.exists():
        for row in read_tsv(ec_reactions_path):
            ec = row.get("ec_id", "").replace("ec:", "")
            reaction = row.get("reaction_id", "")
            if ec and reaction:
                ec_to_reactions.setdefault(ec, set()).add(reaction)

    for gene_id, ec, _ec_id in gene_ec_pairs:
        protein_id = kegg_to_protein.get(gene_id)
        for reaction_id in sorted(ec_to_reactions.get(ec, [])):
            add_edge(edges, protein_id or gene_id.replace("eco:", "gene."), "catalyzes", f"reaction.{reaction_id}", "KEGG", gene_id, notes=f"via EC:{ec}")

    # Pathway detail members.
    members_path = raw_kegg / "pathway_members_raw.tsv"
    if members_path.exists():
        for row in read_tsv(members_path):
            pathway_id = row.get("pathway_id", "")
            member_type = row.get("member_type", "")
            member_id = row.get("member_id", "")
            if member_type == "compound":
                add_edge(edges, f"molecule.{member_id}", "participates_in", pathway_id, "KEGG", pathway_id)
            elif member_type == "reaction":
                add_edge(edges, f"reaction.{member_id}", "participates_in", pathway_id, "KEGG", pathway_id)
            elif member_type == "gene":
                protein_id = kegg_to_protein.get(member_id)
                add_edge(edges, protein_id or member_id.replace("eco:", "gene."), "participates_in", pathway_id, "KEGG", pathway_id)

    # Reaction substrate/product edges from KEGG reaction equations.
    details = raw_kegg / "reaction_details"
    if details.exists():
        for path in sorted(details.glob("R*.txt")):
            reaction_id = path.stem
            equation = section(path.read_text(encoding="utf-8", errors="replace"), "EQUATION")
            substrates, products = parse_equation(equation)
            for compound in substrates:
                add_edge(edges, f"molecule.{compound}", "is_substrate_of", f"reaction.{reaction_id}", "KEGG", reaction_id, notes=equation)
            for compound in products:
                add_edge(edges, f"molecule.{compound}", "is_product_of", f"reaction.{reaction_id}", "KEGG", reaction_id, notes=equation)

    append_optional_edges(edges, Path(args.regulondb_edges))

    # De-duplicate while preserving order.
    seen = set()
    unique = []
    for row in edges:
        key = (row["source_id"], row["relation_type"], row["target_id"], row["source_database"], row["source_record_id"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)

    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(unique)
    print(f"wrote {output} rows={len(unique)}")


if __name__ == "__main__":
    main()
