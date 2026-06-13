# Changelog

Each entry is signed "session-N" so future contributors can diff
chunks at a glance.

## session-2026-06-13d — bug fixes (P1/P2) + global-view report agent

### Fixed
* **Phenotype false positives** (`reporter.py`). `_response_pattern_match` now
  (a) gates on the pattern's driving `signals` — a pattern only matches if the
  upstream sources it requires actually changed (a LacI-only run no longer
  scores the L2 `lac_dual_signal` pattern 1.0), and (b) scores
  `expected_abundance` on the abundance axis (no more cross-matching state vs
  abundance).
* **efficiency lost on resume / initial profile** (`temporal_state.py`).
  `from_snapshot` and `apply_initial_profile` now read/write the `efficiency`
  field; sequential perturbation runs no longer silently drop transcription
  efficiency.
* **Fragile grounding** (`grounding.py`). `EntityGrounder.candidates` now falls
  back to token-level matching (name/alias tier only) so `"knock out recA"` →
  recA and `"add ciprofloxacin"` → ciprofloxacin even if the LLM passes a raw
  span; full-phrase matches rank above generic single-token matches
  (`"DNA gyrase"` → gyrA, not the DNA metabolite).
* **Multi-word aliases destroyed** (`models.py`). New `alias_list()` keeps
  multi-word aliases whole AND adds their tokens, instead of replacing every
  space with `|`. `DNA gyrase` survives; `lacI b0345 JW0336` still tokenizes.
* **`--dry-run` misleading** (`parse_perturbation.py`) — now uses the hardened
  grounder, so a verb/stopword no longer outranks the real agent.
* **Fair retrieval** (`temporal_graphrag.py`). Candidates are now bucketed by
  their signal COMBINATION (crp-only / rpoS-only / crp+rpoS each a bucket) and
  round-robined, so a hub's unique targets are not starved and multi-source
  candidates are not mis-attributed to one source.

