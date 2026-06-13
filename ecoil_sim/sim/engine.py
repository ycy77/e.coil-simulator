"""Main simulation loop.

Per round:

1. ``TemporalGraphRAG`` selects candidate agents whose neighborhood
   changed in the previous round.
2. ``PromptBuilder`` converts each candidate into a public-name
   prompt and emits a ``PromptBuildResult`` with the rule hint map.
3. The LLM client emits action proposals.
4. The :class:`ActionInterpreter` translates the LLM output (or a
   configured fallback) into canonical state updates.
5. ``RuleEngine.apply_structural_complexes`` runs deterministic updates
   for complexes whose components are in degraded/inhibited/active states.
6. The updated state is persisted to the simulation store along with a
   per-round stage report.

The loop is fixed-rounds by design. Steady-state detection only annotates
reports; it never shortens a run.
"""

from __future__ import annotations

import asyncio
from collections import Counter
from typing import Dict, Iterable, List

from ecoil_sim.actions import ActionInterpreter
from ecoil_sim.agents import PromptBuilder
from ecoil_sim.graph import StaticGraph
from ecoil_sim.llm import NameResolver, NullLLMClient
from ecoil_sim.models import AgentState
from ecoil_sim.registry import RuleRegistry
from ecoil_sim.retrieval import TemporalGraphRAG
from ecoil_sim.rules import RuleEngine
from ecoil_sim.sim.enriched_service import EnrichedService
from ecoil_sim.state import TemporalState
from ecoil_sim.storage import SimulationStore
from ecoil_sim.validation import ActionValidator


