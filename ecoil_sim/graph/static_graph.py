from __future__ import annotations

import csv
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

from ecoil_sim.models import Edge, Entity, Pathway
from ecoil_sim.paths import NORMALIZED_DIR


class StaticGraph:
    """Read-only biological graph built from normalized CSV files."""

    def __init__(
        self,
        entities: Dict[str, Entity],
        edges: List[Edge],
        pathways: Dict[str, Pathway],
    ) -> None:
        self.entities = entities
        self.edges = edges
        self.pathways = pathways
        self.out_edges: Dict[str, List[Edge]] = defaultdict(list)
        self.in_edges: Dict[str, List[Edge]] = defaultdict(list)
        self.undirected_edges: Dict[str, List[Edge]] = defaultdict(list)
        for edge in edges:
            self.out_edges[edge.source_id].append(edge)
            self.in_edges[edge.target_id].append(edge)
            self.undirected_edges[edge.source_id].append(edge)
            self.undirected_edges[edge.target_id].append(edge)

    @classmethod
    def from_normalized_dir(cls, path: Path = NORMALIZED_DIR) -> "StaticGraph":
        entities = cls._read_entities(path / "entities.csv")
        edges = cls._read_edges(path / "edges.csv")
        pathways = cls._read_pathways(path / "pathways.csv")
        return cls(entities=entities, edges=edges, pathways=pathways)

    @staticmethod
    def _read_entities(path: Path) -> Dict[str, Entity]:
        with path.open(newline="", encoding="utf-8") as handle:
            return {row["entity_id"]: Entity.from_row(row) for row in csv.DictReader(handle)}

    @staticmethod
    def _read_edges(path: Path) -> List[Edge]:
        with path.open(newline="", encoding="utf-8") as handle:
            return [Edge.from_row(row) for row in csv.DictReader(handle)]

    @staticmethod
    def _read_pathways(path: Path) -> Dict[str, Pathway]:
        with path.open(newline="", encoding="utf-8") as handle:
            return {row["pathway_id"]: Pathway.from_row(row) for row in csv.DictReader(handle)}

    def get_entity(self, entity_id: str) -> Optional[Entity]:
        return self.entities.get(entity_id)

    def neighbors(
        self,
        entity_id: str,
        relation_types: Optional[Set[str]] = None,
        directed: bool = False,
    ) -> List[str]:
        edges = self.out_edges.get(entity_id, []) if directed else self.undirected_edges.get(entity_id, [])
        found: List[str] = []
        for edge in edges:
            if relation_types and edge.relation_type not in relation_types:
                continue
            other = edge.target_id if edge.source_id == entity_id else edge.source_id
            found.append(other)
        return found

    def incident_edges(
        self,
        entity_id: str,
        relation_types: Optional[Set[str]] = None,
        directed: bool = False,
    ) -> List[Edge]:
        edges = self.out_edges.get(entity_id, []) if directed else self.undirected_edges.get(entity_id, [])
        if not relation_types:
            return list(edges)
        return [edge for edge in edges if edge.relation_type in relation_types]

    def search_entities(self, query: str, limit: int = 50) -> List[Entity]:
        needle = query.lower().strip()
        if not needle:
            return []
        scored = []
        for entity in self.entities.values():
            haystack = " ".join([
                entity.entity_id,
                entity.name,
                " ".join(entity.aliases),
                entity.annotation,
                entity.pathways,
                entity.external_ids,
            ]).lower()
            if needle in haystack:
                score = 5 if needle in entity.name.lower() else 1
                score += 2 if needle in entity.entity_id.lower() else 0
                scored.append((score, entity.entity_id, entity))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return [entity for _, _, entity in scored[:limit]]

    def extract_subgraph(
        self,
        seeds: Iterable[str],
        radius: int = 1,
        relation_types: Optional[Set[str]] = None,
        max_nodes: int = 200,
    ) -> "StaticGraph":
        visited: Set[str] = set()
        queue = deque((seed, 0) for seed in seeds if seed in self.entities)
        while queue and len(visited) < max_nodes:
            entity_id, depth = queue.popleft()
            if entity_id in visited or depth > radius:
                continue
            visited.add(entity_id)
            if depth == radius:
                continue
            for neighbor in self.neighbors(entity_id, relation_types=relation_types):
                if neighbor not in visited and neighbor in self.entities:
                    queue.append((neighbor, depth + 1))

        sub_edges = [
            edge for edge in self.edges
            if edge.source_id in visited and edge.target_id in visited
            and (not relation_types or edge.relation_type in relation_types)
        ]
        return StaticGraph(
            entities={entity_id: self.entities[entity_id] for entity_id in visited},
            edges=sub_edges,
            pathways=self.pathways,
        )

    def shortest_distance(self, sources: Iterable[str], target: str, max_depth: int = 6) -> Optional[int]:
        source_set = {source for source in sources if source in self.entities}
        if target in source_set:
            return 0
        queue = deque((source, 0) for source in source_set)
        visited: Set[str] = set(source_set)
        while queue:
            entity_id, depth = queue.popleft()
            if depth >= max_depth:
                continue
            for neighbor in self.neighbors(entity_id):
                if neighbor == target:
                    return depth + 1
                if neighbor not in visited and neighbor in self.entities:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        return None

    def summary(self) -> Dict[str, int]:
        return {
            "entities": len(self.entities),
            "edges": len(self.edges),
            "pathways": len(self.pathways),
        }
