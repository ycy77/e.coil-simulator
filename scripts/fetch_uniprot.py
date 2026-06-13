#!/usr/bin/env python3
"""Fetch E. coli K-12 MG1655 protein annotations from UniProt."""

from __future__ import annotations

import argparse
import time
import urllib.parse
import urllib.request
from pathlib import Path


BASE_URL = "https://rest.uniprot.org/uniprotkb/stream"
QUERY = "proteome:UP000000625"

FIELD_SETS = {
    "core": "accession,id,gene_names,protein_name,organism_name,ec,xref_kegg,xref_geneid",
    "function": "accession,id,gene_names,protein_name,cc_function,cc_subcellular_location",
    "go": "accession,id,gene_names,protein_name,go_id",
    "pathway": "accession,id,gene_names,protein_name,cc_pathway,cc_interaction",
}


def fetch_stream(fields: str, reviewed_only: bool, output: Path) -> None:
    query = QUERY
    if reviewed_only:
        query = f"{query} AND reviewed:true"
    params = {
        "query": query,
        "format": "tsv",
        "fields": fields,
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=180) as response:
        output.write_bytes(response.read())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="data/raw/uniprot")
    parser.add_argument("--reviewed-only", action="store_true")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for name, fields in FIELD_SETS.items():
        output = outdir / f"up000000625_{name}.tsv"
        fetch_stream(fields, args.reviewed_only, output)
        print(f"wrote {output}")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
