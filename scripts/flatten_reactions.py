#!/usr/bin/env python3
"""Flatten reaction nodes into edge payload.

The normalized v2 catalog treats biochemical reactions as nodes.
That makes the graph artificially deep: ``gene --encodes--> protein
--catalyzes--> reaction --is_product_of--> molecule`` requires
two hops to express a single conceptual event ("the enzyme turns
substrate A into product B"). Worse, hiding the conversion behind
a node means downstream simulations cannot react to a single edge
deletion; they have to walk the bipartite structure.

This script makes each reaction a *transformation event* on the
edge. The reaction node is removed; its data (equation, EC number,
pathway membership) is attached as payload to two new edge types
per reaction::

    catalyst --produces--> product       (payload: reactants,
                                          reaction_id, ec_number,
                                          pathway)
    catalyst --consumes--> substrate     (payload: products,
                                          reaction_id, ec_number,
                                          pathway)

Both edges are needed for the inhibition-propagation story: an
inhibited enzyme must (a) stop producing the product and (b) stop
consuming the substrate. Without the consumes edge, the substrate
accumulates silently, which is wrong for the metabolic model.

Spontaneous (un-catalyzed) reactions get an empty source. We use
the literal sentinel ``__spontaneous__`` so the loader can spot
them; downstream code can either treat them as free-floating
events or filter them out.

What is preserved::

  * ``is_component_of``   (protein -> complex)        -- complex assembly
  * ``participates_in``   (entity -> pathway)         -- pathway tag
  * ``encodes``           (gene -> protein)           -- direct
  * ``activates`` /
    ``represses`` /
    ``inhibits`` /
    ``binds``             (TF/protein -> protein/gene/rxn-target)
  * ``transports``        (protein -> small_molecule) -- transporter

What is dropped along with the reaction nodes::

  * ``is_substrate_of``    (molecule -> reaction)
  * ``is_product_of``      (reaction -> molecule)
  * ``catalyzes``          (protein/complex -> reaction)
  * ``participates_in``    (reaction -> pathway)      -- recoverable
                            by joining through the catalyst's own
                            pathway membership.

The original edges are backed up to ``edges_original.csv`` next to
``edges.csv`` so the unflattened topology is always recoverable.

Usage::

    python scripts/flatten_reactions.py
    python scripts/flatten_reactions.py --v2-dir data/normalized/_v2
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_V2 = PROJECT_ROOT / "data" / "normalized" / "_v2"
SPONTANEOUS_SOURCE = "__spontaneous__"

# Edge relation types we drop entirely once the reaction nodes are
# gone -- they all reference a reaction node as source or target.
DROP_RELATIONS = {
    "is_substrate_of",
    "is_product_of",
    "catalyzes",
}

# Source-side relation types we want to keep only when neither
# endpoint is a reaction. ``participates_in`` is allowed only when
# the *target* is a pathway (we still keep pathway membership for
# non-reaction sources).
def keep_participates_in(edge: Dict[str, str], type_by_id: Dict[str, str]) -> bool:
    if type_by_id.get(edge["source_id"]) == "reaction":
        return False
    if type_by_id.get(edge["target_id"]) == "pathway":
        return True
    # Anything else (typically a reaction target) is dropped
    return False


def read_csv(path: Path) -> Tuple[List[Dict[str, str]], List[str]]:
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys()) if rows else []
    return rows, fields


def write_csv(path: Path, fieldnames: List[str], rows: Iterable[Dict[str, str]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
            n += 1
    return n


def extract_ec_number(annotation: str, name: str, aliases: str) -> str:
    """Best-effort EC-number extraction. EC looks like ``1.1.1.1``."""
    for blob in (annotation, name, aliases):
        m = re.search(r"\bEC\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\b", blob or "")
        if m:
            return m.group(1)
        m = re.search(r"\b([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\b", blob or "")
        if m:
            return m.group(1)
    return ""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--v2-dir", type=Path, default=DEFAULT_V2)
    args = p.parse_args()

    v2 = args.v2_dir
    if not (v2 / "entities.csv").exists() or not (v2 / "edges.csv").exists():
        print(f"ERROR: {v2}/entities.csv and edges.csv are required", file=sys.stderr)
        return 1

    print(f"[1/5] reading entities from {v2}/entities.csv ...")
    entity_rows, _ = read_csv(v2 / "entities.csv")
    type_by_id = {r["entity_id"]: r["entity_type"] for r in entity_rows}
    reaction_ids: Set[str] = {r["entity_id"] for r in entity_rows if r["entity_type"] == "reaction"}
    print(f"      {len(entity_rows)} entities, {len(reaction_ids)} reactions")

    print(f"[2/5] reading edges from {v2}/edges.csv ...")
    edge_rows, edge_fields = read_csv(v2 / "edges.csv")
    print(f"      {len(edge_rows)} edges")

    print("[3/5] building reaction index ...")
    # reaction_id -> { 'catalysts': [(source_id, edge), ...],
    #                  'substrates': [source_id, ...],
    #                  'products':   [target_id, ...],
    #                  'pathways':   [pathway_id, ...] (from reaction -> pathway) }
    rxn_index: Dict[str, Dict[str, List]] = defaultdict(
        lambda: {"catalysts": [], "substrates": [], "products": [], "pathways": []}
    )
    for e in edge_rows:
        if e["relation_type"] == "catalyzes" and e["target_id"] in reaction_ids:
            rxn_index[e["target_id"]]["catalysts"].append((e["source_id"], e))
        elif e["relation_type"] == "is_substrate_of" and e["target_id"] in reaction_ids:
            rxn_index[e["target_id"]]["substrates"].append(e["source_id"])
        elif e["relation_type"] == "is_product_of" and e["target_id"] in reaction_ids:
            # Convention: molecule --is_product_of--> reaction. Source
            # is the product molecule, target is the reaction.
            rxn_index[e["target_id"]]["products"].append(e["source_id"])
        elif e["relation_type"] == "participates_in" and e["source_id"] in reaction_ids:
            rxn_index[e["source_id"]]["pathways"].append(e["target_id"])

    # Cache reaction entity metadata for payload
    rxn_meta = {r["entity_id"]: r for r in entity_rows if r["entity_type"] == "reaction"}

    n_with_cat = sum(1 for rid in reaction_ids if rxn_index[rid]["catalysts"])
    n_without_cat = len(reaction_ids) - n_with_cat
    n_with_sub = sum(1 for rid in reaction_ids if rxn_index[rid]["substrates"])
    n_with_prod = sum(1 for rid in reaction_ids if rxn_index[rid]["products"])
    print(f"      reactions with catalyst:     {n_with_cat}")
    print(f"      reactions without catalyst:  {n_without_cat}")
    print(f"      reactions with substrate:    {n_with_sub}")
    print(f"      reactions with product:      {n_with_prod}")

    print("[4/5] generating flattened edges ...")
    new_edge_fields = list(edge_fields) + [
        "reaction_id", "reactants", "products", "ec_number", "pathway",
    ]
    new_edge_rows: List[Dict[str, str]] = []

    for rid, parts in rxn_index.items():
        meta = rxn_meta.get(rid, {})
        ec = extract_ec_number(
            meta.get("annotation", ""), meta.get("name", ""), meta.get("aliases", ""),
        )
        pathway_str = "|".join(sorted(set(parts["pathways"])))
        substrates = parts["substrates"]
        products = parts["products"]
        catalysts = [c for c, _ in parts["catalysts"]]
        # Use the first catalyzes edge as the provenance source.
        cat_edge = parts["catalysts"][0][1] if parts["catalysts"] else {}

        # Use the sentinel if there is no catalyst. We still want
        # to keep the event in the data so that downstream
        # simulations can see the conversion; downstream code
        # can choose to ignore source-less edges.
        sources = catalysts or [SPONTANEOUS_SOURCE]
        for catalyst in sources:
            for product in products:
                reactants_str = "|".join(substrates)
                products_str = product  # only this one in the loop
                new_edge_rows.append({
                    "source_id": catalyst,
                    "target_id": product,
                    "relation_type": "produces" if catalyst != SPONTANEOUS_SOURCE else "spontaneous_produces",
                    "direction": "directed",
                    "evidence": cat_edge.get("evidence", ""),
                    "source_database": cat_edge.get("source_database", "") or meta.get("source_database", ""),
                    "source_record_id": cat_edge.get("source_record_id", "") or rid,
                    "notes": cat_edge.get("notes", ""),
                    "reaction_id": rid,
                    "reactants": reactants_str,
                    "products": products_str,
                    "ec_number": ec,
                    "pathway": pathway_str,
                })
            for substrate in substrates:
                new_edge_rows.append({
                    "source_id": catalyst,
                    "target_id": substrate,
                    "relation_type": "consumes" if catalyst != SPONTANEOUS_SOURCE else "spontaneous_consumes",
                    "direction": "directed",
                    "evidence": cat_edge.get("evidence", ""),
                    "source_database": cat_edge.get("source_database", "") or meta.get("source_database", ""),
                    "source_record_id": cat_edge.get("source_record_id", "") or rid,
                    "notes": cat_edge.get("notes", ""),
                    "reaction_id": rid,
                    "reactants": substrate,
                    "products": "|".join(products),
                    "ec_number": ec,
                    "pathway": pathway_str,
                })

    # Carry over non-reaction edges (filter DROP_RELATIONS, filter
    # participates_in that goes from a reaction).
    for e in edge_rows:
        rel = e["relation_type"]
        if rel in DROP_RELATIONS:
            continue
        if e["source_id"] in reaction_ids or e["target_id"] in reaction_ids:
            # Almost everything touching a reaction node is gone.
            # Exception: pathway targets stay (handled below).
            if rel == "participates_in" and e["source_id"] in reaction_ids and type_by_id.get(e["target_id"]) == "pathway":
                continue
            # Otherwise drop dangling reference
            continue
        if rel == "participates_in" and not keep_participates_in(e, type_by_id):
            continue
        new_e = dict(e)
        # Initialize new columns if absent (older edges lack them)
        for col in ("reaction_id", "reactants", "products", "ec_number", "pathway"):
            new_e.setdefault(col, "")
        new_edge_rows.append(new_e)

    print(f"      produced {len(new_edge_rows)} flattened edges (was {len(edge_rows)})")
    print(f"      breakdown by relation:")
    from collections import Counter
    for rel, c in Counter(r["relation_type"] for r in new_edge_rows).most_common():
        print(f"        {rel:30s} {c}")

    print("[5/5] writing outputs ...")
    # Backup original edges
    backup = v2 / "edges_original.csv"
    if not backup.exists():
        shutil.copy2(v2 / "edges.csv", backup)
        print(f"      backed up original edges -> {backup}")
    else:
        print(f"      {backup} already exists, skipping backup")

    # Write new entities (drop reactions)
    new_entity_rows = [r for r in entity_rows if r["entity_type"] != "reaction"]
    entity_fields = list(entity_rows[0].keys()) if entity_rows else []
    n_ent = write_csv(v2 / "entities.csv", entity_fields, new_entity_rows)
    n_edge = write_csv(v2 / "edges.csv", new_edge_fields, new_edge_rows)

    print()
    print("=" * 70)
    print(f" entities:  {len(entity_rows)} -> {n_ent}  (dropped {len(entity_rows)-n_ent} reactions)")
    print(f" edges:     {len(edge_rows)} -> {n_edge}")
    print(f" backup:    {backup}  (original, untouched)")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
