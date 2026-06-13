#!/usr/bin/env python3
"""Fetch NCBI RefSeq files for E. coli K-12 MG1655."""

from __future__ import annotations

import argparse
import urllib.request
from pathlib import Path


BASE_URL = "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2"
PREFIX = "GCF_000005845.2_ASM584v2"
FILES = [
    f"{PREFIX}_genomic.gff.gz",
    f"{PREFIX}_feature_table.txt.gz",
    f"{PREFIX}_rna_from_genomic.fna.gz",
    f"{PREFIX}_protein.faa.gz",
    f"{PREFIX}_cds_from_genomic.fna.gz",
    f"{PREFIX}_translated_cds.faa.gz",
    f"{PREFIX}_genomic.fna.gz",
    f"{PREFIX}_genomic.gbff.gz",
    f"{PREFIX}_assembly_report.txt",
    "md5checksums.txt",
]


def download(url: str, output: Path, force: bool = False) -> None:
    if output.exists() and not force:
        print(f"exists {output}")
        return
    try:
        with urllib.request.urlopen(url, timeout=180) as response:
            output.write_bytes(response.read())
        print(f"wrote {output}")
    except Exception as exc:
        print(f"skip {url}: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="data/raw/ncbi_refseq/GCF_000005845.2")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for filename in FILES:
        download(f"{BASE_URL}/{filename}", outdir / filename, args.force)


if __name__ == "__main__":
    main()
