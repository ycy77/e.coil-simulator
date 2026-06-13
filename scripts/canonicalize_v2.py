#!/usr/bin/env python3
"""Canonicalize the normalized E. coli graph with vLLM audit decisions.

This is the second-generation canonicalizer. Unlike the first one
(``canonicalize_normalized.py``) which only merged high-confidence
small-molecule duplicates, this version uses a combination of
deterministic rules and the vLLM audit decisions to deduplicate every
entity type:

* Each entity gets a stable ``family_key`` derived from cross-source
  identifiers (UniProt accession, EC number, KEGG compound id,
  protein component set, etc.).
* Multiple ``entity_id`` sharing the same ``(entity_type, family_key)``
  are merged into one canonical row; their ``external_ids``,
  ``aliases``, ``annotation``, and ``notes`` are unioned into the
  canonical row.
* Remaining name collisions across distinct family_keys are
  disambiguated by appending a stable source-id suffix so the
  ``display_name`` is globally unique.
* All edges are rewritten through the new canonical map; orphan edges
  are reported rather than silently dropped.
* ``is_exogenous`` is populated from the vLLM audit decisions when
  available.

The script is conservative. It writes ``data/normalized/_v2/`` and
leaves the existing files untouched until a human inspects the diff and
promotes them with the ``--apply-in-place`` flag.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED = PROJECT_ROOT / "data" / "normalized"
AUDIT_DIR = PROJECT_ROOT / "data" / "audit" / "decisions"


ENTITY_FIELDS = [
    "entity_id",
    "entity_type",
    "name",
    "aliases",
    "default_state",
    "allowed_states",
    "annotation",
    "pathways",
    "subcellular_location",
    "source_database",
    "source_id",
    "external_ids",
    "is_external",
    "is_exogenous",
    "family_key",
    "display_name",
    "merged_from",
    "complex_type",
    "is_virtual",
    "components",
    "critical_components",
    "assembly_condition",
    "notes",
]

EDGE_FIELDS = [
    "source_id",
    "relation_type",
    "target_id",
    "direction",
    "evidence",
    "source_database",
    "source_record_id",
    "notes",
]


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: List[str], rows: Iterable[Dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({field: row.get(field, "") for field in fieldnames})


def load_audit_decisions() -> Dict[str, Dict[str, Any]]:
    """Map entity_id -> audit record."""
    out: Dict[str, Dict[str, Any]] = {}
    if not AUDIT_DIR.exists():
        return out
    for p in AUDIT_DIR.glob("*.jsonl"):
        with p.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                eid = rec.get("entity_id")
                audit = rec.get("audit", {})
                if eid and audit:
                    out[eid] = audit
    return out


# ---------------------------------------------------------------------------
# Field helpers
# ---------------------------------------------------------------------------


def split_list(value: str, sep: str = "|") -> List[str]:
    if not value:
        return []
    out: List[str] = []
    for tok in value.replace(",", sep).replace(";", sep).split(sep):
        tok = tok.strip()
        if tok:
            out.append(tok)
    return out


def join_list(items: Iterable[str]) -> str:
    seen: Set[str] = set()
    out: List[str] = []
    for it in items:
        s = it.strip()
        if not s or s in seen:
            continue
        seen.add(s)
        out.append(s)
    return "|".join(out)


def normalize_name(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def hash_components(components: List[str]) -> str:
    cleaned = sorted({c.strip() for c in components if c and c.strip()})
    return "comp:" + hashlib.sha1("|".join(cleaned).encode("utf-8")).hexdigest()[:12]


def normalize_equation(eq: str) -> str:
    eq = (eq or "").lower()
    eq = re.sub(r"<=>|→|->|<->", " ", eq)
    eq = re.sub(r"[^a-z0-9]+", "", eq)
    return eq


def extract_uniprot_accession(external_ids: str) -> Optional[str]:
    for tok in split_list(external_ids):
        if tok.startswith("UniProt:") or tok.startswith("UNIPROT:"):
            return tok.split(":", 1)[1].strip()
        if re.fullmatch(r"[A-Z][A-Z0-9]{5}", tok):
            return tok
    return None


def extract_kegg_compound(external_ids: str) -> Optional[str]:
    for tok in split_list(external_ids):
        if tok.startswith("KEGG:") or tok.startswith("kegg:"):
            rest = tok.split(":", 1)[1].strip()
            if rest.startswith("C"):
                return rest
    return None


def extract_ec_number(external_ids: str, notes: str, annotation: str) -> Optional[str]:
    pat = re.compile(r"\bEC\s*[:#]?\s*(\d+\.\d+\.\d+\.\d+)\b", re.I)
    blob = " ".join([external_ids or "", notes or "", annotation or ""])
    m = pat.search(blob)
    if m:
        return m.group(1)
    for tok in split_list(external_ids):
        if re.fullmatch(r"\d+\.\d+\.\d+\.\d+", tok):
            return tok
    return None


# ---------------------------------------------------------------------------
# family_key derivation
# ---------------------------------------------------------------------------


def derive_family_key(row: Dict[str, str], etype: str) -> str:
    eid = row.get("entity_id", "")
    name = row.get("name", "")
    aliases = row.get("aliases", "")
    external_ids = row.get("external_ids", "")
    source_db = row.get("source_database", "")
    source_id = row.get("source_id", "")
    notes = row.get("notes", "")
    annotation = row.get("annotation", "")
    components = split_list(row.get("components", ""))

    if etype == "protein":
        acc = extract_uniprot_accession(external_ids)
        if acc:
            return f"protein:uniprot:{acc.lower()}"
        if name:
            return f"protein:name:{normalize_name(name)}"
        return f"protein:id:{eid.lower()}"

    if etype == "complex":
        if components:
            return hash_components(components)
        if name:
            return f"complex:name:{normalize_name(name)}"
        return f"complex:id:{eid.lower()}"

    if etype == "reaction":
        ec = extract_ec_number(external_ids, notes, annotation)
        if ec:
            return f"reaction:ec:{ec}"
        eq = normalize_equation(notes) or normalize_equation(annotation)
        if eq:
            return "reaction:eq:" + hashlib.sha1(eq.encode("utf-8")).hexdigest()[:12]
        if name:
            return f"reaction:name:{normalize_name(name)}"
        return f"reaction:id:{eid.lower()}"

    if etype == "small_molecule":
        kegg = extract_kegg_compound(external_ids)
        if kegg:
            return f"sm:kegg:{kegg.lower()}"
        if source_db == "KEGG" and source_id.startswith("C"):
            return f"sm:kegg:{source_id.lower()}"
        chebi = None
        for tok in split_list(external_ids):
            if tok.lower().startswith("chebi:"):
                chebi = tok.split(":", 1)[1].strip()
                break
        if chebi:
            return f"sm:chebi:{chebi.lower()}"
        if name:
            return f"sm:name:{normalize_name(name)}"
        return f"sm:id:{eid.lower()}"

    if etype == "gene":
        alias_set = {normalize_name(a) for a in split_list(aliases) if a}
        alias_set.add(normalize_name(name))
        alias_set.discard("")
        joined = "|".join(sorted(alias_set))
        return "gene:aliases:" + hashlib.sha1(joined.encode("utf-8")).hexdigest()[:12]

    if etype == "rna":
        if source_id:
            return f"rna:id:{source_id.lower()}"
        if name:
            return f"rna:name:{normalize_name(name)}"
        return f"rna:id:{eid.lower()}"

    return f"{etype}:id:{eid.lower()}"


# ---------------------------------------------------------------------------
# merge
# ---------------------------------------------------------------------------


SOURCE_PRIORITY = {
    "UniProt": 100,
    "NCBI RefSeq": 95,
    "KEGG": 90,
    "RegulonDB": 85,
    "EcoCyc": 80,
}


def source_score(row: Dict[str, str]) -> int:
    db = (row.get("source_database") or "").split("|")[0].strip()
    return SOURCE_PRIORITY.get(db, 50)


def merge_group(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    rows_sorted = sorted(rows, key=lambda r: (-source_score(r), r.get("entity_id", "")))
    primary = rows_sorted[0]
    aliases: Set[str] = set()
    external: Set[str] = set()
    notes: List[str] = []
    annotations: List[str] = []
    pathways: Set[str] = set()
    source_dbs: Set[str] = set()
    for r in rows_sorted:
        for a in split_list(r.get("aliases", "")):
            aliases.add(a)
        if primary.get("name") and r.get("name") and r.get("name") != primary.get("name"):
            aliases.add(r["name"])
        for x in split_list(r.get("external_ids", "")):
            external.add(x)
        for p in split_list(r.get("pathways", "")):
            pathways.add(p)
        if r.get("notes"):
            notes.append(f"{r.get('entity_id', '')}: {r['notes']}")
        if r.get("annotation"):
            annotations.append(r["annotation"])
        if r.get("source_database"):
            for db in split_list(r["source_database"]):
                source_dbs.add(db)
    merged = {field: primary.get(field, "") for field in ENTITY_FIELDS}
    merged["aliases"] = join_list(list(aliases) + split_list(primary.get("aliases", "")))
    merged["external_ids"] = join_list(list(external) + split_list(primary.get("external_ids", "")))
    merged["pathways"] = join_list(list(pathways) + split_list(primary.get("pathways", "")))
    merged["notes"] = " | ".join([n for n in notes if n and n.strip()])[:4000]
    # annotation: keep the longest informative one
    annotations_sorted = sorted([a for a in annotations if a], key=len, reverse=True)
    if annotations_sorted:
        merged["annotation"] = annotations_sorted[0]
    if source_dbs:
        merged["source_database"] = join_list(sorted(source_dbs))
    return merged


# ---------------------------------------------------------------------------
# display_name disambiguation
# ---------------------------------------------------------------------------


def make_unique_display_names(rows: List[Dict[str, str]]) -> Dict[str, str]:
    """Map entity_id -> final display_name (already-canonical rows)."""
    groups: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for r in rows:
        name = (r.get("name") or "").strip()
        if not name:
            continue
        groups[(r.get("entity_type", ""), name.lower())].append(r)

    name_overrides: Dict[str, str] = {}
    for (etype, _), group in groups.items():
        if len(group) <= 1:
            continue
        # Sort for stable suffix assignment.
        group_sorted = sorted(group, key=lambda r: r.get("entity_id", ""))
        for idx, row in enumerate(group_sorted, start=2):
            src_id = (row.get("source_id") or row.get("entity_id") or "").strip()
            short = src_id.split(".")[-1][:24] if src_id else ""
            base = (row.get("name") or row.get("entity_id") or "").strip()
            new_name = f"{base} ({short} #{idx})" if short else f"{base} #{idx}"
            name_overrides[row.get("entity_id", "")] = new_name

    out: Dict[str, str] = {}
    for r in rows:
        eid = r.get("entity_id", "")
        if eid in name_overrides:
            out[eid] = name_overrides[eid]
        else:
            out[eid] = (r.get("name") or eid).strip()
    # Second pass: collision-free across the whole catalog. Some
    # `name` values are empty after merge (the primary row had no
    # name) so we fall back to the canonical id, then dedupe across
    # every row including those.
    lower_counter: Dict[str, int] = defaultdict(int)
    for eid, dn in out.items():
        lower_counter[dn.lower()] += 1
    dup_strings = {s for s, c in lower_counter.items() if c > 1}
    if dup_strings:
        # Re-emit duplicates with a stable id-suffix.
        suffix_owners: Dict[str, List[str]] = defaultdict(list)
        for eid, dn in out.items():
            if dn.lower() in dup_strings:
                suffix_owners[dn.lower()].append(eid)
        for _low, ids in suffix_owners.items():
            ids.sort()
            for i, eid in enumerate(ids, start=2):
                src_id = next((r.get("source_id", "") for r in rows if r.get("entity_id") == eid), "") or eid
                short = src_id.split(".")[-1][:24] if src_id else ""
                base = out[eid]
                out[eid] = f"{base} ({short} #{i})" if short else f"{base} #{i}"
    return out


# ---------------------------------------------------------------------------
# edges
# ---------------------------------------------------------------------------


def rewrite_edges(
    edges: List[Dict[str, str]],
    entity_map: Dict[str, str],
    valid_entity_ids: Set[str],
    pathway_ids: Set[str],
) -> Tuple[List[Dict[str, str]], Dict[str, int]]:
    seen_keys: Set[Tuple[str, str, str]] = set()
    out: List[Dict[str, str]] = []
    orphan = 0
    for r in edges:
        src = entity_map.get(r.get("source_id", ""), r.get("source_id", ""))
        tgt = entity_map.get(r.get("target_id", ""), r.get("target_id", ""))
        relation = r.get("relation_type", "")
        if src not in valid_entity_ids:
            orphan += 1
            continue
        if tgt not in valid_entity_ids and not (relation == "participates_in" and tgt in pathway_ids):
            orphan += 1
            continue
        key = (src, relation, tgt)
        if key in seen_keys:
            continue
        seen_keys.add(key)
        cleaned = {field: r.get(field, "") for field in EDGE_FIELDS}
        cleaned["source_id"] = src
        cleaned["target_id"] = tgt
        out.append(cleaned)
    return out, {"orphan_edges_removed": orphan}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--out-dir", type=Path, default=NORMALIZED / "_v2")
    parser.add_argument("--apply-in-place", action="store_true")
    parser.add_argument("--report-path", type=Path, default=NORMALIZED / "canonicalization_report_v2.json")
    args = parser.parse_args()

    src_dir = args.normalized_dir
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    entities = read_csv(src_dir / "entities.csv")
    edges = read_csv(src_dir / "edges.csv")
    pathways = read_csv(src_dir / "pathways.csv")
    audit = load_audit_decisions()

    # Group by (entity_type, family_key).
    groups: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    family_key_by_id: Dict[str, str] = {}
    for row in entities:
        et = row.get("entity_type", "").strip()
        fk = derive_family_key(row, et)
        family_key_by_id[row.get("entity_id", "")] = fk
        groups[(et, fk)].append(row)

    canonical_map: Dict[str, str] = {}  # old -> canonical id
    canonical_rows: List[Dict[str, str]] = []
    merge_decisions: List[Dict[str, str]] = []
    for (etype, fk), members in groups.items():
        if len(members) == 1:
            row = {field: members[0].get(field, "") for field in ENTITY_FIELDS}
            row["family_key"] = fk
            row["merged_from"] = members[0].get("entity_id", "")
            row["display_name"] = (members[0].get("name") or members[0].get("entity_id", "")).strip()
            canonical_map[members[0].get("entity_id", "")] = members[0].get("entity_id", "")
            canonical_rows.append(row)
            continue
        merged = merge_group(members)
        merged["family_key"] = fk
        canonical_id = merged["entity_id"]
        for m in members:
            mid = m.get("entity_id", "")
            canonical_map[mid] = canonical_id
            if mid != canonical_id:
                merge_decisions.append(
                    {
                        "old_entity_id": mid,
                        "canonical_entity_id": canonical_id,
                        "family_key": fk,
                        "reason": "same family_key via deterministic merge",
                        "confidence": "high",
                    }
                )
        merged["merged_from"] = "|".join(sorted(m.get("entity_id", "") for m in members))
        canonical_rows.append(merged)

    # Apply vLLM audit decisions for is_exogenous + name uniqueness hint.
    class_abstraction_ids: Set[str] = set()
    for r in canonical_rows:
        eid = r.get("entity_id", "")
        decision = audit.get(eid)
        if not decision:
            r["is_exogenous"] = "false"
            continue
        cls = decision.get("endogenous", "unsure")
        if cls in ("exogenous-drug", "exogenous-chemical", "class-abstraction"):
            r["is_exogenous"] = "true"
            if cls == "class-abstraction":
                class_abstraction_ids.add(eid)
        elif cls == "endogenous":
            r["is_exogenous"] = "false"
        else:
            r["is_exogenous"] = "unsure"
        collides = decision.get("collides_with", []) or []
        if collides:
            note = r.get("notes", "")
            extra = f"audit_collides_with={','.join(sorted(set(collides)))}"
            r["notes"] = (note + " | " + extra) if note else extra

    # Stable, globally-unique display names.
    display_names = make_unique_display_names(canonical_rows)
    for r in canonical_rows:
        r["display_name"] = display_names.get(r.get("entity_id", ""), r.get("name", ""))

    # Verify uniqueness invariants.
    name_counts: Counter = Counter()
    type_name_pairs: Set[Tuple[str, str]] = set()
    for r in canonical_rows:
        nm = (r.get("display_name") or "").strip().lower()
        if nm:
            name_counts[nm] += 1
        pair = (r.get("entity_type", ""), (r.get("name") or "").strip().lower())
        type_name_pairs.add(pair)
    dup_names = {k: v for k, v in name_counts.items() if v > 1}

    # Rewrite edges.
    valid_ids = {r["entity_id"] for r in canonical_rows}
    pathway_ids = {p["pathway_id"] for p in pathways}
    new_edges, edge_stats = rewrite_edges(edges, canonical_map, valid_ids, pathway_ids)

    # Write outputs.
    write_csv(out_dir / "entities.csv", ENTITY_FIELDS, canonical_rows)
    write_csv(out_dir / "edges.csv", EDGE_FIELDS, new_edges)
    write_csv(out_dir / "pathways.csv", list(pathways[0].keys()) if pathways else ["pathway_id", "pathway_name", "source", "description", "organism"], pathways)
    write_csv(
        out_dir / "canonical_entity_map_v2.csv",
        ["old_entity_id", "canonical_entity_id", "family_key", "reason", "confidence"],
        merge_decisions,
    )

    report = {
        "input_counts": {
            "entities": len(entities),
            "edges": len(edges),
            "families": len(groups),
        },
        "output_counts": {
            "entities": len(canonical_rows),
            "edges": len(new_edges),
            "merged": len(merge_decisions),
            "class_abstraction_entities": len(class_abstraction_ids),
        },
        "edge_stats": edge_stats,
        "name_uniqueness": {
            "duplicate_display_names": dup_names,
            "unique_display_name_ratio": 1.0 if not dup_names else round(
                sum(1 for v in name_counts.values() if v == 1) / max(len(name_counts), 1), 4
            ),
        },
        "audit_coverage": {
            "with_audit": sum(1 for r in canonical_rows if r.get("entity_id") in audit),
            "without_audit": sum(1 for r in canonical_rows if r.get("entity_id") not in audit),
        },
    }
    (out_dir / "canonicalization_report_v2.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if args.apply_in_place:
        # Promote _v2/* into the canonical normalized dir (with backup).
        for name in ("entities.csv", "edges.csv", "pathways.csv"):
            backup = src_dir / (name + ".pre_canonical_v2")
            if not backup.exists():
                shutil.copy2(src_dir / name, backup)
            shutil.copy2(out_dir / name, src_dir / name)
        shutil.copy2(out_dir / "canonical_entity_map_v2.csv", src_dir / "canonical_entity_map_v2.csv")
        shutil.copy2(out_dir / "canonicalization_report_v2.json", src_dir / "canonicalization_report_v2.json")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())