#!/usr/bin/env python3
"""Build gene/RNA/regulatory entities from NCBI RefSeq GFF."""

from __future__ import annotations

import argparse
import csv
import gzip
import re
from pathlib import Path
from urllib.parse import unquote


FIELDS = [
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

RNA_TYPES = {"rRNA", "tRNA", "tmRNA", "ncRNA", "SRP_RNA", "RNase_P_RNA", "antisense_RNA"}
REGULATORY_TYPES = {"regulatory_region", "promoter", "terminator", "attenuator"}


def parse_attrs(attr_text: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for part in attr_text.split(";"):
        if not part or "=" not in part:
            continue
        key, value = part.split("=", 1)
        attrs[key] = unquote(value)
    return attrs


def sanitize(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[^A-Za-z0-9_.:-]+", "_", value)
    return value.strip("_")


def pick_id(attrs: dict[str, str], fallback: str) -> str:
    for key in ("locus_tag", "gene", "Name", "ID"):
        value = attrs.get(key, "")
        if value:
            return sanitize(value)
    return fallback


def external_ids(attrs: dict[str, str]) -> str:
    items = []
    for key in ("Dbxref", "protein_id", "gbkey", "gene_biotype"):
        value = attrs.get(key, "")
        if value:
            items.append(f"{key}:{value}")
    return "|".join(items)


def row_for(feature_type: str, attrs: dict[str, str], seqid: str, start: str, end: str, strand: str, fallback_ix: int) -> dict[str, str] | None:
    fallback = f"{feature_type}_{fallback_ix}"
    local_id = pick_id(attrs, fallback)
    name = attrs.get("gene") or attrs.get("Name") or attrs.get("product") or local_id
    aliases = "|".join(x for x in [attrs.get("locus_tag", ""), attrs.get("gene", ""), attrs.get("Name", "")] if x)
    product = attrs.get("product", "")
    note = attrs.get("Note", "")
    annotation = product or note or f"NCBI RefSeq {feature_type} feature"

    if feature_type == "gene":
        entity_type = "gene"
        entity_id = f"gene.{local_id}"
        default_state = "expressed"
        allowed = "expressed|repressed|knocked_out|mutated|overexpressed"
    elif feature_type in RNA_TYPES:
        entity_type = "rna"
        entity_id = f"rna.{local_id}"
        default_state = "active"
        allowed = "active|inhibited|degraded|overexpressed"
    elif feature_type in REGULATORY_TYPES:
        entity_type = "regulatory_region"
        entity_id = f"regulatory_region.{local_id}"
        default_state = "active"
        allowed = "active|inactive|bound|unbound|mutated"
    else:
        return None

    return {
        "entity_id": entity_id,
        "entity_type": entity_type,
        "name": name,
        "aliases": aliases,
        "default_state": default_state,
        "allowed_states": allowed,
        "annotation": annotation,
        "pathways": "",
        "subcellular_location": "cytosol",
        "source_database": "NCBI RefSeq",
        "source_id": attrs.get("ID", local_id),
        "external_ids": external_ids(attrs),
        "is_external": "false",
        "complex_type": "",
        "is_virtual": "",
        "components": "",
        "critical_components": "",
        "assembly_condition": "",
        "notes": f"{seqid}:{start}-{end}:{strand}; feature_type={feature_type}",
    }


def parse_gff(gff_path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    with gzip.open(gff_path, "rt", encoding="utf-8") as handle:
        for ix, line in enumerate(handle, 1):
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) != 9:
                continue
            seqid, _source, feature_type, start, end, _score, strand, _phase, attr_text = parts
            row = row_for(feature_type, parse_attrs(attr_text), seqid, start, end, strand, ix)
            if not row:
                continue
            if row["entity_id"] in seen:
                continue
            seen.add(row["entity_id"])
            rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-ncbi", default="data/raw/ncbi_refseq/GCF_000005845.2")
    parser.add_argument("--output", default="data/normalized/ncbi_entities.csv")
    args = parser.parse_args()

    raw = Path(args.raw_ncbi)
    gff = raw / "GCF_000005845.2_ASM584v2_genomic.gff.gz"
    rows = parse_gff(gff)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {output} rows={len(rows)}")


if __name__ == "__main__":
    main()
