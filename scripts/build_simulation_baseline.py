#!/usr/bin/env python3
"""Split the normalized v2 catalog into a clean simulation baseline
and a perturbagen / quarantine library.

The normalized v2 dump currently contains 24,203 entities. About
20% of them are exogenous (drugs / chemicals / heavy metals) or
generic compound classes (e.g. "a 2-oxo acid"). The simulation's
"glucose normal growth" baseline must be **purely E. coli
endogenous** -- anything that the cell can only encounter by
external perturbation goes to a separate perturbagen library.
Generic class placeholders go to a quarantine file for the
report agent.

Re-run after a new audit to update it::

    python scripts/build_simulation_baseline.py

Output layout::

    data/normalized/simulation/
        entities.csv, edges.csv, pathways.csv, SPLIT_REPORT.json
    data/normalized/perturbagens/
        entities.csv, edges.csv, _quarantine.csv,
        _quarantine_edges.csv, SPLIT_REPORT.json
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_V2_DEFAULT = PROJECT_ROOT / "data" / "normalized" / "_v2"
AUDIT_DEFAULT = PROJECT_ROOT / "data" / "audit" / "decisions"
BASELINE_DEFAULT = PROJECT_ROOT / "data" / "normalized" / "simulation"
PERTURBAGEN_DEFAULT = PROJECT_ROOT / "data" / "normalized" / "perturbagens"

# Relations that count as "regulatory" when we look for signaling
# metabolites or sRNA with regulatory edges.
REGULATORY_RELATIONS = {
    "activates", "represses", "inhibits", "inhibits_enzyme",
    "represses_transcription", "binds", "encodes", "is_component_of",
    "transports", "catalyzes",
}

# Name patterns (case-insensitive) that mark classic bacterial
# signaling metabolites.
# Strict bacterial signaling molecules only. Pure metabolic
# intermediates (NAD+/NADH, ATP/ADP, FAD, quinones, SAM, ...) are
# folded implicitly into the reaction nodes per design and are NOT
# in this list.
SIGNALING_NAME_PATTERNS = (
    # Cyclic nucleotides / stringent response
    "camp", "cgmp", "camp", "cgmp", "cyclic amp", "cyclic gmp",
    "ppapp", "pppgpp", "ppgpp", "apppp", "ppappp",
    "guanosine penta", "guanosine tetra", "guanosine 3", "guanosine 5",
    "magic spot",
    # Cyclic di-nucleotides
    "c-di-gmp", "c-di-amp", "c-di-imp", "cyclic di-gmp", "cyclic di-amp",
    "bis(3',5')-cyclic", "bis(3,5)-cyclic",
    # Quorum sensing
    "ai-", "ai-2", "al-2", "autoinducer", "acyl-homoserine", "ahsl",
    "homoserine lactone", "hsl",
    # Indole
    "indole",
    # Specific Pseudomonas / Xanthomonas signals
    "hqno", "pqs", "hhq",
    # Stress / carbon signaling
    "alpha-ketoglutarate", "alphaketoglutarate",
    "acetyl phosphate", "acetyl-p",
)


def load_audit_decisions(audit_dir: Path) -> Dict[str, str]:
    decisions: Dict[str, str] = {}
    if not audit_dir.exists():
        return decisions
    for path in sorted(audit_dir.glob("*.jsonl")):
        for line in path.open(encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            eid = rec.get("entity_id")
            label = (rec.get("audit") or {}).get("endogenous")
            if eid and label:
                decisions[eid] = label
    return decisions


def is_endogenous(decision: Optional[str], row: Dict[str, str]) -> bool:
    if decision == "endogenous":
        return True
    if decision in {"exogenous-drug", "exogenous-chemical", "class-abstraction", "unsure"}:
        return False
    return row.get("is_exogenous", "").strip().lower() != "true"


def is_exogenous_perturbagen(decision: Optional[str]) -> bool:
    return decision in {"exogenous-drug", "exogenous-chemical"}


def is_quarantine(decision: Optional[str]) -> bool:
    return decision in {"class-abstraction", "unsure"}


def name_matches_signaling(name: str, aliases: str) -> bool:
    blob = f" {name.lower()} {aliases.lower()} "
    return any(pat in blob for pat in SIGNALING_NAME_PATTERNS)


def index_edges(edges: List[Dict[str, str]]):
    out_by_source = defaultdict(list)
    in_by_target = defaultdict(list)
    for e in edges:
        out_by_source[e["source_id"]].append((e["relation_type"], e["target_id"]))
        in_by_target[e["target_id"]].append((e["relation_type"], e["source_id"]))
    return out_by_source, in_by_target


def decide_rna(row, _decision, _out_by_source):
    # NCBI RefSeq notes carry ``feature_type=ncRNA|rRNA|tRNA``.
    # The sRNA-like working set is the ncRNA bucket. rRNA / tRNA
    # are folded implicitly into the relevant complex (ribosome,
    # tRNA-synthetase) per design.
    notes = (row.get("notes") or "").lower()
    return "feature_type=ncrna" in notes


# Target entity_types that count as "regulatory partner" for a
# small molecule signaling edge. Direct regulation of a protein or
# gene only -- not a reaction (which would just be metabolic
# participation).
REG_TARGET_TYPES = {"protein", "gene"}


def decide_signaling_metabolite(row, _decision, out_by_source, type_by_id):
    """Pick the small molecules that belong in the simulation baseline.

    The user wants the baseline to support both the regulatory
    signaling view (cAMP, ppGpp, ...) and the metabolic flow view
    (glucose -> pyruvate, ...). After ``flatten_reactions.py`` the
    produces/consumes edges go protein -> molecule, so a
    "metabolic" small molecule is any endogenous molecule that is
    the target of an in-degree edge from a baseline protein.

    A molecule is kept in the baseline if any of the following holds:

    1. Strict signaling name pattern (cAMP, ppGpp, c-di-GMP,
       AI-2, indole, ...). These are the second-messengers the
       user explicitly listed.
    2. Outgoing regulatory edge to a protein/gene
       (activates/represses/inhibits/binds) -- the molecule
       itself acts as a regulator. This picks up e.g. NADPH going
       to a redox-sensing TF.
    3. The molecule is consumed or produced by a baseline protein
       (an incoming or outgoing produces/consumes edge). This
       keeps the metabolic backbone intact: a hexokinase
       protein's consumes->glucose edge is only useful if
       glucose is also a node.
    """
    eid = row["entity_id"]
    aliases = row.get("aliases") or ""
    if name_matches_signaling(row.get("name", ""), aliases):
        return True
    has_direct_reg = any(
        rel in {"activates", "represses", "inhibits", "binds"}
        and type_by_id.get(other) in REG_TARGET_TYPES
        for rel, other in out_by_source.get(eid, [])
    )
    if has_direct_reg:
        return True
    # 3) Connected to a baseline protein via produces/consumes.
    # We need to look at *incoming* edges too, but the caller
    # already passed the out_by_source index; for incoming we'd
    # need a second pass. Instead, the small_molecule rows in
    # baseline will be re-evaluated after the protein set is
    # known, via a second pass at the bottom of main().
    return False


def decide_reaction(row, _decision, in_by_target):
    eid = row["entity_id"]
    for rel, _other in in_by_target.get(eid, []):
        if rel in {"catalyzes", "is_component_of"}:
            return True
    return False


def decide_complex(row, _decision):
    components = (row.get("components") or "").replace(",", "|").split("|")
    components = [c.strip() for c in components if c.strip()]
    if len(set(components)) < 2:
        return False
    ctype = (row.get("complex_type") or "").lower()
    if ctype and "transient" in ctype:
        return False
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--v2-dir", type=Path, default=NORMALIZED_V2_DEFAULT)
    p.add_argument("--audit-dir", type=Path, default=AUDIT_DEFAULT)
    p.add_argument("--out-baseline", type=Path, default=BASELINE_DEFAULT)
    p.add_argument("--out-perturbagen", type=Path, default=PERTURBAGEN_DEFAULT)
    args = p.parse_args()

    v2 = args.v2_dir
    if not (v2 / "entities.csv").exists():
        print(f"ERROR: {v2}/entities.csv not found", file=sys.stderr)
        return 1

    print(f"[1/5] loading audit decisions from {args.audit_dir} ...")
    decisions = load_audit_decisions(args.audit_dir)
    print(f"      loaded {len(decisions)} decisions")

    print(f"[2/5] reading entities from {v2}/entities.csv ...")
    with (v2 / "entities.csv").open(encoding="utf-8") as f:
        entity_rows = list(csv.DictReader(f))
    print(f"      {len(entity_rows)} rows")

    print(f"      reading edges from {v2}/edges.csv ...")
    with (v2 / "edges.csv").open(encoding="utf-8") as f:
        edge_rows = list(csv.DictReader(f))
    print(f"      {len(edge_rows)} rows")

    print("[3/5] building edge index for rule predicates ...")
    out_by_source, in_by_target = index_edges(edge_rows)
    type_by_id = {r["entity_id"]: r["entity_type"] for r in entity_rows}

    print("[4/5] classifying entities ...")
    baseline_ids: Set[str] = set()
    perturbagen_ids: Set[str] = set()
    quarantine_ids: Set[str] = set()
    skip_ids: Set[str] = set()
    type_decision: Dict[str, Counter] = defaultdict(Counter)

    for row in entity_rows:
        eid = row["entity_id"]
        etype = row["entity_type"]
        decision = decisions.get(eid)

        if is_exogenous_perturbagen(decision):
            perturbagen_ids.add(eid)
            type_decision["exogenous-perturbagen"][etype] += 1
            continue
        if is_quarantine(decision):
            quarantine_ids.add(eid)
            type_decision["quarantine"][etype] += 1
            continue
        if not is_endogenous(decision, row):
            perturbagen_ids.add(eid)
            type_decision["exogenous-perturbagen"][etype] += 1
            continue

        if etype == "gene":
            keep = True
        elif etype == "protein":
            keep = True
        elif etype == "rna":
            keep = decide_rna(row, decision, out_by_source)
        elif etype == "small_molecule":
            keep = decide_signaling_metabolite(row, decision, out_by_source, type_by_id)
        elif etype == "reaction":
            keep = decide_reaction(row, decision, in_by_target)
        elif etype == "complex":
            keep = decide_complex(row, decision)
        elif etype == "regulatory_region":
            keep = True
        else:
            keep = True

        if keep:
            baseline_ids.add(eid)
            type_decision["baseline"][etype] += 1
        else:
            skip_ids.add(eid)
            type_decision["dropped-from-baseline"][etype] += 1

    # Second pass: pull in any endogenous small_molecule that is
    # the target of a produces/consumes edge from a baseline
    # protein. This preserves the metabolic backbone even for
    # generic intermediates (glucose, pyruvate, ATP, ...) that
    # do not match the strict signaling-name pattern. Without
    # this, hexokinase etc. would appear as floating nodes
    # with no visible substrate.
    baseline_protein_ids = {r["entity_id"] for r in entity_rows
                            if r["entity_type"] == "protein"
                            and r["entity_id"] in baseline_ids}
    for e in edge_rows:
        if e["relation_type"] not in {"produces", "consumes",
                                       "spontaneous_produces", "spontaneous_consumes"}:
            continue
        if e["source_id"] not in baseline_protein_ids:
            continue
        target = e["target_id"]
        if target in baseline_ids:
            continue
        target_row = next((r for r in entity_rows if r["entity_id"] == target), None)
        if target_row is None:
            continue
        if target_row["entity_type"] != "small_molecule":
            continue
        if not is_endogenous(decisions.get(target), target_row):
            continue
        baseline_ids.add(target)
        # Re-classify it
        t = type_decision["dropped-from-baseline"].pop("small_molecule", 0)
        type_decision["baseline"]["small_molecule"] = type_decision["baseline"].get("small_molecule", 0) + 1
        skip_ids.discard(target)

    print("[5/5] writing outputs ...")
    baseline_edges = [
        e for e in edge_rows
        if e["source_id"] in baseline_ids and e["target_id"] in baseline_ids
    ]
    perturbagen_edges = [
        e for e in edge_rows
        if e["source_id"] in perturbagen_ids and e["target_id"] in perturbagen_ids
    ]
    quarantine_edges = [
        e for e in edge_rows
        if e["source_id"] in quarantine_ids and e["target_id"] in quarantine_ids
    ]

    def write_csv(path: Path, fieldnames, rows) -> int:
        path.parent.mkdir(parents=True, exist_ok=True)
        n = 0
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows:
                w.writerow(r)
                n += 1
        return n

    entity_fields = list(entity_rows[0].keys()) if entity_rows else []
    edge_fields = list(edge_rows[0].keys()) if edge_rows else []

    base = args.out_baseline
    pert = args.out_perturbagen
    for d in (base, pert):
        d.mkdir(parents=True, exist_ok=True)

    n_base_ent = write_csv(base / "entities.csv", entity_fields, [r for r in entity_rows if r["entity_id"] in baseline_ids])
    n_base_edge = write_csv(base / "edges.csv", edge_fields, baseline_edges)
    pathways_src = v2 / "pathways.csv"
    if pathways_src.exists():
        shutil.copy2(pathways_src, base / "pathways.csv")

    n_pert_ent = write_csv(pert / "entities.csv", entity_fields, [r for r in entity_rows if r["entity_id"] in perturbagen_ids])
    n_pert_edge = write_csv(pert / "edges.csv", edge_fields, perturbagen_edges)
    n_quar_ent = write_csv(pert / "_quarantine.csv", entity_fields, [r for r in entity_rows if r["entity_id"] in quarantine_ids])
    n_quar_edge = write_csv(pert / "_quarantine_edges.csv", edge_fields, quarantine_edges)

    report = {
        "source": str(v2),
        "audit_decisions_loaded": len(decisions),
        "baseline": {
            "entities": n_base_ent,
            "edges": n_base_edge,
            "by_type": dict(type_decision["baseline"]),
        },
        "perturbagen": {
            "entities": n_pert_ent,
            "edges": n_pert_edge,
            "by_type": dict(type_decision["exogenous-perturbagen"]),
        },
        "quarantine": {
            "entities": n_quar_ent,
            "edges": n_quar_edge,
            "by_type": dict(type_decision["quarantine"]),
        },
        "dropped_from_baseline": {
            "total": len(skip_ids),
            "by_type": dict(type_decision["dropped-from-baseline"]),
            "note": "Endogenous by audit, but failed the per-type inclusion rule. Folded implicitly into reaction/complex nodes per design.",
        },
        "inclusion_rules": {
            "gene": "all endogenous",
            "protein": "all endogenous",
            "rna": "sRNA-like: has an outgoing regulatory edge; drops mRNA / rRNA / tRNA by name",
            "small_molecule": "signaling metabolites only: (a) has an outgoing regulatory edge to a protein/gene OR (b) name matches a known signaling pattern (cAMP, ppGpp, c-di-GMP, AI-2, indole, ...)",
            "reaction": "at least one protein catalyzes it (incoming catalyzes/is_component_of edge)",
            "complex": ">= 2 distinct protein components and non-transient complex_type",
        },
        "edge_split_rule": "Both endpoints must live in the same library (per user spec).",
    }
    (base / "SPLIT_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    (pert / "SPLIT_REPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print()
    print("=" * 70)
    print(f" baseline   -> {base}")
    print(f"             {n_base_ent} entities, {n_base_edge} edges")
    for t, c in sorted(type_decision["baseline"].items(), key=lambda kv: -kv[1]):
        print(f"   {t:25s} {c}")
    print()
    print(f" perturbagen-> {pert}")
    print(f"             {n_pert_ent} entities, {n_pert_edge} edges")
    for t, c in sorted(type_decision["exogenous-perturbagen"].items(), key=lambda kv: -kv[1]):
        print(f"   {t:25s} {c}")
    print()
    print(f" quarantine -> {pert}/_quarantine.csv + _quarantine_edges.csv")
    print(f"             {n_quar_ent} entities, {n_quar_edge} edges")
    for t, c in sorted(type_decision["quarantine"].items(), key=lambda kv: -kv[1]):
        print(f"   {t:25s} {c}")
    print()
    print(f" dropped (endogenous but failed inclusion rule): {len(skip_ids)}")
    for t, c in sorted(type_decision["dropped-from-baseline"].items(), key=lambda kv: -kv[1]):
        print(f"   {t:25s} {c}")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
