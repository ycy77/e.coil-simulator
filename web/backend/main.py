"""FastAPI backend for the E.coil diagnostic UI.

Mounts the data loader, graph service, and run service and exposes
them as JSON endpoints. CORS is permissive (``*``) because the
diagnostic is local-only. The port is fixed at ``28932`` to stay out
of the way of common dev services.
"""

# We deliberately do NOT use ``from __future__ import annotations``
# here because FastAPI / Pydantic needs the return-type annotations
# to resolve at module-load time, not as forward-reference strings.
# Pydantic 2 + typing.Dict stringification caused spurious
# "TypeAdapter not fully defined" errors when this file used
# ``from __future__ import annotations``.

import logging
import sys
from pathlib import Path
from typing import Any, List, Optional, Dict

# Allow ``from web.backend ...`` to work when uvicorn is started with
# ``--app-dir web`` (which we do in the launcher) and also when the
# module is imported directly.
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from web.backend.data_loader import DataLoader
from web.backend.enriched_loader import EnrichedLoader
from web.backend.graph_service import GraphService
from web.backend.run_service import RunService
from web.backend import insights


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def create_app() -> FastAPI:
    app = FastAPI(title="E.coil diagnostic UI", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False,
    )

    # Loader priority:
    #   1. data/normalized/simulation/   -- clean simulation baseline
    #                                    (output of build_simulation_baseline.py,
    #                                    post flatten_reactions.py)
    #   2. data/normalized/_v2/          -- canonicalized v2 (legacy)
    #   3. data/normalized/              -- raw v1
    loader = DataLoader(PROJECT_ROOT)
    sim_dir = PROJECT_ROOT / "data" / "normalized" / "simulation"
    v2_dir = PROJECT_ROOT / "data" / "normalized" / "_v2"
    if sim_dir.exists() and (sim_dir / "entities.csv").exists():
        loader.normalized_dir = sim_dir
    elif v2_dir.exists() and (v2_dir / "entities.csv").exists():
        loader.normalized_dir = v2_dir
    loader.load()
    enriched_path = PROJECT_ROOT / "data" / "enriched" / "_v2" / "entities_enriched_v2_lite.jsonl"
    if not enriched_path.exists():
        enriched_path = PROJECT_ROOT / "data" / "enriched" / "entities_enriched_lite.jsonl"
    enriched = EnrichedLoader(enriched_path)
    enriched.load()
    loader.attach_enriched(enriched._by_id)  # type: ignore[attr-defined]
    graph = GraphService(loader)
    runs = RunService(PROJECT_ROOT / "runs")

    # Optional perturbagen-pool loader, only used by endpoints
    # that explicitly ask for it. Built lazily so the diagnostic
    # UI keeps a low memory footprint.
    perturbagen_loader: Optional[DataLoader] = None
    pert_dir = PROJECT_ROOT / "data" / "normalized" / "perturbagens"
    if pert_dir.exists() and (pert_dir / "entities.csv").exists():
        perturbagen_loader = DataLoader(PROJECT_ROOT)
        perturbagen_loader.normalized_dir = pert_dir
        perturbagen_loader.load()

    @app.get("/api/health")
    def health() -> dict:
        return {
            "status": "ok",
            "entities": len(loader._entities),  # type: ignore[attr-defined]
            "edges": len(loader._edges),  # type: ignore[attr-defined]
        }

    @app.get("/api/stats")
    def stats() -> dict:
        report = loader.data_quality_report().to_dict()  # type: ignore[attr-defined]
        report["enriched_quality"] = dict(
            sorted(enriched.quality_distribution().items())  # type: ignore[attr-defined]
        )
        report["enriched_count"] = len(enriched._by_id)  # type: ignore[attr-defined]
        # Augment with the perturbagen-pool roll-up so the
        # diagnostic top-bar can show "baseline N / perturbagen M".
        # Reading the perturbagen loader is cheap once it is
        # already loaded at startup.
        if perturbagen_loader is not None:
            pert_report = perturbagen_loader.data_quality_report()  # type: ignore[attr-defined]
            report["perturbagen"] = {
                "entities": pert_report.entity_count,
                "edges": pert_report.edge_count,
                "by_type": dict(sorted(pert_report.type_distribution.items())),
            }
        else:
            report["perturbagen"] = None
        # Quarantine (class-abstraction) is co-located with the
        # perturbagen directory; count it from disk.
        quar_path = PROJECT_ROOT / "data" / "normalized" / "perturbagens" / "_quarantine.csv"
        if quar_path.exists():
            with quar_path.open(encoding="utf-8") as f:
                n_quar = sum(1 for _ in f) - 1  # minus header
            report["quarantine_count"] = max(0, n_quar)
        else:
            report["quarantine_count"] = 0
        report["data_source"] = str(loader.normalized_dir.relative_to(PROJECT_ROOT))
        return report

    @app.get("/api/entities/search")
    def search(q: str = Query(..., min_length=1), limit: int = 20) -> dict:
        results = loader.search(q, limit=limit)  # type: ignore[attr-defined]
        return {
            "query": q,
            "count": len(results),
            "results": [
                {
                    "entity_id": entity.entity_id,
                    "name": entity.name,
                    "display_name": entity.display_name,
                    "entity_type": entity.entity_type,
                    "aliases": entity.aliases,
                    "annotation_length": entity.annotation_length,
                    "annotation_empty": entity.annotation_length == 0,
                    "quality_label": entity.quality_label,
                }
                for entity in results
            ],
        }

    @app.get("/api/entities/{entity_id}")
    def entity_detail(entity_id: str) -> dict:
        if entity_id not in loader._entities:  # type: ignore[attr-defined]
            raise HTTPException(status_code=404, detail=f"entity {entity_id} not found")
        overview = graph.full_overview(entity_id)  # type: ignore[attr-defined]
        entity = loader._entities[entity_id]  # type: ignore[attr-defined]
        overview["is_exogenous"] = entity.is_exogenous
        overview["family_key"] = entity.family_key
        overview["merged_from"] = entity.merged_from
        overview["display_name"] = entity.display_name
        return overview

    @app.get("/api/entities/{entity_id}/subgraph")
    def subgraph(entity_id: str, hops: int = 1, max_nodes: int = 200) -> dict:
        if entity_id not in loader._entities:  # type: ignore[attr-defined]
            raise HTTPException(status_code=404, detail=f"entity {entity_id} not found")
        return graph.subgraph(entity_id, hops=hops, max_nodes=max_nodes)  # type: ignore[attr-defined]

    @app.get("/api/pathways")
    def pathways() -> dict:
        return {
            "count": len(loader._pathways),  # type: ignore[attr-defined]
            "items": [rec.to_dict() for rec in loader._pathways.values()][:200],  # type: ignore[attr-defined]
        }

    @app.get("/api/diagnostics/duplicate-names")
    def duplicate_names(min_count: int = 2, limit: int = 100) -> dict:
        return loader.duplicate_name_report(min_count=min_count, limit=limit)  # type: ignore[attr-defined]

    @app.get("/api/perturbagens")
    def perturbagens(limit: int = 200, search: Optional[str] = None) -> dict:
        """List / search the exogenous-perturbagen pool.

        Only available when the perturbagens directory was built
        by ``scripts/build_simulation_baseline.py``. Returns 503
        otherwise so the UI can degrade gracefully.
        """
        if perturbagen_loader is None:
            raise HTTPException(status_code=503, detail="perturbagen pool not loaded")
        results = (
            perturbagen_loader.search(search, limit=limit)  # type: ignore[attr-defined]
            if search
            else list(perturbagen_loader._entities.values())[:limit]  # type: ignore[attr-defined]
        )
        return {
            "count": len(results),
            "results": [
                {
                    "entity_id": e.entity_id,
                    "name": e.name,
                    "display_name": e.display_name,
                    "entity_type": e.entity_type,
                    "is_exogenous": e.is_exogenous,
                    "source_database": e.source_database,
                }
                for e in results
            ],
        }

    @app.get("/api/runs")
    def runs_list() -> dict:
        return {"runs": runs.list_runs()}

    @app.get("/api/runs/{run_id}")
    def runs_meta(run_id: str) -> dict:
        meta = runs.get_meta(run_id)
        if meta is None:
            raise HTTPException(status_code=404, detail=f"run {run_id} not found")
        return meta

    @app.get("/api/runs/{run_id}/timeline")
    def runs_timeline(run_id: str) -> dict:
        return {"run_id": run_id, "timeline": runs.get_timeline(run_id)}

    @app.get("/api/runs/{run_id}/agents/{entity_id}")
    def runs_agent_history(run_id: str, entity_id: str) -> dict:
        history = runs.get_agent_history(run_id, entity_id)
        if history is None:
            raise HTTPException(status_code=404, detail="agent history not found")
        final_state = runs.get_final_state(run_id, entity_id)
        return {"run_id": run_id, "entity_id": entity_id, "history": history, "final_state": final_state}

    # ------------------------------------------------------------------
    # Insight endpoints (literature overlay / KG validation / scorecard).
    # All degrade gracefully when their backing artifact is absent so the
    # local diagnostic stays usable even before the GPU host has produced
    # the corresponding files.
    # ------------------------------------------------------------------

    @app.get("/api/literature/edges")
    def literature_edges() -> dict:
        return insights.literature_overview(PROJECT_ROOT, loader)

    @app.get("/api/validation/kg")
    def validation_kg() -> dict:
        return insights.kg_validation_report(PROJECT_ROOT)

    @app.get("/api/scorecard")
    def scorecard_list() -> dict:
        return {"scorecards": insights.scorecard_index(PROJECT_ROOT)}

    @app.get("/api/scorecard/{ts}")
    def scorecard_get(ts: str) -> dict:
        payload = insights.scorecard_payload(PROJECT_ROOT, ts)
        if payload is None:
            raise HTTPException(status_code=404, detail=f"scorecard {ts} not found")
        return payload

    return app


app = create_app()


if __name__ == "__main__":
    import argparse
    import uvicorn

    parser = argparse.ArgumentParser(description="E.coil diagnostic backend")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=28932)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host=args.host, port=args.port, log_level="warning")
