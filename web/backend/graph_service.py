"""Subgraph extraction for the diagnostic UI.

Pulls a node-and-edge payload suitable for vis-network from the
:class:`DataLoader` and tints nodes by entity type and edges by
relation type so the reviewer can see data quality at a glance.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Set

from web.backend.data_loader import DataLoader, EdgeRecord, EntityRecord


# Reactions are no longer nodes (they were flattened into
# ``produces`` / ``consumes`` edge payloads by
# scripts/flatten_reactions.py), so there is no "reaction"
# entity_type to color any more.
_ENTITY_TYPE_COLORS = {
    "gene": "#7c9eff",
    "protein": "#f0a36b",
    "small_molecule": "#7ad7a3",
    "rna": "#d59af1",
    "complex": "#e8d36b",
    "regulatory_region": "#8fe0d0",
}

# New relation vocabulary after flatten_reactions.py.
#   * ``produces``  : catalyst -> product (was catalyzes + is_product_of)
#   * ``consumes``  : catalyst -> substrate (was catalyzes + is_substrate_of)
#   * ``spontaneous_produces`` / ``spontaneous_consumes``: same, no catalyst
# ``is_substrate_of`` / ``is_product_of`` / ``catalyzes`` are
# gone with the reaction nodes.
_RELATION_DASHES = {
    "represses": [6, 4],
    "activates": [],
    "inhibits": [2, 2],
    "encodes": [4, 2, 1, 2],
    "produces": [4, 4],
    "consumes": [4, 4],
    "spontaneous_produces": [1, 3],
    "spontaneous_consumes": [1, 3],
    "participates_in": [3, 3, 1, 3],
    "is_component_of": [],
}


class GraphService:
    def __init__(self, loader: DataLoader) -> None:
        self.loader = loader

    def subgraph(self, center: str, hops: int = 1, max_nodes: int = 200) -> Dict:
        if center not in self.loader._entities:  # type: ignore[attr-defined]
            return {"center": center, "nodes": [], "edges": [], "truncated": False}
        nodes, distances, truncated = self._bounded_neighborhood(
            center=center,
            hops=hops,
            max_nodes=max_nodes,
        )
        edges: List[Dict] = []
        seen_edges: Set[tuple[str, str, str, str, str]] = set()
        for node in nodes:
            for edge in self.loader.edges_of(node):  # type: ignore[attr-defined]
                if edge.source_id in nodes and edge.target_id in nodes:
                    edge_key = (
                        edge.source_id,
                        edge.relation_type,
                        edge.target_id,
                        edge.source_database,
                        edge.source_record_id,
                    )
                    if edge_key in seen_edges:
                        continue
                    seen_edges.add(edge_key)
                    edges.append(edge.to_dict())
        node_payload: List[Dict] = []
        for node_id in sorted(nodes, key=lambda nid: (distances.get(nid, 999), nid != center, nid)):
            entity = self.loader.get_entity(node_id)  # type: ignore[attr-defined]
            if entity is None:
                continue
            node_payload.append(self._entity_to_node(entity, distance=distances.get(node_id, 0)))
        return {
            "center": center,
            "hops": hops,
            "nodes": node_payload,
            "edges": edges,
            "truncated": truncated,
        }

    def full_overview(self, center: str) -> Dict:
        if center not in self.loader._entities:  # type: ignore[attr-defined]
            return {"center": center, "error": "not found"}
        entity = self.loader.get_entity(center)  # type: ignore[attr-defined]
        in_edges: List[Dict] = []
        out_edges: List[Dict] = []
        for edge in self.loader.edges_of(center):  # type: ignore[attr-defined]
            data = edge.to_dict()
            if edge.target_id == center:
                in_edges.append(data)
            else:
                out_edges.append(data)
        return {
            "entity": entity.to_dict() if entity else None,
            "in_edges": in_edges,
            "out_edges": out_edges,
            "reconciliation": self.loader.reconciliation_for_entity(center),  # type: ignore[attr-defined]
            "same_name_siblings": self.loader.same_name_siblings(center),  # type: ignore[attr-defined]
        }

    def _entity_to_node(self, entity: EntityRecord, distance: int = 0) -> Dict:
        return {
            "id": entity.entity_id,
            "label": entity.display_name,
            # Short name without the "(UniProt #N)" suffix. The graph
            # canvas is too dense to fit the full display_name; the
            # parenthetical stays available via the detail panel and
            # the node tooltip.
            "name": entity.name,
            "entity_type": entity.entity_type,
            "color": _ENTITY_TYPE_COLORS.get(entity.entity_type, "#999999"),
            "shape": _shape_for(entity.entity_type),
            "distance": distance,
            "annotation_length": entity.annotation_length,
            "annotation_empty": entity.annotation_length == 0,
            "quality_label": entity.quality_label,
            "summary_excerpt": (entity.display_summary[:200] + "…") if len(entity.display_summary) > 200 else entity.display_summary,
        }

    def _bounded_neighborhood(self, center: str, hops: int, max_nodes: int) -> tuple[Set[str], Dict[str, int], bool]:
        """Collect a local neighborhood without losing the connected core.

        The old implementation gathered the entire hop-limited neighborhood
        and then kept the lexicographically first ``max_nodes`` ids. Around
        global regulators this often discarded the very protein / complex /
        reaction nodes that made the subgraph interpretable, leaving dozens
        of disconnected genes on screen. Here we retain the BFS frontier
        order so lower-hop nodes are always preserved first.
        """
        valid_max_nodes = max(1, max_nodes)
        visited: Set[str] = {center}
        distances: Dict[str, int] = {center: 0}
        frontier: List[str] = [center]
        truncated = False
        for depth in range(1, max(hops, 0) + 1):
            candidates: Set[str] = set()
            for node_id in frontier:
                for edge in self.loader.edges_of(node_id):  # type: ignore[attr-defined]
                    if edge.source_id not in visited and self.loader.get_entity(edge.source_id) is not None:  # type: ignore[attr-defined]
                        candidates.add(edge.source_id)
                    if edge.target_id not in visited and self.loader.get_entity(edge.target_id) is not None:  # type: ignore[attr-defined]
                        candidates.add(edge.target_id)
            if not candidates:
                break
            ordered_candidates = sorted(
                candidates,
                key=lambda node_id: (
                    _type_priority(self.loader.get_entity(node_id)),  # type: ignore[attr-defined]
                    -self._node_degree(node_id),
                    node_id,
                ),
            )
            remaining = valid_max_nodes - len(visited)
            if remaining <= 0:
                truncated = True
                break
            if len(ordered_candidates) > remaining:
                ordered_candidates = ordered_candidates[:remaining]
                truncated = True
            frontier = ordered_candidates
            for node_id in ordered_candidates:
                visited.add(node_id)
                distances[node_id] = depth
            if truncated:
                break
        return visited, distances, truncated

    def _node_degree(self, entity_id: str) -> int:
        return len(self.loader._edges_by_source.get(entity_id, [])) + len(self.loader._edges_by_target.get(entity_id, []))  # type: ignore[attr-defined]


def _shape_for(entity_type: str) -> str:
    if entity_type == "gene":
        return "triangle"
    if entity_type == "protein":
        return "box"
    if entity_type == "small_molecule":
        return "dot"
    if entity_type == "rna":
        return "diamond"
    if entity_type == "complex":
        return "square"
    if entity_type == "regulatory_region":
        return "hexagon"
    return "ellipse"


def _type_priority(entity: Optional[EntityRecord]) -> int:
    # After the flatten step there is no "reaction" entity type.
    # Place the surviving types in the same priority order the
    # reviewer is used to (proteins first, genes last).
    if entity is None:
        return 99
    order = {
        "protein": 0,
        "complex": 1,
        "small_molecule": 2,
        "rna": 3,
        "gene": 4,
        "regulatory_region": 5,
    }
    return order.get(entity.entity_type, 50)
