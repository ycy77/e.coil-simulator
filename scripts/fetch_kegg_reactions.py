#!/usr/bin/env python3
"""Fetch KEGG reactions linked to E. coli EC numbers."""

from __future__ import annotations

import argparse
import time
import urllib.request
from pathlib import Path


KEGG = "https://rest.kegg.jp"


def get_text(path: str, timeout: int = 45) -> str:
    with urllib.request.urlopen(f"{KEGG}/{path}", timeout=timeout) as response:
        return response.read().decode()


def read_ec_numbers(gene_ec_path: Path) -> list[str]:
    ecs = set()
    for line in gene_ec_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        _gene, ec = line.split("\t")
        ecs.add(ec.replace("ec:", ""))
    return sorted(ecs)


def chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def split_kegg_records(text: str) -> dict[str, str]:
    records: dict[str, str] = {}
    for chunk in text.split("///"):
        chunk = chunk.strip()
        if not chunk:
            continue
        first = chunk.splitlines()[0]
        parts = first.split()
        if len(parts) >= 2 and parts[0] == "ENTRY":
            records[parts[1]] = chunk + "\n///\n"
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-kegg", default="data/raw/kegg")
    parser.add_argument("--sleep", type=float, default=0.15)
    parser.add_argument("--batch-size", type=int, default=50)
    args = parser.parse_args()

    raw = Path(args.raw_kegg)
    details = raw / "reaction_details"
    details.mkdir(parents=True, exist_ok=True)

    ec_reaction_lines = ["ec_id\treaction_id"]
    reaction_ids = set()
    ec_numbers = read_ec_numbers(raw / "gene_ec_raw.tsv")
    for i, ec_chunk in enumerate(chunks(ec_numbers, args.batch_size), 1):
        ec_query = "+".join(f"ec:{ec}" for ec in ec_chunk)
        print(f"fetch EC batch {i}", flush=True)
        try:
            text = get_text(f"link/rn/{ec_query}")
        except Exception as exc:
            print(f"warn failed EC batch {i}: {exc}", flush=True)
            continue
        for line in text.splitlines():
            if not line.strip():
                continue
            ec_id, rn_id = line.split("\t")
            reaction_id = rn_id.replace("rn:", "")
            ec_reaction_lines.append(f"{ec_id}\t{reaction_id}")
            reaction_ids.add(reaction_id)
        time.sleep(args.sleep)

    (raw / "ec_reactions_raw.tsv").write_text("\n".join(ec_reaction_lines) + "\n", encoding="utf-8")
    print(f"wrote {raw / 'ec_reactions_raw.tsv'} rows={len(ec_reaction_lines)-1}")

    pending = [rid for rid in sorted(reaction_ids) if not (details / f"{rid}.txt").exists()]
    for i, reaction_chunk in enumerate(chunks(pending, args.batch_size), 1):
        print(f"fetch reaction batch {i}", flush=True)
        try:
            text = get_text("get/" + "+".join(reaction_chunk))
        except Exception as exc:
            print(f"warn failed reaction batch {i}: {exc}", flush=True)
            continue
        records = split_kegg_records(text)
        for reaction_id, record in records.items():
            (details / f"{reaction_id}.txt").write_text(record, encoding="utf-8")
        time.sleep(args.sleep)
    print(f"wrote reaction details count={len(reaction_ids)}")


if __name__ == "__main__":
    main()
