# Simulation

## Loop

For a given `initial_conditions/<name>.yaml` and a list of perturbations:

1. The `SimulationEngine` seeds `AgentState` for every entity listed in
   the initial profile.
2. The engine applies each perturbation by walking the graph one hop
   at a time. A perturbation is a tuple `(entity_id, new_state)`.
3. After every state change, the engine re-schedules all
   `outgoing_by_relation` neighbours that should react.
4. When an Agent wakes, the engine asks the prompt builder to compose
   its local prompt, calls the LLM (or mock), validates the returned
   action, and applies it via `ActionInterpreter`.
5. The new state is committed to `simulation_store` and the loop
   repeats until no Agent is schedulable or `max_rounds` is hit.

## The local prompt

Each Agent sees:

* `you.entity_id`, `you.entity_type`, `you.public_id_hint`,
  `you.display_name`, `you.name`
* `you.your_state.{state, efficiency, abundance}`
* `signals_propagated`: list of `{source_id, relation, new_state}`
* `candidate_rules`: rules that touch this entity
* `local_knowledge.environment` + `local_knowledge.rules`

It does **not** see:

* the original perturbation text
* the global graph topology
* any state change that did not propagate to it

## Action vocabulary

Defined in `ecoil_sim/actions/schemas.py` and validated by
`ecoil_sim/validation/action_validator.py`:

* `change_state`
* `change_efficiency`
* `change_abundance`
* `change_mrna_abundance`
* `change_activity`

Every action carries:

* `action_type`
* `rule_id` (must be in `data/registry/native_rules.jsonl`)
* `targets`: list of canonical entity ids
* `direction`: `up` / `down` / `keep`
* `strength`: 1–3
* `reason`: short biological explanation

## Phenotype expectations

`data/phenotypes/phenotype_db.yaml` defines what "success" looks like
for each perturbation class:

* `L0` — direct state change, no propagation expected
* `L1` — single-hop propagation
* `L2` — multi-hop conflict, LLM must reason about net effect
* `L3` — multi-step cascade, full reasoning required

`scripts/eval_baseline.py` runs mock + LLM on each phenotype and
emits a per-pattern comparison report. The reporter uses
`display_name` + first-mention `[id]` brackets so the human reading
the report sees exactly the names shown in the diagnostic UI.

## Output

Every run writes under `runs/<timestamp>/`:

```
runs/<ts>/
  meta.json                 # input profile + perturbations + config
  rounds/round_<N>.json     # full state snapshot per round
  agents/<entity_id>.json   # full AgentState history for that entity
  stage_reports/new_changes.json
  stage_reports/uncertain.json
```

`web/backend/run_service.py` exposes these via
`/api/runs`, `/api/runs/{id}/timeline`,
`/api/runs/{id}/agents/{entity_id}`.