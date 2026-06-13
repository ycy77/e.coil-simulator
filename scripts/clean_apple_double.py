#!/usr/bin/env python3
"""Strip macOS AppleDouble ``._*`` files that pollute the tree.

These files are created by macOS Finder (or by ``tar`` / ``rsync``
performed on a Mac) and serve no purpose on Linux. They
accidentally get committed to the repo, slow down ``git`` and
``find`` operations, confuse package tooling (npm, pyinstaller,
zipapp), and contaminate tests that glob over the project tree.

This script walks the project and removes every file whose name
starts with ``._`` or matches ``.DS_Store``. It is safe to run
idempotently.

Usage::

    python scripts/clean_apple_double.py            # dry-run, prints what it would delete
    python scripts/clean_apple_double.py --apply   # actually delete
    python scripts/clean_apple_double.py --apply --exclude .git --exclude node_modules

The script never touches anything inside ``.git/`` by default (it
is in the implicit exclude list) so a ``git`` repo is safe. The
``node_modules/`` directory is excluded by default because
removing files there would be wasted work and risks confusing
tooling that re-creates them.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_EXCLUDES = {".git", "node_modules", "__pycache__", "data/raw/ecocyc/extracted"}


def is_junk(name: str) -> bool:
    """Return True if ``name`` looks like an AppleDouble metadata file."""
    return name == ".DS_Store" or name.startswith("._")


def walk_targets(project_root: Path, excludes: set) -> list[Path]:
    out: list[Path] = []
    for path in project_root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in excludes for part in path.parts):
            continue
        if is_junk(path.name):
            out.append(path)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually delete the files (default is dry-run).",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional directory names to skip (can be passed multiple times).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Project root to walk (default: parent of this script).",
    )
    args = parser.parse_args()

    excludes = set(DEFAULT_EXCLUDES) | set(args.exclude)
    targets = walk_targets(args.root, excludes)
    if not targets:
        print("nothing to clean.")
        return 0

    verb = "delete" if args.apply else "would delete"
    print(f"{verb}: {len(targets)} file(s) under {args.root}")
    for path in sorted(targets):
        rel = path.relative_to(args.root)
        print(f"  {rel}")
        if args.apply:
            path.unlink()
    if not args.apply:
        print("Run with --apply to actually delete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
