"""Read-only insight endpoints: literature overlay, KG validation, scorecards.

These surface artifacts produced elsewhere in the pipeline (literature
ingest, ``scripts/validate_kg.py``, ``scripts/score_phenotypes.py`` — all of
which run on the GPU host) so the diagnostic UI can show the
literature-augmented edges, the RegulonDB validation numbers, and the
phenotype scorecard without re-running anything.

Every function degrades gracefully (``available: False``) when its backing
file is absent, so the UI can render a placeholder instead of erroring — the
same contract the perturbagen endpoint already uses.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional


# --------------------------------------------------------------------------
# Literature overlay
# --------------------------------------------------------------------------

def _base_edge_triples(loader: Any) -> set:
    """Set of ``(source_id, relation_type, target_id)`` in the loaded graph."""
    triples = set()
    for edge in getattr(loader, "_edges", []):
        triples.add((edge.source_id, edge.relation_type, edge.target_id))
    return triples


def literature_overview(project_root: Path, loader: Any = None) -> Dict[str, Any]:
    """Literature-grounded overlay edges + their overlap with the base graph.

    The overlap split is the honest-accounting number: how many literature
    edges were *already* present in the graph vs genuinely novel. This is what
    keeps "literature augmentation" from silently inflating RegulonDB recall.
    """
    path = project_root / "data" / "literature" / "literature_edges.overlay.csv"
    if not path.exists():
        return {"available": False, "count": 0, "edges": [], "overlap": None}

    base = _base_edge_triples(loader) if loader is not None else set()
    entities = getattr(loader, "_entities", {}) if loader is not None else {}

    def _name(eid: Optional[str]) -> Optional[str]:
        ent = entities.get(eid)
        if ent is None:
            return eid
        return getattr(ent, "display_name", None) or getattr(ent, "name", None) or eid

    edges: List[Dict[str, Any]] = []
    in_base = 0
    unresolved = 0
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            src = row.get("source_id")
            rel = row.get("relation_type")
            tgt = row.get("target_id")
            present = (src, rel, tgt) in base
            if present:
                in_base += 1
            resolved = bool(entities) and src in entities and tgt in entities
            if entities and not resolved:
                unresolved += 1
            edges.append({
                "source_id": src,
                "relation_type": rel,
                "target_id": tgt,
                "source_name": _name(src),
                "target_name": _name(tgt),
                "direction": row.get("direction"),
                "evidence": row.get("evidence"),
                "doi": row.get("source_record_id"),
                "notes": row.get("notes"),
                "in_base_graph": present,
                "endpoints_resolved": resolved,
            })

    return {
        "available": True,
        "count": len(edges),
        "edges": edges,
        "overlap": {
            "in_base_graph": in_base,
            "novel": len(edges) - in_base,
            "unresolved_endpoints": unresolved,
        },
    }


# --------------------------------------------------------------------------
# KG validation vs RegulonDB
# --------------------------------------------------------------------------

# "<label> ... NN.N% ... (count/total)" — the parenthetical may itself be
# preceded by other parens (e.g. the sign-agreement legend), so the leading
# match is non-greedy and the fraction's own prefix forbids parens.
_PCT_FRAC = r"([0-9.]+)%[^()\n]*\((\d+)\s*/\s*(\d+)\)"


def kg_validation_report(project_root: Path) -> Dict[str, Any]:
    """Parse the latest ``docs/KG_VALIDATION_*.md`` into headline numbers."""
    docs = sorted((project_root / "docs").glob("KG_VALIDATION_*.md"))
    if not docs:
        return {"available": False, "doc": None, "parsed": None, "markdown": None}
    path = docs[-1]
    text = path.read_text(encoding="utf-8")
    parsed: Dict[str, Any] = {}

    def grab(label: str, key: str) -> None:
        m = re.search(re.escape(label) + r"[^\n]*?" + _PCT_FRAC, text)
        if m:
            parsed[key] = {
                "pct": float(m.group(1)),
                "count": int(m.group(2)),
                "total": int(m.group(3)),
            }

    grab("present as a graph edge", "recall")
    grab("Sign agreement", "sign_accuracy")
    grab("Regulators mappable", "regulators_mappable")
    grab("Target genes mappable", "targets_mappable")
    grab("Both endpoints mappable", "both_mappable")

    return {"available": True, "doc": path.name, "parsed": parsed, "markdown": text}


# --------------------------------------------------------------------------
# Phenotype scorecards
# --------------------------------------------------------------------------

def scorecard_index(project_root: Path) -> List[Dict[str, Any]]:
    """Newest-first list of available scorecard timestamps."""
    base = project_root / "runs" / "_scorecard"
    if not base.exists():
        return []
    items: List[Dict[str, Any]] = []
    for d in sorted((p for p in base.iterdir() if p.is_dir()), key=lambda p: p.name, reverse=True):
        if (d / "scorecard.json").exists():
            items.append({"timestamp": d.name})
    return items


def scorecard_payload(project_root: Path, ts: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Return one scorecard.json (``ts=None``/``"latest"`` → newest)."""
    base = project_root / "runs" / "_scorecard"
    if not base.exists():
        return None
    if ts in (None, "latest"):
        idx = scorecard_index(project_root)
        if not idx:
            return None
        ts = idx[0]["timestamp"]
    payload = base / ts / "scorecard.json"
    if not payload.exists():
        return None
    try:
        return json.loads(payload.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return None
