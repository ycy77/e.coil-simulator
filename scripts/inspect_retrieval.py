#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import AgentState
from ecoil_sim.paths import PROJECT_ROOT
from ecoil_sim.registry import RuleRegistry
from ecoil_sim.retrieval import TemporalGraphRAG
from ecoil_sim.rules import RuleEngine
from ecoil_sim.state import TemporalState


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect temporal GraphRAG retrieval for a perturbed entity.")
    parser.add_argument("entity_id")
    parser.add_argument("--state", default="knocked_out")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    graph = StaticGraph.from_normalized_dir()
    registry = RuleRegistry.from_registry_dir()
    edge_config = load_yaml_like(PROJECT_ROOT / "configs/edge_weights.yaml")
    weights = edge_config.get("edge_weights", {})
    temporal = TemporalState.initialize(graph.entities.values())
    updates = RuleEngine().apply_perturbations(
        temporal,
        [{"entity_id": args.entity_id, "state": args.state, "reason": "inspection perturbation"}],
    )
    temporal.apply_changes(updates)
    retriever = TemporalGraphRAG(graph, registry, weights, state_distance=edge_config.get("state_distance", {}), min_score=0.0)
    contexts = retriever.retrieve(temporal, [args.entity_id], max_agents=args.limit)
    print(f"changed={args.entity_id} contexts={len(contexts)}")
    for ctx in contexts:
        entity = graph.entities.get(ctx.entity_id)
        rels = ",".join(sorted({edge.relation_type for edge in ctx.edges}))
        print(f"{ctx.score:.2f}\t{ctx.entity_id}\t{entity.entity_type if entity else '?'}\t{entity.name if entity else '?'}\t{rels}\trules={len(ctx.rules)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