class SimulationEngine:
    def __init__(
        self,
        graph: StaticGraph,
        registry: RuleRegistry,
        retriever: TemporalGraphRAG,
        prompt_builder: PromptBuilder,
        store: SimulationStore,
        llm_client=None,
        name_resolver: NameResolver | None = None,
        action_interpreter: ActionInterpreter | None = None,
        validator: ActionValidator | None = None,
        enriched_service: EnrichedService | None = None,
    ) -> None:
        self.graph = graph
        self.registry = registry
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.store = store
        self.llm_client = llm_client or NullLLMClient()
        self.name_resolver = name_resolver or NameResolver(graph.entities.values())
        self.prompt_builder.attach_resolver(self.name_resolver)
        if enriched_service is not None:
            self.prompt_builder.attach_enriched(enriched_service)
        self.rule_engine = RuleEngine(graph)
        self.validator = validator or ActionValidator(name_resolver=self.name_resolver)
        self.action_interpreter = action_interpreter or ActionInterpreter(graph)

    async def run(
        self,
        perturbations: Iterable[dict],
        max_rounds: int = 5,
        max_active_agents: int = 64,
        steady_state_patience: int = 2,
        initial_state: TemporalState | None = None,
        initial_profile: Dict | None = None,
        run_context: Dict | None = None,
    ) -> TemporalState:
        state = initial_state or TemporalState.initialize(self.graph.entities.values(), initial_profile=initial_profile)
        perturbation_list = list(perturbations)
        self.store.write_meta(
            {
                "max_rounds": max_rounds,
                "perturbations": perturbation_list,
                "run_context": run_context or {},
                "iteration_policy": "fixed_rounds",
                "steady_state_patience": steady_state_patience,
                "steady_state_behavior": "annotate_only_do_not_stop",
            }
        )
        self.store.write_graph_summary(self.graph.summary() | self.registry.summary())

        initial_updates = self.rule_engine.apply_perturbations(state, perturbation_list)
        state.apply_changes(initial_updates, reason_prefix="round_0")
        self.store.write_round(state)
        self.store.write_stage_report(
            state.current_round,
            self._stage_report(
                state=state,
                previous_changed=[],
                candidate_count=0,
                stable_rounds=0,
                steady_state_patience=steady_state_patience,
            ),
        )

        stable_rounds = 0
        for _ in range(max_rounds):
            previous_changed = state.changed_entities()
            state.begin_round()
            contexts: List = []
            changed_count = 0
            if previous_changed:
                contexts = self.retriever.retrieve(state, previous_changed, max_agents=max_active_agents)
                prompt_results = [self.prompt_builder.build(self.graph, state, context) for context in contexts]
                prompts = [result.messages for result in prompt_results]
                hint_maps = [result.rule_hint_map for result in prompt_results]
                llm_outputs = await self.llm_client.batch_chat(prompts)
                updates = self._outputs_to_states(state, contexts, llm_outputs, hint_maps)
                changed_count = state.apply_changes(updates, reason_prefix=f"round_{state.current_round}")
            else:
                updates = []

            complex_updates = self.rule_engine.apply_structural_complexes(state)
            changed_count += state.apply_changes(complex_updates, reason_prefix=f"round_{state.current_round}")

            state.end_round()
            if changed_count == 0:
                stable_rounds += 1
            else:
                stable_rounds = 0
            self.store.write_round(state)
            self.store.write_stage_report(
                state.current_round,
                self._stage_report(
                    state=state,
                    previous_changed=previous_changed,
                    candidate_count=len(contexts),
                    stable_rounds=stable_rounds,
                    steady_state_patience=steady_state_patience,
                ),
            )

        self.store.write_agent_histories(state)
        return state

    def _outputs_to_states(
        self,
        state: TemporalState,
        contexts,
        outputs: List[Dict],
        hint_maps: List[Dict[str, str]],
    ) -> List[AgentState]:
        results: List[AgentState] = []
        for context, output, hint_map in zip(contexts, outputs, hint_maps):
            if context.entity_id not in state.states:
                continue
            self._attach_hint_map(output, hint_map)
            candidate_rule_ids = {rule.rule_id for rule in context.rules}
            validated = self.validator.validate(
                output,
                candidate_rule_ids=candidate_rule_ids,
                rule_hint_map=hint_map or None,
            )
            merged_output = dict(output) if isinstance(output, dict) else {"actions": []}
            merged_output["actions"] = validated.get("actions", [])
            if validated.get("diagnostics") is not None and isinstance(merged_output, dict):
                merged_output.setdefault("_validation_diagnostics", validated["diagnostics"])
            results.append(self.action_interpreter.interpret(state, context, merged_output))
        return results

    @staticmethod
    def _attach_hint_map(output: Dict, hint_map: Dict[str, str]) -> None:
        if not isinstance(output, dict):
            return
        if hint_map and "_rule_hint_map" not in output:
            output["_rule_hint_map"] = dict(hint_map)

    def _stage_report(
        self,
        state: TemporalState,
        previous_changed: List[str],
        candidate_count: int,
        stable_rounds: int,
        steady_state_patience: int,
        event_limit: int = 100,
    ) -> Dict:
        round_number = state.current_round
        events = [
            {"entity_id": entity_id, **item}
            for entity_id, history in state.history.items()
            for item in history
            if item.get("round") == round_number and item.get("changed")
        ]
        events.sort(key=lambda item: item["entity_id"])
        propagation_edges = []
        for item in events:
            for neighbor_id in item.get("changed_neighbors", []) or []:
                propagation_edges.append(
                    {
                        "round": round_number,
                        "source": neighbor_id,
                        "target": item["entity_id"],
                    }
                )
        state_counts = Counter(agent_state.state for agent_state in state.states.values())
        abundance_counts = Counter(
            agent_state.abundance_label
            for agent_state in state.states.values()
            if agent_state.abundance_label
        )
        return {
            "round": round_number,
            "report_type": "stage_report",
            "iteration_policy": "fixed_rounds",
            "steady_state": {
                "detected": stable_rounds >= steady_state_patience,
                "stable_rounds": stable_rounds,
                "patience": steady_state_patience,
                "action": "annotated_only_simulation_continues_until_max_rounds",
            },
            "summary": {
                "previous_round_changed_agents": len(previous_changed),
                "candidate_agents": candidate_count,
                "new_changed_agents": len(events),
            },
            "new_changes": events[:event_limit],
            "propagation_edges": propagation_edges[:event_limit],
            "state_counts": dict(sorted(state_counts.items())),
            "abundance_counts": dict(sorted(abundance_counts.items())),
        }


def run_sync(engine: SimulationEngine, *args, **kwargs) -> TemporalState:
    return asyncio.run(engine.run(*args, **kwargs))
