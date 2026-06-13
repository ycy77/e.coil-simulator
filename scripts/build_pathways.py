#!/usr/bin/env python3
"""Build normalized pathways.csv from KEGG pathway list."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


FIELDS = ["pathway_id", "pathway_name", "source", "description", "organism"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-kegg", default="data/raw/kegg")
    parser.add_argument("--output", default="data/normalized/pathways.csv")
    args = parser.parse_args()

    raw = Path(args.raw_kegg) / "pathways_raw.tsv"
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with raw.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            pathway_id, name = line.split("\t", 1)
            rows.append(
                {
                    "pathway_id": pathway_id,
                    "pathway_name": name.replace(" - Escherichia coli K-12 MG1655", ""),
                    "source": "KEGG",
                    "description": name,
                    "organism": "Escherichia coli K-12 MG1655",
                }
            )

    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {output} rows={len(rows)}")


if __name__ == "__main__":
    main()
