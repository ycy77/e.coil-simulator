#!/usr/bin/env python3
"""Fetch KEGG data needed for the first E.coil graph build."""

from __future__ import annotations

import argparse
import re
import time
import urllib.request
from pathlib import Path


KEGG = "https://rest.kegg.jp"


def get_text(path: str) -> str:
    url = f"{KEGG}/{path}"
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read().decode()


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path}")


def parse_pathway_ids(pathways_text: str) -> list[str]:
    ids: list[str] = []
    for line in pathways_text.splitlines():
        if not line.strip():
            continue
        token = line.split("\t", 1)[0]
        if token.startswith("path:"):
            token = token.split(":", 1)[1]
        ids.append(token)
    return ids


def section(text: str, name: str) -> str:
    pattern = rf"^{name}\s+(.+?)(?=^[A-Z_]+\s|\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def parse_pathway_members(pathway_id: str, text: str) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    gene_block = section(text, "GENE")
    for line in gene_block.splitlines():
        line = line.rstrip()
        match = re.match(r"^(\d+)\s+([^\s;]+)", line)
        if match:
            rows.append((pathway_id, "gene", f"eco:b{int(match.group(1)):04d}"))

    compound_block = section(text, "COMPOUND")
    for line in compound_block.splitlines():
        match = re.match(r"^(C\d{5})\s+", line.strip())
        if match:
            rows.append((pathway_id, "compound", match.group(1)))

    reaction_block = section(text, "REACTION")
    for line in reaction_block.splitlines():
        match = re.match(r"^(R\d{5})\s+", line.strip())
        if match:
            rows.append((pathway_id, "reaction", match.group(1)))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="data/raw/kegg")
    parser.add_argument("--sleep", type=float, default=0.25)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    details_dir = outdir / "pathway_details"
    outdir.mkdir(parents=True, exist_ok=True)
    details_dir.mkdir(parents=True, exist_ok=True)

    pathways = get_text("list/pathway/eco")
    write(outdir / "pathways_raw.tsv", pathways)

    gene_pathways = get_text("link/pathway/eco")
    write(outdir / "gene_pathways_raw.tsv", gene_pathways)

    gene_ec = get_text("link/ec/eco")
    write(outdir / "gene_ec_raw.tsv", gene_ec)

    compounds = get_text("list/compound")
    write(outdir / "compounds_raw.tsv", compounds)

    members: list[tuple[str, str, str]] = []
    for pathway_id in parse_pathway_ids(pathways):
        text = get_text(f"get/{pathway_id}")
        write(details_dir / f"{pathway_id}.txt", text)
        members.extend(parse_pathway_members(pathway_id, text))
        time.sleep(args.sleep)

    member_lines = ["pathway_id\tmember_type\tmember_id"]
    member_lines.extend("\t".join(row) for row in members)
    write(outdir / "pathway_members_raw.tsv", "\n".join(member_lines) + "\n")


if __name__ == "__main__":
    main()
