#!/usr/bin/env python3
"""Export normalized E.coil entities as Obsidian Markdown notes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--normalized-dir", type=Path, default=Path("data/normalized"))
    parser.add_argument("--enriched-file", type=Path, default=Path("data/enriched/entities_enriched_lite.jsonl"))
    parser.add_argument("--output-dir", type=Path, default=Path("obsidian_vault/entities"))
    parser.add_argument("--clean", action="store_true", help="Remove existing output directory before export.")
    args = parser.parse_args()

    normalized = args.normalized_dir
    out = args.output_dir
    if args.clean and out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    entities = read_csv(normalized / "entities.csv")
    edges = read_csv(normalized / "edges.csv")
    pathways = {row["pathway_id"]: row for row in read_csv(normalized / "pathways.csv")}
    enriched = read_jsonl_by_id(args.enriched_file)
    filename_map, filename_collisions = build_filename_map([row["entity_id"] for row in entities])

    outgoing: dict[str, list[dict[str, str]]] = defaultdict(list)
    incoming: dict[str, list[dict[str, str]]] = defaultdict(list)
    pathway_memberships: dict[str, list[str]] = defaultdict(list)
    entity_ids = {row["entity_id"] for row in entities}

    for row in edges:
        source = row.get("source_id", "")
        target = row.get("target_id", "")
        relation = row.get("relation_type", "")
        if relation == "participates_in" and target in pathways:
            pathway_memberships[source].append(target)
            continue
        if source in entity_ids:
            outgoing[source].append(row)
        if target in entity_ids:
            incoming[target].append(row)

    type_counts: dict[str, int] = defaultdict(int)
    for entity in entities:
        type_counts[entity.get("entity_type", "")] += 1
        path = out / f"{filename_map[entity['entity_id']]}.md"
        path.write_text(
            render_entity_note(
                entity,
                outgoing[entity["entity_id"]],
                incoming[entity["entity_id"]],
                pathway_memberships[entity["entity_id"]],
                pathways,
                filename_map,
                enriched.get(entity["entity_id"], {}),
            ),
            encoding="utf-8",
        )

    index = out.parent / "E.coil Entity Index.md"
    index.write_text(render_index(entities, type_counts, out.name, filename_map), encoding="utf-8")

    map_path = out.parent / "entity_filename_map.csv"
    with map_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["entity_id", "note_filename"])
        writer.writeheader()
        for entity in entities:
            writer.writerow({"entity_id": entity["entity_id"], "note_filename": f"{filename_map[entity['entity_id']]}.md"})

    actual_note_count = len(list(out.glob("*.md")))
    report = {
        "entity_count": len(entities),
        "note_count": actual_note_count,
        "filename_collision_groups": filename_collisions,
        "filename_collision_group_count": len(filename_collisions),
        "missing_note_count": len([entity for entity in entities if not (out / f"{filename_map[entity['entity_id']]}.md").is_file()]),
    }
    report_path = out.parent / "obsidian_export_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote entity notes: {len(entities)}")
    print(f"actual markdown files: {actual_note_count}")
    print(f"filename collision groups: {len(filename_collisions)}")
    print(f"output_dir={out.resolve()}")
    print(f"index={index.resolve()}")
    print(f"filename_map={map_path.resolve()}")
    print(f"report={report_path.resolve()}")
    return 0


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_jsonl_by_id(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    records = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            entity_id = data.get("entity_id")
            if entity_id:
                records[entity_id] = data
    return records


def render_entity_note(
    entity: dict[str, str],
    outgoing: list[dict[str, str]],
    incoming: list[dict[str, str]],
    pathway_ids: list[str],
    pathways: dict[str, dict[str, str]],
    filename_map: dict[str, str],
    enriched: dict,
) -> str:
    entity_id = entity["entity_id"]
    aliases = split_aliases(entity.get("aliases", ""))
    tags = [f"entity/{entity.get('entity_type', 'unknown')}", f"source/{slug(entity.get('source_database', 'unknown'))}"]
    lines = [
        "---",
        f"entity_id: {yaml_quote(entity_id)}",
        f"entity_type: {yaml_quote(entity.get('entity_type', ''))}",
        f"name: {yaml_quote(entity.get('name', ''))}",
        f"source_database: {yaml_quote(entity.get('source_database', ''))}",
        f"source_id: {yaml_quote(entity.get('source_id', ''))}",
        f"default_state: {yaml_quote(entity.get('default_state', ''))}",
        f"allowed_states: {yaml_quote(entity.get('allowed_states', ''))}",
        f"subcellular_location: {yaml_quote(entity.get('subcellular_location', ''))}",
        f"enriched_summary_quality: {yaml_quote(enriched.get('quality', {}).get('enriched_summary_quality', ''))}",
        "tags:",
        *[f"  - {tag}" for tag in tags],
        "aliases:",
        *[f"  - {yaml_quote(alias)}" for alias in aliases[:30]],
        "---",
        "",
        f"# {entity.get('name') or entity_id}",
        "",
        f"`{entity_id}`",
        "",
        "## Static",
        "",
        f"- Type: `{entity.get('entity_type', '')}`",
        f"- Source: `{entity.get('source_database', '')}:{entity.get('source_id', '')}`",
        f"- Default state: `{entity.get('default_state', '')}`",
        f"- Allowed states: `{entity.get('allowed_states', '')}`",
    ]
    if entity.get("subcellular_location"):
        lines.append(f"- Location: {entity['subcellular_location']}")
    if entity.get("complex_type"):
        lines.append(f"- Complex type: `{entity['complex_type']}`")
    if entity.get("components"):
        component_links = [obsidian_link(item, filename_map) for item in split_pipe(entity["components"])]
        lines.append(f"- Components: {', '.join(component_links)}")
    if entity.get("critical_components"):
        component_links = [obsidian_link(item, filename_map) for item in split_pipe(entity["critical_components"])]
        lines.append(f"- Critical components: {', '.join(component_links)}")

    if enriched:
        lines.extend(["", "## Enriched Summary", "", clean_text(enriched.get("summary", "")) or "_No enriched summary._"])
        if enriched.get("biological_role"):
            lines.extend(["", "## Biological Role", "", clean_text(enriched["biological_role"])])
        if enriched.get("pathways"):
            lines.extend(["", "## Enriched Pathways", ""])
            for pathway in enriched["pathways"][:30]:
                lines.append(f"- `{pathway.get('pathway_id', '')}` {pathway.get('pathway_name', '')} ({pathway.get('source', '')})")

    lines.extend(["", "## Annotation", "", clean_text(entity.get("annotation", "")) or "_No annotation._"])

    if pathway_ids:
        lines.extend(["", "## Pathways", ""])
        for pathway_id in sorted(set(pathway_ids)):
            pathway = pathways.get(pathway_id, {})
            name = pathway.get("pathway_name", pathway_id)
            source = pathway.get("source", "")
            lines.append(f"- `{pathway_id}` {name} ({source})")

    lines.extend(["", f"## Outgoing Edges ({len(outgoing)})", ""])
    if outgoing:
        for edge in sort_edges(outgoing):
            target = edge["target_id"]
            lines.append(edge_line(edge["relation_type"], target, edge, outgoing=True, filename_map=filename_map))
    else:
        lines.append("_None._")

    lines.extend(["", f"## Incoming Edges ({len(incoming)})", ""])
    if incoming:
        for edge in sort_edges(incoming):
            source = edge["source_id"]
            lines.append(edge_line(edge["relation_type"], source, edge, outgoing=False, filename_map=filename_map))
    else:
        lines.append("_None._")

    if entity.get("external_ids"):
        lines.extend(["", "## External IDs", ""])
        for item in split_pipe(entity["external_ids"]):
            lines.append(f"- `{item}`")

    if entity.get("notes"):
        lines.extend(["", "## Notes", "", clean_text(entity["notes"])])
    lines.append("")
    return "\n".join(lines)


def render_index(
    entities: list[dict[str, str]],
    type_counts: dict[str, int],
    entity_dir_name: str,
    filename_map: dict[str, str],
) -> str:
    lines = [
        "# E.coil Entity Index",
        "",
        f"Entity directory: `{entity_dir_name}/`",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted(type_counts.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Entry Points", ""])
    entry_ids = [
        "protein.P03023",
        "gene.b0344",
        "protein.P00722",
        "gene.b0343",
        "protein.P02920",
        "molecule.C00243",
        "molecule.C00031",
        "complex.ecocyc.BETAGALACTOSID-CPLX",
    ]
    existing = {row["entity_id"] for row in entities}
    for entity_id in entry_ids:
        if entity_id in existing:
            lines.append(f"- {obsidian_link(entity_id, filename_map)}")
    lines.append("")
    return "\n".join(lines)


def edge_line(relation: str, other_id: str, edge: dict[str, str], outgoing: bool, filename_map: dict[str, str]) -> str:
    arrow = "-->" if outgoing else "<--"
    source = edge.get("source_database", "")
    evidence = edge.get("evidence", "")
    note = clean_text(edge.get("notes", ""))
    suffix = f" `{source}`"
    if evidence:
        suffix += f" `{evidence}`"
    if note:
        suffix += f" - {note[:240]}"
    return f"- `{relation}` {arrow} {obsidian_link(other_id, filename_map)}{suffix}"


def sort_edges(edges: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(edges, key=lambda row: (row.get("relation_type", ""), row.get("target_id", ""), row.get("source_id", "")))


def obsidian_link(entity_id: str, filename_map: dict[str, str]) -> str:
    target = filename_map.get(entity_id, safe_filename(entity_id))
    return f"[[{target}|{entity_id}]]"


def safe_filename(entity_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", entity_id or "entity").strip("._")
    return safe or "entity"


def build_filename_map(entity_ids: list[str]) -> tuple[dict[str, str], list[dict[str, object]]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for entity_id in entity_ids:
        groups[safe_filename(entity_id).casefold()].append(entity_id)

    filename_map: dict[str, str] = {}
    collisions: list[dict[str, object]] = []
    for folded_name, ids in sorted(groups.items()):
        if len(ids) == 1:
            filename_map[ids[0]] = safe_filename(ids[0])
            continue

        collisions.append({"casefolded_filename": folded_name, "entity_ids": sorted(ids)})
        for entity_id in sorted(ids):
            digest = hashlib.sha1(entity_id.encode("utf-8")).hexdigest()[:8]
            filename_map[entity_id] = f"{safe_filename(entity_id)}__{digest}"

    return filename_map, collisions


def split_pipe(text: str) -> list[str]:
    return [item.strip() for item in (text or "").split("|") if item.strip()]


def split_aliases(text: str) -> list[str]:
    aliases = []
    seen = set()
    for item in re.split(r"[|;]", text or ""):
        item = item.strip()
        if not item or item.casefold() in seen:
            continue
        seen.add(item.casefold())
        aliases.append(item)
    return aliases


def slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", text or "unknown").strip("_")
    return text or "unknown"


def yaml_quote(text: str) -> str:
    text = (text or "").replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def clean_text(text: str) -> str:
    text = text or ""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


if __name__ == "__main__":
    raise SystemExit(main())
