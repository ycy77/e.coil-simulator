#!/usr/bin/env python3
"""Fetch the Tjaden 2023 E. coli transcriptome compendium from Harvard Dataverse.

Tjaden B. "Escherichia coli transcriptome assembly from a compendium of RNA-seq
data sets." RNA Biology 2023. doi:10.1080/15476286.2023.2189331
Data: Harvard Dataverse doi:10.7910/DVN/QBMC9D (TPM expression for all genes
across 3,376 RNA-seq samples + operon / co-transcription tables + transcript GFF).

We use it for external validation that does NOT depend on RegulonDB:
  * co-expression validation of the graph's regulatory edges
    (scripts/validate_coexpression.py)
  * (follow-up) operon import to raise KG recall and enable L3.

This downloads at runtime via the Dataverse API, so it needs network egress —
run it on the GPU host (the dev laptop sandbox has none). It discovers files by
querying the dataset, then downloads those matching --patterns into
data/raw/transcriptome_compendium/.

    python scripts/fetch_transcriptome_compendium.py            # expression + operon tables
    python scripts/fetch_transcriptome_compendium.py --all      # everything
    python scripts/fetch_transcriptome_compendium.py --list     # just list files
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOI = "doi:10.7910/DVN/QBMC9D"
BASE = "https://dataverse.harvard.edu"
DEST = PROJECT_ROOT / "data" / "raw" / "transcriptome_compendium"
# substrings (lowercased) that flag the files we care about by default
DEFAULT_PATTERNS = ["express", "tpm", "operon", "transcription", "cotranscri", "polycistron"]


def parse_args():
    p = argparse.ArgumentParser(description="Fetch Tjaden 2023 transcriptome compendium.")
    p.add_argument("--doi", default=DOI)
    p.add_argument("--dest", type=Path, default=DEST)
    p.add_argument("--patterns", nargs="*", default=DEFAULT_PATTERNS,
                   help="download files whose name contains any of these (lowercased)")
    p.add_argument("--all", action="store_true", help="download every file")
    p.add_argument("--list", action="store_true", help="only list files, do not download")
    p.add_argument("--max-mb", type=float, default=2000.0, help="skip files larger than this")
    return p.parse_args()


def list_files(doi: str):
    url = f"{BASE}/api/datasets/:persistentId/?persistentId={doi}"
    with urllib.request.urlopen(url, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    files = data.get("data", {}).get("latestVersion", {}).get("files", [])
    out = []
    for f in files:
        df = f.get("dataFile", {})
        out.append({
            "id": df.get("id"),
            "name": df.get("filename", ""),
            "size_mb": round(df.get("filesize", 0) / 1e6, 2),
            "type": df.get("contentType", ""),
        })
    return out


def download(file_id: int, name: str, dest_dir: Path):
    dest_dir.mkdir(parents=True, exist_ok=True)
    url = f"{BASE}/api/access/datafile/{file_id}"
    target = dest_dir / name
    print(f"  downloading {name} ...", flush=True)
    urllib.request.urlretrieve(url, target)
    return target


def main() -> int:
    args = parse_args()
    try:
        files = list_files(args.doi)
    except Exception as exc:
        print(f"ERROR: could not reach Harvard Dataverse ({exc}).", file=sys.stderr)
        print("This needs network egress — run on a networked machine (the GPU host).", file=sys.stderr)
        return 2

    print(f"Dataset {args.doi}: {len(files)} files")
    for f in files:
        print(f"  id={f['id']:>8}  {f['size_mb']:>8.1f}MB  {f['name']}  ({f['type']})")
    if args.list:
        return 0

    patterns = [p.lower() for p in args.patterns]
    selected = [
        f for f in files
        if (args.all or any(p in f["name"].lower() for p in patterns)) and f["size_mb"] <= args.max_mb
    ]
    if not selected:
        print("\nNo files matched. Use --list to inspect names, or --patterns / --all.")
        return 1
    print(f"\nDownloading {len(selected)} file(s) into {args.dest}:")
    for f in selected:
        try:
            download(f["id"], f["name"], args.dest)
        except Exception as exc:
            print(f"  ! failed {f['name']}: {exc}")
    print("\nDone. Next: python scripts/validate_coexpression.py "
          "--matrix data/raw/transcriptome_compendium/<expression_file>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