### Added — global-view report agent
* `ecoil_sim/report/llm_report_agent.py` `LLMReportAgent` + `prompts/report_agent.system.md`.
  After the run, a single agent with the FULL global view (perturbation sources,
  round-by-round propagation, causal chains, final states, phenotype matches +
  the involved entities' annotations) writes a grounded biological report. LLM
  injected (testable offline); wired into `main.py --llm-report`. No
  deterministic fallback narrative — without an LLM, the existing
  `Reporter.render_narrative` stands.
* Tests: `tests/test_report_agent.py`. Suite 55 → 57.

## session-2026-06-13c — LLM perturbation intake (offline scaffolding)

The product front door: user enters a perturbation by chat text or uploaded
file → LLM parses + grounds it to canonical graph entry points → user confirms →
run. No hand-written drug→target table (decisions to the model; the existing
`perturbation_knowledge.yaml` and fallback rules are left as test/baseline
scaffolding for now, not touched).

### Added (offline-verifiable; the LLM call is GPU-host-only)
* `ecoil_sim/sim/grounding.py` — `EntityGrounder`: ranks graph + perturbagen
  entities for a free-text mention (name/alias matches rank above annotation
  mentions so `recA` grounds to recA, not recB/recC).
* `ecoil_sim/sim/llm_perturbation.py` — `LLMPerturbationParser`
  (extract→ground→resolve→validate, LLM injected for testability) +
  `VLLMJsonCompleter` (real call) + `PerturbationProposal` (confirm render +
  engine changes). Deterministic guard rejects ids not in the graph and
  target_states outside `allowed_states`.
* `schemas/perturbation_intake.schema.json` (guided_json contract),
  `prompts/perturbation_parse.system.md`, `prompts/perturbation_ground.system.md`.
* `scripts/parse_perturbation.py` — both input adapters (`--text`, `--file`) over
  one grounding+confirm core; `--dry-run` previews grounding offline.
* Tests: `tests/test_grounding.py` (grounder on real graph + parser orchestration
  and guards with a stub LLM). Suite 50 → 55.
* Remote TODO recorded in `docs/REMOTE_WORK_PLAN.md` Phase 5 (run vs vLLM, web
  endpoints, confirm UI).

## session-2026-06-13b — guided decoding, fair retrieval, redundancy cleanup

Follows the remote scorecard report (`docs/SCORECARD_REPORT_20260613.md`),
acting on its hand-off priorities 1 and 2.

### Added / Changed (decision quality + scaling)
* **Guided decoding wired** (`ecoil_sim/llm/client.py`). `AsyncVLLMClient` now
  sends `guided_json` (the action schema) at the top level of the request, so
  the model is constrained to valid JSON actions — this targets the ~0.25 L2
  variance the report attributed to free-form decoding. Request building is now
  a testable `_build_payload`. Fixed a latent bug: the old `extra_body` block
  was nested under a key vLLM ignores on a raw POST (so `enable_thinking` never
  actually reached the server); extension fields are now top-level.
  Loaded via `load_guided_json()` from the model config's `structured_output`
  block; wired into `main.py`, `scripts/score_phenotypes.py`,
  `scripts/eval_baseline.py`.
* **`schemas/action.schema.json`** — added the missing `change_efficiency`
  action type. Without it, guided decoding would have forbidden a valid action
  the two-axis gene model needs. A test now asserts the schema enum is a
  superset of `ActionValidator.ACTION_TYPES`.
* **Fair candidate selection** (`ecoil_sim/retrieval/temporal_graphrag.py`).
  Replaced the global top-N truncation (which broke score ties by `entity_id`,
  systematically dropping high-id targets) with round-robin selection across
  the source hub, so a high-degree regulator can't starve another hub's
  targets. `scripts/score_phenotypes.py` default `--max-active-agents` 32 → 128.
* Note on report issue C (katG never wakes under OxyR): root cause is a
  **missing edge** — OxyR→katG does not exist in the baseline graph (OxyR only
  carries auto-regulation). This is a Phase-4 RegulonDB-structure gap, not a
  retriever bug. The fairness fix still removes the entity_id starvation class.

### Removed (redundant tracked files, ~95 MB, zero functional impact)
* `data/normalized/*.pre_canonical_v2` (3 backup files, 16.8 MB).
* Top-level `data/enriched/entities_enriched_v2*.{jsonl,csv}` +
  `enrichment_report_v2.json` (78 MB) — byte-identical duplicates of
  `data/enriched/_v2/`, which is the copy the web backend actually reads
  (`web/backend/main.py:64`). Verified no code reads the top-level v2 files.
* Left in place (NOT redundant): v1 enriched files (read by audit/verify/sim/
  web fallback), `data/enriched/_v2/` (web primary), `data/normalized/_v2`
  (web fallback), first-gen scripts (docs mark them "preserved"),
  `obsidian_vault/` (user vault), `runs/` + the ssh-config file (already
  gitignored, untracked local scratch).

### Tests
* 41 → 50. Added `tests/test_vllm_payload.py` (guided-decoding payload + schema
  coverage) and `tests/test_retrieval_fairness.py` (hub starvation).

## session-2026-06-13 — runnability fixes + engine↔baseline reconciliation

### Fixed (foundation — the project did not run out of the box)
* `requirements.txt` added (was missing). Core: PyYAML + httpx; web:
  fastapi + uvicorn; tests: pytest.
* `ecoil_sim/config.py` — `load_yaml_like` previously fell back to a
  hand-rolled mini-parser when PyYAML was absent, which silently
  *corrupted* nested config (block scalars, flow maps, lists became
  garbage; e.g. `expected_states: {}` parsed to the string `"{}"`,
  crashing the reporter). PyYAML is now a hard dependency and config
  loading fails loudly — in line with the #1 hard rule (no silent
  fallback).
* `ecoil_sim/report/reporter.py` — `_response_pattern_match` guards
  non-dict `expected_states`.
* `ecoil_sim/llm/response_parser.py` — truncated-JSON recovery rewritten.
  The old `rfind("{")` grabbed an inner action fragment and dropped the
  whole decision; now we balance brackets from the *outer* wrapper and
  drop only a dangling partial element. This is the #1 vLLM failure mode
  at high concurrency with small `decision_max_tokens`.

### Changed (cell rules — use the curated, STRING-dense baseline)
* `configs/simulation.yaml` — simulator now runs on
  `data/normalized/simulation` + `data/registry/simulation` (the curated
  baseline: endogenous-only, STRING PPIs integrated, reactions folded
  into produces/consumes). Density 4.6 edges/entity vs 1.9; isolated
  nodes 2% vs 20%; STRING was previously absent from the simulated graph.
* Engine now understands the baseline relation vocabulary
  (`interacts`, `produces`, `consumes`, `transcribed_as`, `paralog_of`,
  `bound_by`) across `configs/edge_weights.yaml`,
  `ecoil_sim/llm/signal_direction.py`, `configs/fallback_rules.yaml`,
  `ecoil_sim/agents/prompt_builder.py` (decision_policy), and
  `scripts/build_rule_registry.py`. Previously these 6 relation types
  (53% of baseline edges, all STRING PPIs) got a flat 0.1 noise weight.
