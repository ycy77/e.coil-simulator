#!/usr/bin/env python3
"""LLM perturbation intake — chat text or uploaded file -> graph entry points.

Two input adapters, one shared grounding + confirm core:

    # chat-style free text (real model, on the GPU host):
    python scripts/parse_perturbation.py --text "knock out recA and add 2mg/L ciprofloxacin"

    # uploaded file (a protocol / experiment description):
    python scripts/parse_perturbation.py --file my_treatment.txt

    # offline grounding preview (no vLLM needed) — see what each mention maps to:
    python scripts/parse_perturbation.py --text "ciprofloxacin, recA, ampicillin" --dry-run

The real modes need the vLLM endpoint (configs/model.qwen35_9b.yaml). They print
a proposal for the user to confirm; nothing is run automatically (judgment to
humans). Pass --emit-changes to also print the engine-ready perturbation list.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import csv  # noqa: E402

from ecoil_sim.config import load_yaml_like  # noqa: E402
from ecoil_sim.graph import StaticGraph  # noqa: E402
from ecoil_sim.models import Entity  # noqa: E402
from ecoil_sim.sim.grounding import EntityGrounder  # noqa: E402
from ecoil_sim.sim.llm_perturbation import LLMPerturbationParser, VLLMJsonCompleter  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="LLM perturbation intake (chat/file -> entry points).")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="free-text perturbation request (chat adapter)")
    src.add_argument("--file", type=Path, help="path to a request/protocol file (file adapter)")
    p.add_argument("--config", type=Path, default=Path("configs/simulation.yaml"))
    p.add_argument("--model-config", type=Path, default=Path("configs/model.qwen35_9b.yaml"))
    p.add_argument("--intake-schema", type=Path, default=Path("schemas/perturbation_intake.schema.json"))
    p.add_argument("--dry-run", action="store_true", help="offline: show grounding candidates only, no LLM")
    p.add_argument("--emit-changes", action="store_true", help="also print engine-ready perturbation JSON")
    return p.parse_args()


def build_grounder(config) -> tuple:
    graph_cfg = config.get("graph", {})
    graph = StaticGraph.from_normalized_dir(PROJECT_ROOT / graph_cfg.get("normalized_dir", "data/normalized"))
    # Perturbagen entities are loaded directly (their dir has no pathways.csv).
    perturbagen_csv = PROJECT_ROOT / "data" / "normalized" / "perturbagens" / "entities.csv"
    perturbagens = []
    if perturbagen_csv.exists():
        with perturbagen_csv.open(newline="", encoding="utf-8") as handle:
            perturbagens = [Entity.from_row(row) for row in csv.DictReader(handle)]
    return graph, EntityGrounder(graph.entities.values(), perturbagens)


def dry_run(grounder: EntityGrounder, text: str) -> int:
    # Rough offline preview. The real pipeline's LLM stage extracts a clean
    # mention ("recA") and target concepts ("DNA gyrase"); here we approximate by
    # grounding each clause AND its individual tokens, then keeping the best
    # candidates. This previews the grounder without an LLM; it is not the
    # production path.
    mentions = [m.strip() for m in re.split(r",|;|\band\b|\n", text) if m.strip()]
    print(f"Offline grounding preview for {len(mentions)} clause(s):\n")
    for mention in mentions:
        # The grounder already handles verb-prefixed spans (token fallback at
        # name/alias tier), so a stopword like "add" no longer outranks the
        # real agent.
        ranked = grounder.candidates(mention, limit=5)
        print(f"  \"{mention}\":")
        if not ranked:
            print("      (no candidates — likely exogenous; the LLM would supply the target concept)")
        for c in ranked:
            tag = " [exogenous]" if c.is_exogenous else ""
            print(f"      {c.entity_id:28s} {c.name:14s} via={c.matched_via:16s} states={'|'.join(c.allowed_states)}{tag}")
        print()
    return 0


def main() -> int:
    args = parse_args()
    config = load_yaml_like(PROJECT_ROOT / args.config)
    graph, grounder = build_grounder(config)
    text = args.text if args.text is not None else Path(args.file).read_text(encoding="utf-8")

    if args.dry_run:
        return dry_run(grounder, text)

    model_config = load_yaml_like(PROJECT_ROOT / args.model_config)
    llm_cfg = model_config.get("llm", {})
    completer = VLLMJsonCompleter(
        base_url=llm_cfg.get("base_url", "http://localhost:8000/v1"),
        model=llm_cfg.get("model", ""),
        api_key=llm_cfg.get("api_key", "EMPTY"),
    )
    intake_schema = None
    if args.intake_schema.exists():
        intake_schema = json.loads((PROJECT_ROOT / args.intake_schema).read_text(encoding="utf-8"))
    parser = LLMPerturbationParser(
        graph, grounder, completer, prompts_dir=PROJECT_ROOT / "prompts", intake_schema=intake_schema
    )
    proposal = parser.parse_text(text)
    print(proposal.render())
    if args.emit_changes:
        print("\nengine_changes=" + json.dumps(proposal.to_engine_changes(), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
