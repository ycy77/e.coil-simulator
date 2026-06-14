"""Structured and narrative reporting for an E.coil simulation run.

The reporter returns a structured dict (for storage, JSON outputs, and
downstream tooling) plus a natural-language narrative that can be
consumed by humans and (later) by an LLM-powered follow-up agent.

The narrative is intentionally descriptive, not explanatory: it
summarises what changed and which agent, and it points at the
candidate rules and graph edges that drove the change. It does not
invent biological mechanisms the registry did not provide.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional

from ecoil_sim.config import load_yaml_like
from ecoil_sim.graph import StaticGraph
from ecoil_sim.models import Entity
from ecoil_sim.state import TemporalState


class Reporter:
    def __init__(
        self,
        graph: StaticGraph | None = None,
        phenotype_db: Path | None = None,
        name_resolver=None,
    ) -> None:
        self.graph = graph
        self.phenotype_db = load_yaml_like(phenotype_db) if phenotype_db and phenotype_db.exists() else {}
        self.name_resolver = name_resolver

    def _public(self, entity_id: str) -> str:
        if self.name_resolver is not None:
            try:
                return self.name_resolver.to_public(entity_id)
            except Exception:
                pass
        if self.graph is not None:
            entity = self.graph.entities.get(entity_id)
            if entity is not None:
                return entity.name or entity_id
        return entity_id

    def _labeled(self, entity_id: str, seen: set) -> str:
        """First-mention bracketed display name.

        Within a single ``render_narrative`` call the helper
        remembers which entity_ids it has already produced a label
        for. The first mention includes the canonical id in square
        brackets (``"LacI repressor [protein.P03023]"``); later
        mentions are just the display name.

        This convention preserves traceability (a reviewer can
        always click through the bracketed id) without repeating
        the ugly id in every line of a long report.
        """
        if not entity_id:
            return "?"
        if entity_id in seen:
            return self._public(entity_id)
        seen.add(entity_id)
        return f"{self._public(entity_id)} [{entity_id}]"

    def summarize_changes(self, state: TemporalState, limit: int = 50) -> Dict:
        events: List[Dict] = []
        for entity_id, history in state.history.items():
            for item in history:
                if item.get("changed"):
                    events.append({"entity_id": entity_id, **item})
        events.sort(key=lambda item: (item.get("round", 0), item["entity_id"]))
        final_changed = {}
        for entity_id, history in state.history.items():
            changed_items = [item for item in history if item.get("changed")]
            if changed_items:
                final_changed[entity_id] = changed_items[-1]
        by_round = Counter(item.get("round", 0) for item in events)
        propagation_edges = []
        for item in events:
            for neighbor_id in item.get("changed_neighbors", []) or []:
                propagation_edges.append(
                    {
                        "round": item.get("round"),
                        "source": neighbor_id,
                        "target": item["entity_id"],
                    }
                )
        perturbation_sources = [item["entity_id"] for item in events if item.get("round") == 0]
        response_pattern_match = self._response_pattern_match(state)
        inflection_points = self._inflection_points(events, propagation_edges)
        feedback = self._feedback_events(events, perturbation_sources)
        return {
            "rounds": state.current_round,
            "changed_events": len(events),
            "perturbation_sources": perturbation_sources,
            "feedback_loops": feedback,
            "events_by_round": dict(sorted(by_round.items())),
            "propagation_edges": propagation_edges[:limit],
            "causal_chains": self._causal_chains(perturbation_sources, propagation_edges, limit=limit),
            "final_changed_states": {
                entity_id: {
                    "state": item.get("state"),
                    "abundance_label": item.get("abundance_label"),
                    "round": item.get("round"),
                }
                for entity_id, item in sorted(final_changed.items())
            },
            "unexpected_response_candidates": self._unexpected_candidates(events, perturbation_sources),
            "response_pattern_match": response_pattern_match,
            "phenotype_match": response_pattern_match,
            "inflection_points": inflection_points,
            "events": events[:limit],
        }

    @staticmethod
    def _feedback_events(events: List[Dict], perturbation_sources: List[str]) -> Dict:
        """Detect cascades that loop back — the reason a run counts by rounds, not convergence.

        In a regulatory network with feedback (a gene product that re-regulates an
        upstream TF), propagation can return to a node that already changed,
        including the originally perturbed one. We surface two signals:
          * ``closed_on_source`` — a perturbation source re-changed in a later round
            (the loop closed back on the origin).
          * ``reactivations`` — any entity that changed in more than one round
            (oscillation / sustained feedback).
        These never stop the run; the human-set round budget does.
        """
        source_set = set(perturbation_sources)
        rounds_by_entity: Dict[str, set] = {}
        for item in events:
            rounds_by_entity.setdefault(item["entity_id"], set()).add(item.get("round", 0))
        closed_on_source = [
            {"entity_id": eid, "rounds": sorted(rs)}
            for eid, rs in rounds_by_entity.items()
            if eid in source_set and any(r > 0 for r in rs)
        ]
        reactivations = [
            {"entity_id": eid, "rounds": sorted(rs)}
            for eid, rs in rounds_by_entity.items()
            if len(rs) > 1
        ]
        return {
            "closed_on_source": sorted(closed_on_source, key=lambda x: x["entity_id"]),
            "reactivations": sorted(reactivations, key=lambda x: x["entity_id"]),
            "has_feedback": bool(closed_on_source or reactivations),
        }

    def per_round_summaries(self, summary: Dict) -> List[Dict]:
        """Slice a run summary into per-round views for round-by-round reporting.

        Each entry is the changes that landed in that propagation round plus the
        edges that carried them and whether the round re-touched a perturbation
        source (a feedback closure). Feeds the report agent's per-round mode.
        """
        sources = set(summary.get("perturbation_sources", []))
        edges_by_round: Dict[int, List[Dict]] = {}
        for edge in summary.get("propagation_edges", []):
            edges_by_round.setdefault(edge.get("round", 0), []).append(edge)
        changes_by_round: Dict[int, List[Dict]] = {}
        for ev in summary.get("events", []):
            changes_by_round.setdefault(ev.get("round", 0), []).append(
                {"entity_id": ev["entity_id"], "state": ev.get("state"),
                 "abundance_label": ev.get("abundance_label"), "efficiency": ev.get("efficiency"),
                 "reason": ev.get("reason", "")}
            )
        rounds = sorted(set(changes_by_round) | set(edges_by_round))
        out = []
        for r in rounds:
            changed_ids = {c["entity_id"] for c in changes_by_round.get(r, [])}
            out.append({
                "round": r,
                "changes": changes_by_round.get(r, []),
                "propagation_edges": edges_by_round.get(r, []),
                "feedback_closure": sorted(changed_ids & sources) if r > 0 else [],
            })
        return out

    def render_narrative(self, summary: Dict) -> str:
        rounds = summary.get("rounds", 0)
        sources = summary.get("perturbation_sources", []) or []
        events_by_round = summary.get("events_by_round", {}) or {}
        chains = summary.get("causal_chains", []) or []
        final_states = summary.get("final_changed_states", {}) or {}
        inflections = summary.get("inflection_points", []) or []
        pattern_match = summary.get("response_pattern_match", {}) or {}

        # Track which entity_ids have been mentioned in this report
        # so the first reference shows the bracketed id and later
        # references stay clean.
        seen: set = set()
        lines: List[str] = []
        lines.append("=" * 72)
        lines.append("E.coil simulation report")
        lines.append("=" * 72)
        lines.append(f"Rounds simulated: {rounds}")
        if sources:
            lines.append(
                "Perturbation sources: "
                + ", ".join(self._labeled(src, seen) for src in sources)
            )
        else:
            lines.append("No perturbations were applied; the run started from the initial profile.")
        lines.append("")

        lines.append("Per-round change counts")
        for round_number in sorted(events_by_round.keys()):
            count = events_by_round[round_number]
            lines.append(f"  round {round_number}: {count} agent change(s)")

        if inflections:
            lines.append("")
            lines.append("Key inflection points")
            for point in inflections:
                lines.append(self._format_inflection(point, seen))

        if chains:
            lines.append("")
            lines.append("Causal chains (sampled)")
            for chain in chains[:10]:
                lines.append(
                    "  "
                    + "  ->  ".join(self._labeled(node, seen) for node in chain)
                )

        if final_states:
            lines.append("")
            lines.append("Final changed states")
            for entity_id, info in final_states.items():
                state_part = info.get("state", "?")
                abundance_part = info.get("abundance_label", "")
                abundance = f" / abundance={abundance_part}" if abundance_part else ""
                lines.append(
                    f"  round {info.get('round')}  {self._labeled(entity_id, seen)}  state={state_part}{abundance}"
                )

        matches = pattern_match.get("matches", []) if isinstance(pattern_match, dict) else []
        if matches:
            lines.append("")
            lines.append("Phenotype / response-pattern matches")
            for match in matches[:5]:
                lines.append(
                    f"  - {match.get('pattern_id')}  similarity={match.get('similarity')}  "
                    f"{match.get('description', '')}"
                )
        lines.append("=" * 72)
        return "\n".join(lines)

    def _format_inflection(self, point: Dict, seen: set) -> str:
        round_number = point.get("round")
        target = self._labeled(point.get("target", ""), seen)
        state = point.get("state", "?")
        abundance = point.get("abundance_label", "")
        abundance_part = f" (abundance={abundance})" if abundance else ""
        reasons = point.get("reasons", []) or []
        reason_text = ""
        if reasons:
            top = reasons[0]
            reason_text = f" — {self._labeled(top.get('source', '?'), seen)} -> {self._labeled(top.get('target', '?'), seen)} via {top.get('relation', '?')}"
        return f"  round {round_number}  {target}  ->  state={state}{abundance_part}{reason_text}"

    def _inflection_points(self, events: List[Dict], propagation_edges: List[Dict]) -> List[Dict]:
        if not events:
            return []
        per_round = defaultdict(int)
        for event in events:
            per_round[event.get("round", 0)] += 1
        ranked_rounds = sorted(per_round.items(), key=lambda item: (-item[1], item[0]))
        top = []
        for round_number, count in ranked_rounds[:3]:
            if count == 0:
                continue
            round_events = [event for event in events if event.get("round") == round_number]
            representative = sorted(round_events, key=lambda item: item.get("entity_id", ""))[:5]
            top.append(
                {
                    "round": round_number,
                    "change_count": count,
                    "targets": [event.get("entity_id", "") for event in representative],
                }
            )
        enriched: List[Dict] = []
        for point in top:
            round_number = point["round"]
            target = point["targets"][0] if point["targets"] else ""
            sample = next((event for event in events if event.get("round") == round_number), {})
            reasons = []
            for edge in propagation_edges:
                if edge.get("round") != round_number:
                    continue
                if edge.get("target") == target:
                    reasons.append(
                        {
                            "source": edge.get("source"),
                            "target": edge.get("target"),
                            "relation": "graph_propagation",
                        }
                    )
                if len(reasons) >= 3:
                    break
            enriched.append(
                {
                    "round": round_number,
                    "change_count": point["change_count"],
                    "target": target,
                    "state": sample.get("state", ""),
                    "abundance_label": sample.get("abundance_label", ""),
                    "reasons": reasons,
                }
            )
        return enriched

    def _unexpected_candidates(self, events: List[Dict], perturbation_sources: List[str]) -> List[Dict]:
        candidates = []
        for item in events:
            if item.get("round", 0) <= 1:
                continue
            distance = None
            if self.graph:
                distance = self.graph.shortest_distance(perturbation_sources, item["entity_id"], max_depth=6)
                if distance is not None and distance <= 3:
                    continue
            candidates.append(
                {
                    "entity_id": item["entity_id"],
                    "round": item.get("round"),
                    "state": item.get("state"),
                    "distance_from_perturbation": distance,
                    "reason": item.get("reason", ""),
                }
            )
        return candidates[:20]

    @staticmethod
    def _causal_chains(sources: List[str], propagation_edges: List[Dict], limit: int = 20) -> List[List[str]]:
        children: Dict[str, List[str]] = defaultdict(list)
        for edge in sorted(propagation_edges, key=lambda item: item.get("round", 0)):
            children[edge["source"]].append(edge["target"])
        chains: List[List[str]] = []
        stack = [[source] for source in sources]
        while stack and len(chains) < limit:
            chain = stack.pop(0)
            tail = chain[-1]
            next_nodes = [node for node in children.get(tail, []) if node not in chain]
            if not next_nodes:
                if len(chain) > 1:
                    chains.append(chain)
                continue
            for node in next_nodes:
                stack.append(chain + [node])
        return chains

    def _response_pattern_match(self, state: TemporalState) -> Dict:
        if not self.phenotype_db:
            return {
                "status": "not_configured",
                "note": "Response-pattern DB not loaded.",
            }
        changed_entities = {
            entity_id
            for entity_id, history in state.history.items()
            if any(item.get("changed") for item in history)
        }
        results = []
        for pattern_id, spec in self.phenotype_db.items():
            if not isinstance(spec, dict):
                continue
            expected_states = spec.get("expected_states", {})
            expected_abundance = spec.get("expected_abundance", {})
            expected_states = expected_states if isinstance(expected_states, dict) else {}
            expected_abundance = expected_abundance if isinstance(expected_abundance, dict) else {}
            if not expected_states and not expected_abundance:
                continue

            # Gate on the scenario's driving signals: a pattern only matches if
            # the upstream sources it requires actually changed in this run.
            # Without this, a LacI-only run spuriously matched the L2
            # lac_dual_signal pattern (which also requires CRP-cAMP to be low).
            required_sources = self._pattern_signal_sources(spec)
            if required_sources and not required_sources.issubset(changed_entities):
                continue

            matched = 0
            checked = 0
            touched = 0
            details = {}
            # Compare states against expected_states and abundance against
            # expected_abundance -- on their own axes, no cross-matching.
            for entity_id, wanted in expected_states.items():
                observed = state.states.get(entity_id)
                if not observed:
                    continue
                checked += 1
                touched += 1 if entity_id in changed_entities else 0
                ok = observed.state == wanted
                matched += 1 if ok else 0
                details[entity_id] = {"axis": "state", "expected": wanted, "observed": observed.state, "match": ok}
            for entity_id, wanted in expected_abundance.items():
                observed = state.states.get(entity_id)
                if not observed:
                    continue
                checked += 1
                touched += 1 if entity_id in changed_entities else 0
                ok = observed.abundance_label == wanted
                matched += 1 if ok else 0
                details[entity_id] = {"axis": "abundance", "expected": wanted, "observed": observed.abundance_label, "match": ok}

            if checked and touched and matched:
                results.append(
                    {
                        "pattern_id": pattern_id,
                        "description": spec.get("description", ""),
                        "matched": matched,
                        "total": checked,
                        "touched": touched,
                        "required_signals_present": bool(required_sources),
                        "similarity": round(matched / checked, 3),
                        "details": details,
                    }
                )
        results.sort(key=lambda item: (-item["similarity"], item["pattern_id"]))
        return {"status": "ok", "matches": results[:10]}

    @staticmethod
    def _pattern_signal_sources(spec: Dict) -> set:
        """Upstream source entities a pattern's ``signals`` block requires.

        These are the perturbation that *defines* the scenario; if they did not
        change in the run, the run is not an instance of this phenotype.
        """
        sources: set = set()
        signals = spec.get("signals", {})
        if not isinstance(signals, dict):
            return sources
        for sigs in signals.values():
            if not isinstance(sigs, list):
                continue
            for sig in sigs:
                if isinstance(sig, dict) and sig.get("from"):
                    sources.add(sig["from"])
        return sources

    def agent_replay_prompt(self, state: TemporalState, entity_id: str, question: str) -> str:
        entity = self.graph.entities.get(entity_id) if self.graph else None
        history = state.history.get(entity_id, [])
        lines = [
            f"You are {self._public(entity_id)}.",
            f"Entity ID: {entity_id}",
        ]
        if entity:
            lines.extend(
                [
                    f"Entity type: {entity.entity_type}",
                    f"Function: {entity.annotation[:1200]}",
                    f"Pathways: {entity.pathways}",
                ]
            )
        lines.append("Full simulation history:")
        for item in history:
            lines.append(
                f"Round {item.get('round')}: state={item.get('state')} "
                f"abundance={item.get('abundance_label')} changed={item.get('changed')} "
                f"neighbors={item.get('changed_neighbors')} reason={item.get('reason')}"
            )
        lines.append(f"User question: {question}")
        lines.append("Answer only from this entity history and the known annotation.")
        return "\n".join(lines)