* `ecoil_sim/models.py::Edge` now loads per-edge `edge_weight`
  (STRING confidence) + `string_channel`; `TemporalGraphRAG` scales the
  relation-type weight by per-edge confidence so a high-confidence PPI
  wakes its partner strongly and a weak one barely registers.
* PPI relations (`interacts`, `paralog_of`, `bound_by`) deliberately have
  NO deterministic fallback: a physical interaction carries no fixed
  direction, so the LLM is the sole decision-maker (decisions to the
  model; rules to the cell).

### Added
* `tests/test_engine_integration.py` — end-to-end lac-operon derepression
  on the baseline + glucose-log-phase profile, and a negative control.
* `tests/test_retrieval_ppi.py` — STRING PPI partners are woken on
  perturbation, with retrieval scores modulated by STRING confidence.
* `data/registry/simulation/native_rules.jsonl` — rule registry rebuilt
  from the baseline edges (49,742 rules).

## session-2026-06-10 — workspace governance + vLLM audit pipeline

### Added
* `scripts/audit_entities.py` — strict vLLM audit. 24,369 entities
  classified as `endogenous` / `exogenous-drug` / `exogenous-chemical`
  / `class-abstraction` / `unsure`. Auto-detects the served model
  from `/v1/models`. Supports `--concurrency N` and `--resume`.
  Refuses to silently fall back to mock / rules.
* `scripts/canonicalize_v2.py` — full-graph canonicalizer. Derives
  `family_key` from UniProt accession / EC number / KEGG compound id /
  complex components set / gene alias set; merges duplicate rows;
  rewrites edges; writes a globally-unique `display_name`; populates
  `is_exogenous` from the audit; outputs to `data/normalized/_v2/`
  with `--apply-in-place` promotion.
* `scripts/enrich_entities_v2.py` — multi-source enriched card
  builder. Walks every cross-source row listed in `merged_from`;
  unions annotations, aliases, external_ids; emits a richer summary
  than `enrich_entities.py` did.
* `scripts/verify_uniqueness.py` — invariant gate. Exit 1 on duplicate
  `entity_id`, duplicate `(entity_type, name)`, orphan edges, or
  enriched card missing canonical entity.
* `docs/PROJECT_OVERVIEW.md`, `docs/ARCHITECTURE.md`,
  `docs/DATA_DICTIONARY.md`, `docs/AUDIT_AND_CURATION.md`,
  `docs/ECOCYC_INGEST.md`, `docs/SIMULATION.md`,
  `docs/LLM_PROMPTS.md`, `docs/DIAGNOSTIC_UI.md`, this changelog.
* `docs/inventory/` — file / metric snapshots.

### Changed
* `README.md` rewritten as the single entry point. Old
  `docs/architecture.md` moved to `docs/architecture.legacy.md`.
* `web/frontend/src/components/SubgraphView.vue`:
  * default hop is now `1` (was `2`)
  * added per-mount request-sequence guard so an in-flight
    `/subgraph` response cannot overwrite a newer selection
  * explicit `redraw()` + `fit()` after `setData()` to defeat
    vis-network's internal cache.
* `web/backend/graph_service.py`:
  * `subgraph()` now bounds the BFS by hop distance instead of
    truncating by lexicographic id order
  * dedupes edges by `(source, relation, target, source_db,
    source_record_id)`

### Removed
* `data/raw/ecocyc/extracted/29.6/data/biopax-level2.owl` (74M)
* `data/raw/ecocyc/extracted/29.6/data/biopax-level3.owl` (71M)
* `data/raw/ecocyc/extracted/29.6/data/ecoli-COLI-K12-3659364498.fsa` (4.5M)
* `data/raw/ecocyc/extracted/29.6/data/dnaseq.fsa` (4.6M)
* `data/raw/ecocyc/extracted/29.6/data/protseq.fsa` (1.9M)
* `data/raw/ecocyc/extracted/29.6/data/{kb,fba,moleculardiagrams,reports,rawdata,input}/` (~250M)
* `data/raw/ecocyc/extracted/29.6/data/wc-model-29.0/`, `wc-model-29.1/` (16M)
* `data/raw/ecocyc/extracted/29.6/data/*.dat/.col/.gaf` files not consumed by
  `scripts/parse_ecocyc.py` (~100M across 23 files; the 10
  `.dat/.col` files that `parse_ecocyc.py` actually reads are kept)
* `data/raw/ecocyc/extracted/ecoli.tar.gz`
* `data/normalized/*.pre_canonical`, `*.pre_ecocyc` (26M)
* `scripts/__pycache__/`

