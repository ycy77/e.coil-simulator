#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect stored raw LLM outputs in a run")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--glob", default="*.json")
    parser.add_argument("--limit", type=int, default=2000)
    args = parser.parse_args()

    for path in sorted((args.run_dir / "agents").glob(args.glob)):
        data = json.loads(path.read_text(encoding="utf-8"))
        last = data["history"][-1]
        metadata = last.get("metadata", {})
        print(f"--- {path}")
        print(f"state={last.get('state')} changed={last.get('changed')} reason={last.get('reason')}")
        print("parsed=", json.dumps(metadata.get("llm_parsed_payload"), ensure_ascii=False)[: args.limit])
        print("raw=", (metadata.get("llm_raw_content") or "")[: args.limit])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
