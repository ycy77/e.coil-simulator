# LLM Prompts

The simulator uses one LLM — the local Qwen3.5-9B served at
`http://127.0.0.1:8000`. There are two distinct prompt surfaces:

1. **Audit prompt** (per entity, in `scripts/audit_entities.py`)
2. **Agent decision prompt** (per Agent per round, in
   `ecoil_sim/agents/prompt_builder.py`)

They share design constraints but solve different problems.

## Audit prompt

Goal: classify every entity exactly once. Output is strict JSON.
Prompt body, paraphrased:

```
You audit E. coli biology knowledge-graph entities. The model is
E. coli K-12. The simulation treats each entity as an Agent that can
exist in the initial intracellular system or only as an externally
added perturbation. Classify strictly:
  - endogenous: a component the cell makes / uses by itself
  - exogenous-drug: an antibiotic / therapeutic / probe that is NOT
    produced by E. coli
  - exogenous-chemical: a non-drug chemical that E. coli does not
    produce
  - class-abstraction: a name that denotes an entire compound class
  - unsure: only if the raw signals are truly insufficient

For entity_type == 'reaction' or 'rna' choose endogenous when the
reaction/RNA is encoded by E. coli and present in E. coli metabolism.
Do NOT return unsure for things that obviously belong in one bucket.

Also judge name uniqueness; if the same (entity_type, name) is reused
across multiple entity_ids, return name_uniqueness='collides' and list
the other ids in collides_with.
```

The audit **never** falls back to mock. If the model reply is not
parseable JSON, the entity is rerouted to `ambiguous/` with
`audit_method=parse_error`.

## Agent decision prompt

Goal: at each round, decide how the Agent's state should change in
response to the propagated signals. Prompt body, paraphrased:

```
You are one molecule in a single E. coli cell.
You only see what propagated to you.
You do NOT know the global perturbation.
You decide only your own new state.

Inputs you receive:
  - your entity_id, entity_type, display_name
  - your current state, efficiency, abundance
  - propagated signals: source_id, relation, new_state
  - local candidate rules
  - your annotation summary + linked_entities

Two-axis decision (gene only):
  - state (permissibility)
  - efficiency (rate)
If a single round requires both, emit two actions.

Output: JSON list of actions, each with
  {action_type, rule_id, targets, direction, strength, reason}.
```

The action validator rejects any action whose `rule_id` is not in
`native_rules.jsonl`, whose `targets` are not in `entities.csv`, or
whose `strength` is out of range.

## First-mention bracket format

When the prompt or the report mentions an entity, the convention is:

```
<display_name> (<entity_id>)
```

The first mention carries the id in brackets; subsequent mentions
drop the id and use `display_name` only. The reporter in
`ecoil_sim/report/reporter.py` implements this with `_labeled()`.

## Prompt builder quirks

* `Promp tBuilder.attach_enriched(enriched_service)` is called once
  after the engine is constructed. The service is **not** imported
  statically to avoid the circular import between
  `ecoil_sim.agents.prompt_builder` and
  `ecoil_sim.sim.enriched_service`.
* The prompt builder selects between `enriched.summary` (when quality
  is informative and length >= 40) and the raw `annotation` field.
* `linked_entities` in the prompt are top-N by in-edge weight, not
  arbitrary — see `_linked_entities_for_prompt` in
  `ecoil_sim/agents/prompt_builder.py`.