### Invariants enforced (verify with `python scripts/verify_uniqueness.py --strict`)
* `entity_id` is unique
* `(entity_type, name)` is unique
* `display_name` is unique
* `family_key` is unique within `(entity_type,)`
* every edge source/target resolves to an entity or pathway id
* every enriched card maps to an entity id

## session-2026-06-09 — first diagnostic UI + initial conditions

* Stand up FastAPI + Vue 2 + vis-network on ports 28932 / 40211.
* `web/frontend/src/components/{EntitySearch,SubgraphView,EntityDetail,RunTimeline,DuplicateReport}.vue`.
* `web/backend/{data_loader,graph_service,run_service,enriched_loader}.py`.
* `data/enriched/entities_enriched.jsonl`, `entities_enriched_lite.jsonl`.
* `data/initial_conditions/glucose_log_phase.yaml`.

## session-2026-06-08 — first simulation loop

* `ecoil_sim/{agents,llm,graph,sim,registry,report,retrieval,rules,storage,state,validation,actions}/`.
* `scripts/parse_ecocyc.py`, `scripts/build_*.py`.
* `data/normalized/{entities,edges,pathways,canonical_entity_map,canonicalization_report}.csv/json`.
* `data/registry/native_rules.jsonl`.
## session-2026-06-13-v2 — phenotype battery + LLM reasoning fixes

Knobs driven from the scorecard run `runs/_scorecard/20260613_071545/`.
Full report in `docs/SCORECARD_REPORT_20260613.md`.

### Fixed
* `data/phenotypes/phenotype_db.yaml`:
  * `ara_dual_signal_arabinose_absent` used the wrong AraC id
    (`protein.P0ACT01`); replaced with `protein.P0A9E0` (the real UniProt
    accession in `data/normalized/simulation`).
  * Added `signals:` blocks to `beta_lactam_cell_wall_response`,
    `aminoglycoside_translation_response`,
    `oxidative_stress_response_like`, `cell_division_inhibition_like`,
    plus the new L2 / L3 patterns, so the scorer can drive them.
  * Adjusted `oxidative_stress_response_like` expected states to mirror
    what the graph actually encodes (OxyR auto-represses its own gene,
    SoxR auto-represses itself, katG is the activator target).
  * Removed `stringent_starvation_response_like` — RelA / SpoT have no
    `activates`/`represses` edges to genes in the simulation graph, so
    the pattern was unrunnable. Add back when the rule registry includes
    ppGpp → rpoS regulation.
  * Rewrote `sos_response_like` (L3) to use only the `LexA → SOS genes`
    pathway present in the graph (RecA carries no gene-regulation edges).
  * New L2 same-direction pattern `ara_induction_full` (ara operon,
    arabinose present + glucose absent).
  * Adjusted `lac_dual_signal_glucose_present` expected abundance from
    `low` → `medium` — current `_shift_abundance` semantics only have
    four tiers; "modest production" maps to `medium`.

* `ecoil_sim/actions/interpreter.py::_shift_abundance`:
  * Now honors `strength: 0` as a true no-op (was
    `step = max(1, strength)`, which contradicted the prompt's
    "strength: 1 = modest" guidance).
  * Added explicit `direction: "none"` no-op branch.

* `ecoil_sim/agents/prompt_builder.py`:
  * `public_neighbors` now exposes each changed neighbor's `efficiency`
    field. Without this the LLM could not see that its source gene was
    `expressed` but starved of activator, and overestimated the encoded
    protein's abundance.

* `prompts/agent_decision.system.md`:
  * Replaced the vague `strength: 1 = modest` hint with an explicit
    `efficiency → strength` table for the `encodes` rule.
  * Added explicit "two co-aligned signals ⇒ strength: 2" rule with
    the rationale ("cell heard this from two places").

### Measured impact
| Metric | Before | After |
| --- | --- | --- |
| `pytest -q`              | 41 passed | 41 passed |
| runnable patterns        | 8 (5 unrunnable) | 13 |
| L2 mock mean             | 0.17 (3) | 0.38 (4) |
| L2 LLM mean (repeat=2)   | n/a      | **0.43 (4)** |
| `lac_dual_signal_glucose_present` LLM | 0.50 | **0.58** (mean of 0.83, 0.33) |
| `glucose_to_lactose_shift` LLM        | 0.00 | **0.13** (mean of 0.00, 0.25) |

LLM now beats mock on L2 — the project's headline thesis — but variance
on the thesis case is still high (stdev 0.25). See report §6 issue B for
the recommended next step (wire `structured_output.require_json`
through `AsyncVLLMClient`).
