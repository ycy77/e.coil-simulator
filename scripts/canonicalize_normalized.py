#!/usr/bin/env python3
"""Canonicalize normalized E.coil graph tables after multi-source merges.

This script is deliberately conservative. It removes graph-breaking edges,
collapses repeated source/target/relation edges into one multi-source edge, and
canonicalizes only high-confidence small-molecule duplicates.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


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

PATHWAY_FIELDS = ["pathway_id", "pathway_name", "source", "description", "organism"]
CANONICAL_MAP_FIELDS = ["old_entity_id", "canonical_entity_id", "reason", "confidence"]

GENERIC_MOLECULE_NAMES = {
    "h",
    "dna",
    "rna",
    "light",
    "water",
    "protein",
    "a protein",
    "a peptide",
    "an amino acid",
    "a carbohydrate",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=Path("data/normalized"))
    parser.add_argument("--no-backup", action="store_true")
    args = parser.parse_args()

    normalized_dir = args.normalized_dir
    entities = read_csv(normalized_dir / "entities.csv")
    edges = read_csv(normalized_dir / "edges.csv")
    pathways = read_csv(normalized_dir / "pathways.csv")

    canonical_map, molecule_report = build_small_molecule_canonical_map(entities)
    canonical_entities = apply_entity_canonicalization(entities, canonical_map)
    canonical_entity_ids = {row["entity_id"] for row in canonical_entities}
    pathway_ids = {row["pathway_id"] for row in pathways}
    canonical_edges, edge_report = canonicalize_edges(edges, canonical_map, canonical_entity_ids, pathway_ids)
    pathway_report = pathway_duplicate_report(pathways)

    report = {
        "input_counts": {
            "entities": len(entities),
            "edges": len(edges),
            "pathways": len(pathways),
        },
        "output_counts": {
            "entities": len(canonical_entities),
            "edges": len(canonical_edges),
            "pathways": len(pathways),
        },
        "small_molecule_canonicalization": molecule_report,
        "edge_canonicalization": edge_report,
        "pathway_duplicate_report": pathway_report,
    }

    if not args.no_backup:
        backup(normalized_dir / "entities.csv")
        backup(normalized_dir / "edges.csv")
        backup(normalized_dir / "pathways.csv")

    write_csv(normalized_dir / "entities.csv", ENTITY_FIELDS, canonical_entities)
    write_csv(normalized_dir / "edges.csv", EDGE_FIELDS, canonical_edges)
    write_csv(
        normalized_dir / "canonical_entity_map.csv",
        CANONICAL_MAP_FIELDS,
        [
            {
                "old_entity_id": old,
                "canonical_entity_id": spec["canonical"],
                "reason": spec["reason"],
                "confidence": spec["confidence"],
            }
            for old, spec in sorted(canonical_map.items())
        ],
    )
    (normalized_dir / "canonicalization_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"canonicalized entities {len(entities)} -> {len(canonical_entities)}")
    print(f"canonicalized edges {len(edges)} -> {len(canonical_edges)}")
    print(f"canonical mappings {len(canonical_map)}")
    print(f"removed invalid edges {edge_report['invalid_edges_removed']}")
    print(f"collapsed duplicate edge groups {edge_report['duplicate_edge_groups_collapsed']}")
    return 0


def build_small_molecule_canonical_map(entities: list[dict[str, str]]) -> tuple[dict[str, dict[str, str]], dict]:
    kegg_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    ecocyc_fallback_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in entities:
        if row.get("entity_type") != "small_molecule":
            continue
        name = normalize_name(row.get("name", ""))
        if not name:
            continue
        if row.get("source_database") == "KEGG" and row.get("entity_id", "").startswith("molecule.C"):
            kegg_by_name[name].append(row)
        elif row.get("source_database") == "EcoCyc" and ".ecocyc." in row.get("entity_id", ""):
            ecocyc_fallback_by_name[name].append(row)

    canonical_map: dict[str, dict[str, str]] = {}
    rejected = Counter()
    reviewed = 0
    examples = []
    for name, eco_rows in ecocyc_fallback_by_name.items():
        if name not in kegg_by_name:
            continue
        reviewed += len(eco_rows)
        kegg_rows = kegg_by_name[name]
        if len(eco_rows) != 1:
            rejected["multiple_ecocyc_same_name"] += len(eco_rows)
            continue
        if len(kegg_rows) != 1:
            rejected["multiple_kegg_same_name"] += len(eco_rows)
            continue
        if not safe_molecule_name(name):
            rejected["generic_or_unsafe_name"] += len(eco_rows)
            continue
        eco = eco_rows[0]
        kegg = kegg_rows[0]
        if conflicting_stereochemistry(eco.get("source_id", ""), kegg.get("name", "")):
            rejected["possible_stereochemistry_conflict"] += 1
            continue
        canonical_map[eco["entity_id"]] = {
            "canonical": kegg["entity_id"],
            "reason": f"exact normalized molecule name match: {name}",
            "confidence": "medium",
        }
        if len(examples) < 20:
            examples.append(
                {
                    "old_entity_id": eco["entity_id"],
                    "canonical_entity_id": kegg["entity_id"],
                    "name": name,
                }
            )

    return canonical_map, {
        "reviewed_exact_name_candidates": reviewed,
        "canonicalized": len(canonical_map),
        "rejected": dict(rejected),
        "examples": examples,
    }


def apply_entity_canonicalization(rows: list[dict[str, str]], canonical_map: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    canonical_ids = {spec["canonical"] for spec in canonical_map.values()}
    alias_payload: dict[str, list[str]] = defaultdict(list)
    external_payload: dict[str, list[str]] = defaultdict(list)
    notes_payload: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        entity_id = row.get("entity_id", "")
        if entity_id not in canonical_map:
            continue
        canonical_id = canonical_map[entity_id]["canonical"]
        alias_payload[canonical_id].extend(split_aliases(row.get("aliases", "")))
        alias_payload[canonical_id].append(row.get("name", ""))
        external_payload[canonical_id].extend(split_multi(row.get("external_ids", "")))
        external_payload[canonical_id].append(f"canonicalized_from:{entity_id}")
        notes_payload[canonical_id].append(f"{entity_id}: {row.get('source_database')}:{row.get('source_id')}")

    result = []
    for row in rows:
        entity_id = row.get("entity_id", "")
        if entity_id in canonical_map:
            continue
        merged = {field: row.get(field, "") for field in ENTITY_FIELDS}
        if entity_id in canonical_ids:
            aliases = unique_keep_order([*split_aliases(merged.get("aliases", "")), *alias_payload.get(entity_id, [])])
            external = unique_keep_order([*split_multi(merged.get("external_ids", "")), *external_payload.get(entity_id, [])])
            notes = unique_keep_order([merged.get("notes", ""), *notes_payload.get(entity_id, [])])
            merged["aliases"] = "|".join(item for item in aliases if item)
            merged["external_ids"] = "|".join(item for item in external if item)
            merged["notes"] = " | ".join(item for item in notes if item)
        result.append(merged)
    return result


def canonicalize_edges(
    rows: list[dict[str, str]],
    canonical_map: dict[str, dict[str, str]],
    entity_ids: set[str],
    pathway_ids: set[str],
) -> tuple[list[dict[str, str]], dict]:
    invalid = Counter()
    normalized_rows = []
    for row in rows:
        source = canonical_map.get(row.get("source_id", ""), {}).get("canonical", row.get("source_id", ""))
        target = canonical_map.get(row.get("target_id", ""), {}).get("canonical", row.get("target_id", ""))
        relation = row.get("relation_type", "")
        if source == target:
            invalid["self_edge_after_canonicalization"] += 1
            continue
        source_ok = source in entity_ids
        target_ok = target in entity_ids or (relation == "participates_in" and target in pathway_ids)
        if not source_ok or not target_ok:
            invalid[relation or "unknown"] += 1
            continue
        cleaned = {field: row.get(field, "") for field in EDGE_FIELDS}
        cleaned["source_id"] = source
        cleaned["target_id"] = target
        normalized_rows.append(cleaned)

    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in normalized_rows:
        groups[(row["source_id"], row["relation_type"], row["target_id"])].append(row)

    output = []
    duplicate_groups = 0
    duplicate_rows_removed = 0
    for key in sorted(groups):
        group = groups[key]
        if len(group) > 1:
            duplicate_groups += 1
            duplicate_rows_removed += len(group) - 1
        output.append(merge_edge_group(group))

    return output, {
        "invalid_edges_removed": sum(invalid.values()),
        "invalid_edges_by_relation": dict(invalid),
        "duplicate_edge_groups_collapsed": duplicate_groups,
        "duplicate_edge_rows_removed": duplicate_rows_removed,
    }


def merge_edge_group(group: list[dict[str, str]]) -> dict[str, str]:
    first = group[0]
    source_databases = unique_keep_order(item for row in group for item in split_sources(row.get("source_database", "")))
    evidences = unique_keep_order(row.get("evidence", "") for row in group if row.get("evidence", ""))
    records = unique_keep_order(row.get("source_record_id", "") for row in group if row.get("source_record_id", ""))
    notes = unique_keep_order(row.get("notes", "") for row in group if row.get("notes", ""))
    directions = unique_keep_order(row.get("direction", "") for row in group if row.get("direction", ""))
    return {
        "source_id": first["source_id"],
        "relation_type": first["relation_type"],
        "target_id": first["target_id"],
        "direction": "|".join(directions) if directions else "directed",
        "evidence": strongest_evidence(evidences),
        "source_database": "|".join(source_databases),
        "source_record_id": "|".join(records[:20]),
        "notes": merge_notes(notes, len(records)),
    }


def pathway_duplicate_report(rows: list[dict[str, str]]) -> dict:
    by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_name[normalize_name(row.get("pathway_name", ""))].append(row)
    groups = []
    for name, vals in by_name.items():
        if name and len(vals) > 1:
            groups.append(
                {
                    "normalized_name": name,
                    "members": [{"pathway_id": row["pathway_id"], "source": row["source"]} for row in vals],
                }
            )
    groups.sort(key=lambda item: item["normalized_name"])
    return {
        "same_name_groups": len(groups),
        "groups": groups[:50],
        "policy": "Pathways are retained as source-specific metadata; exact/near equivalence is reported but not merged.",
    }


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def backup(path: Path) -> None:
    backup_path = path.with_suffix(path.suffix + ".pre_canonical")
    if not backup_path.exists():
        shutil.copy2(path, backup_path)


def normalize_name(text: str) -> str:
    text = html.unescape(text or "").lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def safe_molecule_name(name: str) -> bool:
    if not name or name in GENERIC_MOLECULE_NAMES:
        return False
    if len(name) <= 2:
        return False
    generic_words = {"class", "group", "placeholder", "holder", "compound", "compounds", "derivatives"}
    return not any(word in name.split() for word in generic_words)


def conflicting_stereochemistry(ecocyc_source_id: str, kegg_name: str) -> bool:
    # Avoid merging named stereoisomer variants into a generic KEGG compound.
    source = normalize_name(ecocyc_source_id)
    kegg = normalize_name(kegg_name)
    stereochemical = {"alpha", "beta", "d", "l", "r", "s", "cis", "trans"}
    source_tokens = set(source.split())
    kegg_tokens = set(kegg.split())
    extra = (source_tokens - kegg_tokens) & stereochemical
    return bool(extra and len(source_tokens) > len(kegg_tokens))


def split_aliases(text: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|;]", text or "") if item.strip()]


def split_multi(text: str) -> list[str]:
    return [item.strip() for item in (text or "").split("|") if item.strip()]


def split_sources(text: str) -> list[str]:
    return [item.strip() for item in (text or "").split("|") if item.strip()]


def unique_keep_order(items: Iterable[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        item = item.strip() if isinstance(item, str) else item
        if not item or item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def strongest_evidence(values: list[str]) -> str:
    order = {"confirmed": 5, "C": 5, "strong": 4, "S": 4, "database": 3, "curated": 3, "weak": 1}
    if not values:
        return "database"
    return max(values, key=lambda item: order.get(item, order.get(item.upper(), 2)))


def merge_notes(notes: list[str], record_count: int) -> str:
    notes = notes[:12]
    text = " | ".join(notes)
    if record_count > 20:
        text = f"{text} | source_record_id_truncated_total={record_count}" if text else f"source_record_id_truncated_total={record_count}"
    return text[:4000]


if __name__ == "__main__":
    raise SystemExit(main())
