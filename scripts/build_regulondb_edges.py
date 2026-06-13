#!/usr/bin/env python3
"""Build regulatory edges from RegulonDB TSV files."""

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

KEEP_CONFIDENCE = {"C", "S"}


def clean_header(value: str) -> str:
    return re.sub(r"^\d+\)", "", value).strip()


def read_regulondb_tsv(path: Path) -> list[dict[str, str]]:
    lines = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        lines.append(line)
    if not lines:
        return []
    header = [clean_header(x) for x in lines[0].split("\t")]
    rows = []
    for line in lines[1:]:
        cols = line.split("\t")
        if len(cols) < len(header):
            cols += [""] * (len(header) - len(cols))
        rows.append(dict(zip(header, cols)))
    return rows


def parse_other_ids(text: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for key, value in re.findall(r"\[([^:\]]+):([^\]]+)\]", text or ""):
        result.setdefault(key.upper(), []).append(value)
    return result


def build_gene_maps(regulondb: Path) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Return gene name/id/product id maps to b-number."""
    name_to_b: dict[str, str] = {}
    id_to_b: dict[str, str] = {}
    product_to_b: dict[str, str] = {}
    for row in read_regulondb_tsv(regulondb / "GeneProductSet.tsv"):
        bnum = row.get("bnumber", "").strip()
        if not bnum:
            ids = parse_other_ids(row.get("otherDbsIds", ""))
            refs = ids.get("REFSEQ", [])
            bnum = refs[0] if refs else ""
        if not bnum:
            continue
        gene_id = row.get("geneId", "").strip()
        if gene_id:
            id_to_b[gene_id] = bnum
        product_id = row.get("productId", "").strip()
        if product_id:
            product_to_b[product_id] = bnum
        names = [row.get("geneName", "").strip()]
        for value in row.get("relatedBnumbers", "").split("|"):
            if value:
                names.append(value.strip())
        other = parse_other_ids(row.get("otherDbsIds", ""))
        for ref in other.get("REFSEQ", []):
            names.append(ref)
        for name in names:
            if name:
                name_to_b[name.lower()] = bnum
    return name_to_b, id_to_b, product_to_b


def build_tf_maps(regulondb: Path, name_to_b: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    regulator_id_to_b: dict[str, str] = {}
    sigma_name_to_b: dict[str, str] = {}
    for filename in ("RegulatorSet.tsv", "TFSet.tsv"):
        path = regulondb / filename
        if not path.exists():
            continue
        for row in read_regulondb_tsv(path):
            rid = row.get("regulatorId") or row.get("tfId") or ""
            bnum = row.get("geneBnumberCodingForRegulator") or row.get("geneBnumberCodingForTF") or ""
            gene = row.get("geneCodingForRegulator") or row.get("geneCodingForTF") or ""
            if not bnum and gene:
                bnum = name_to_b.get(gene.lower(), "")
            if rid and bnum:
                regulator_id_to_b[rid] = bnum
            name = row.get("regulatorName") or row.get("tfName") or ""
            if name and bnum and name.lower().startswith("sigma"):
                sigma_name_to_b[name.lower()] = bnum

    # Common sigma aliases when RegulonDB uses sigmaXX names in NetworkSigma*.
    sigma_alias = {
        "sigma70": "rpoD",
        "sigma38": "rpoS",
        "sigma32": "rpoH",
        "sigma54": "rpoN",
        "sigma28": "fliA",
        "sigma24": "rpoE",
        "sigma19": "fecI",
    }
    for sigma, gene in sigma_alias.items():
        bnum = name_to_b.get(gene.lower(), "")
        if bnum:
            sigma_name_to_b.setdefault(sigma, bnum)
    return regulator_id_to_b, sigma_name_to_b


def build_b_to_protein(raw_uniprot: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    path = raw_uniprot / "up000000625_core.tsv"
    if not path.exists():
        return mapping
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            accession = row.get("Entry", "")
            match = re.search(r"\bb\d{4}\b", row.get("Gene Names", ""))
            if accession and match:
                mapping[match.group(0)] = f"protein.{accession}"
    return mapping


def function_to_rel(function: str) -> list[str]:
    f = (function or "").strip().lower()
    rels = []
    if "+" in f or "activator" in f:
        rels.append("activates")
    if "-" in f or "repressor" in f:
        rels.append("represses")
    return rels


def add_edge(edges: list[dict[str, str]], source: str, rel: str, target: str, record_id: str, confidence: str, notes: str) -> None:
    if not source or not target:
        return
    edges.append(
        {
            "source_id": source,
            "relation_type": rel,
            "target_id": target,
            "direction": "directed",
            "evidence": confidence,
            "source_database": "RegulonDB",
            "source_record_id": record_id,
            "notes": notes,
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regulondb", default="data/regulationDB")
    parser.add_argument("--raw-uniprot", default="data/raw/uniprot")
    parser.add_argument("--output", default="data/normalized/regulondb_edges.csv")
    parser.add_argument("--skipped", default="data/normalized/regulondb_skipped.tsv")
    parser.add_argument("--include-weak", action="store_true")
    args = parser.parse_args()

    regulondb = Path(args.regulondb)
    name_to_b, id_to_b, _product_to_b = build_gene_maps(regulondb)
    regulator_id_to_b, sigma_name_to_b = build_tf_maps(regulondb, name_to_b)
    b_to_protein = build_b_to_protein(Path(args.raw_uniprot))
    keep = {"C", "S", "W"} if args.include_weak else KEEP_CONFIDENCE

    edges: list[dict[str, str]] = []
    skipped: list[tuple[str, str, str]] = []

    for row in read_regulondb_tsv(regulondb / "NetworkRegulatorGene.tsv"):
        conf = row.get("confidenceLevel", "").strip()
        if conf not in keep:
            continue
        target_b = id_to_b.get(row.get("regulatedId", ""), "") or name_to_b.get(row.get("regulatedName", "").lower(), "")
        reg_b = regulator_id_to_b.get(row.get("regulatorId", ""), "") or name_to_b.get(row.get("RegulatorGeneName", "").lower(), "")
        source = b_to_protein.get(reg_b, f"gene.{reg_b}" if reg_b else "")
        target = f"gene.{target_b}" if target_b else ""
        rels = function_to_rel(row.get("function", ""))
        if not source or not target or not rels:
            skipped.append(("NetworkRegulatorGene", row.get("regulatorName", ""), row.get("regulatedName", "")))
            continue
        for rel in rels:
            add_edge(edges, source, rel, target, row.get("regulatorId", ""), conf, f"regulator={row.get('regulatorName','')}; target={row.get('regulatedName','')}; function={row.get('function','')}")

    for row in read_regulondb_tsv(regulondb / "NetworkSigmaGene.tsv"):
        conf = row.get("confidenceLevel", "").strip()
        if conf not in keep:
            continue
        sigma_b = sigma_name_to_b.get(row.get("sigmaName", "").lower(), "")
        target_b = name_to_b.get(row.get("regulatedName", "").lower(), "")
        source = b_to_protein.get(sigma_b, f"gene.{sigma_b}" if sigma_b else "")
        target = f"gene.{target_b}" if target_b else ""
        rels = function_to_rel(row.get("function", "")) or ["activates"]
        if not source or not target:
            skipped.append(("NetworkSigmaGene", row.get("sigmaName", ""), row.get("regulatedName", "")))
            continue
        for rel in rels:
            add_edge(edges, source, rel, target, row.get("sigmaName", ""), conf, f"sigma={row.get('sigmaName','')}; target={row.get('regulatedName','')}; function={row.get('function','')}")

    seen = set()
    unique = []
    for row in edges:
        key = (row["source_id"], row["relation_type"], row["target_id"], row["source_record_id"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(unique)

    skipped_path = Path(args.skipped)
    with skipped_path.open("w", encoding="utf-8") as handle:
        handle.write("source\tregulator\ttarget\n")
        for item in skipped:
            handle.write("\t".join(item) + "\n")

    print(f"wrote {output} rows={len(unique)}")
    print(f"wrote {skipped_path} rows={len(skipped)}")


if __name__ == "__main__":
    main()
