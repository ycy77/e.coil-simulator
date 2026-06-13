# Remote work plan — for the vLLM-equipped agent

This document is written for an agent (or engineer) working **on the remote
server where the vLLM Qwen3.5-9B endpoint is reachable**. The local laptop
sessions cannot reach the model (`base_url` is `http://localhost:8000/v1` on the
GPU host), so everything that needs real LLM inference is queued here.

Read [`README.md`](../README.md) and [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md)
first. The one-line thesis: **decisions to the model, rules to the cell, judgment
to humans.** The model must run — deterministic rules cannot resolve conflicting
signals on a node; that is precisely the LLM's job.

## What already changed (session 2026-06-13)

See [`docs/CHANGELOG.md`](CHANGELOG.md). In short:

1. **The project runs now.** Missing `requirements.txt` added; PyYAML is a hard
   dependency (config used to corrupt silently without it); a truncated-JSON
   decision-recovery bug (the #1 vLLM failure mode) was fixed.
2. **The simulator now runs on the curated, STRING-dense baseline**
   (`data/normalized/simulation` + `data/registry/simulation`), not the sparse
   full graph. 26,389 STRING PPI edges are now live in the scheduler, weighted by
   per-edge confidence. PPI edges wake neighbours but carry **no deterministic
   action** — the LLM decides their effect.
3. **A quantitative scorer exists**: [`scripts/score_phenotypes.py`](../scripts/score_phenotypes.py).
   Mock baseline today: **L0=1.00, L1=1.00, L2=0.17**. L2 is where the model has
   to earn its keep.

All 41 tests pass: `python -m pytest -q`.

## Environment

```bash
# On the GPU host (conda env `world` per configs/model.qwen35_9b.yaml):
bash scripts/start_vllm.sh --gpus 2 --devices 6,7 --port 8000 &
# health check:
curl -s http://127.0.0.1:8000/v1/models | head

# The simulator/eval code env (PyYAML, httpx, fastapi, uvicorn, pytest):
pip install -r requirements.txt
python -m pytest -q          # must stay green
```

Model facts (from `configs/model.qwen35_9b.yaml`): Qwen3.5-9B, TP=2,
`max_model_len=65536`, `decision_max_tokens=512`, temp 0.2, top_p 0.8,
thinking disabled via `qwen35_no_thinking.jinja`.

---

## Phase 1 — Make model decisions measurable (PRIORITY 1)

Goal: produce the headline number — *how much accuracy does the LLM add over the
mock per signal level*, with variance.

```bash
# Sanity: deterministic baseline (no GPU needed)
python scripts/score_phenotypes.py --mode mock

# The headline run (needs vLLM up). --repeat captures temperature variance.
python scripts/score_phenotypes.py --mode both --repeat 3
# Output: runs/_scorecard/<ts>/scorecard.md + scorecard.json
```

Read `scorecard.md`. The **acceptance bar**:

- **L0 = 1.00** for both modes (negative control: no spurious changes). If the
  LLM breaks this, it is hallucinating changes with no signal — fix the prompt
  before anything else.
- **L1 ≈ 1.00** for the LLM (single-signal cases the mock also gets right).
- **L2(llm) > L2(mock)=0.17** by a clear margin. This is the whole thesis. If
  they tie, the LLM is not paying for itself on conflict resolution — go to
  Phase 2.
- `stdev_score` per pattern should be low. High variance ⇒ the prompt is
  under-constraining the model; tighten it (Phase 2).

For deep qualitative inspection of *why* a pattern scored as it did, use the
reasoning-trace tool: [`scripts/eval_baseline.py`](../scripts/eval_baseline.py)
(`--mode both --level L2`). It re-derives the exact local view each agent saw.

### Data fixes this phase will surface (judgment to humans)

The scorer already flags these — fix in `data/phenotypes/phenotype_db.yaml`:

- `ara_dual_signal_arabinose_absent` references **`protein.P0ACT01`** which is not
  a real id (AraC is `P0A9E0`; confirm it and the araBAD genes `b0061/b0062/b0063`
  exist in the baseline with `grep`). Without a valid source the pattern can't run.
- Six patterns have **no `signals` block** (`beta_lactam_cell_wall_response`,
  `aminoglycoside_translation_response`, `oxidative_stress_response_like`,
  `stringent_starvation_response_like`, `cell_division_inhibition_like`,
  `sos_response_like`). They define `expected_states` but no perturbation to drive
  them, so they are unrunnable. Add a `signals` block (the upstream source + the
  state it takes after perturbation) to bring each into the scored battery.
- Expand the **L2/L3 battery**. L2+ is the only level that proves the model's
  value; today there are 3 L2 patterns and 0 runnable L3. Add conflict cases
  (two upstream signals pushing opposite directions) grounded in real edges.

---

## Phase 2 — Improve model decision quality

Iterate against the Phase-1 scorecard. Levers, roughly in order of expected ROI:

1. **Structured decoding.** `configs/model.qwen35_9b.yaml` declares
   `structured_output.require_json` + `schemas/action.schema.json`, but
   `AsyncVLLMClient` (`ecoil_sim/llm/client.py`) does not yet send vLLM's
   `guided_json` / `response_format`. Wiring guided JSON eliminates parse
   failures and truncation entirely. Verify scores and `parse_diagnostics`
   (in run metadata) improve.
2. **Prompt / conflict resolution.** The system prompt is
   [`prompts/agent_decision.system.md`](../prompts/agent_decision.system.md); the
   per-agent `decision_policy` and conflict hints are built in
   `ecoil_sim/agents/prompt_builder.py` and `ecoil_sim/llm/signal_direction.py`.
   The L2 thesis case (`lac_dual_signal_glucose_present`) needs the model to
   reason "promoter unblocked but activator missing ⇒ abundance stays *low*".
   Tune the hint wording and the `interacts` policy note; re-score.
3. **Two-axis gene model.** Genes carry transcription state (`expressed`/
   `repressed`) AND efficiency (`change_efficiency`); proteins carry activity.
   Confirm the model uses the right axis (the prompt explains it; test on L1
   `lactose_induction_like`, which expects both gene expression and protein
   abundance).
4. **PPI decisions.** `interacts` edges now wake partners with no default action.
   Spot-check that the model makes *biologically sensible, annotation-grounded*
   calls on PPI partners and does not rubber-stamp every interaction. This is the
   purest test of "decisions to the model".

Keep `python -m pytest -q` green throughout. Add a regression test when you lock
in a behaviour.

---

## Phase 3 — Scale to hundreds/thousands of concurrent agents

Only meaningful once Phase 1 shows good per-decision accuracy (scaling a wrong
decision just makes more wrong decisions). Measure before optimizing.

Run a large perturbation and watch wall-clock + GPU utilization:

```bash
python main.py --use-llm --gpus 2 --agents-per-gpu 200 \
  --perturbation "knock out rpoS" --rounds 6
```

Known bottlenecks (verify with a profiler before touching):

- **Retriever** (`ecoil_sim/retrieval/temporal_graphrag.py`) recomputes scores
  for every neighbour of every changed agent each round, no caching. On the
  dense baseline (hub degree up to ~1,300) this can dominate. Consider caching
  incident-edge weights and capping fan-out per hub.
- **Concurrency** is gated by `max_concurrency = gpu_count * max_concurrency_per_gpu`
  (`configs/simulation.yaml`, default 50/GPU). Raise it toward what vLLM can
  actually sustain; watch for timeouts (`timeout_seconds`, retries).
- **Storage** (`ecoil_sim/storage/store.py`) writes one JSON per round plus
  per-agent history files. At thousands of agents × rounds this is heavy I/O;
  batch writes or make per-agent dumps opt-in.
- `max_active_agents` (CLI / `simulation.yaml`) caps agents woken per round; it is
  the main knob trading breadth vs cost.

Acceptance: a run with N≈1000 active agents/round completes without timeouts, and
throughput (agents/sec) scales roughly linearly with `agents_per_gpu` until the
GPU saturates.

---

## Phase 4 — Cell-rule quality (ongoing, the user's top long-term axis)

The graph is the cell's rule-set. Higher-value graph work:

- **Audit the unaudited types.** `scripts/audit_entities.py` skips
  gene/protein/complex (assumed endogenous). Run the strict vLLM audit over them
  to catch exogenous/mis-classified entries; ~50 entities currently have no audit
  decision.
- **Reconcile reaction namespaces.** EcoCyc frame-id reactions and KEGG R-number
  reactions are not merged; the same reaction can appear twice. (Reactions are
  folded out of the baseline, but this matters if you re-expand them.)
- **RegulonDB structure.** Only TF→gene edges are imported; operons,
  transcription units, promoters and binding sites are dropped. Adding them
  enables real L3 conflict patterns (AND/OR operator logic) — currently the
  blocker for the L3 battery.
- **Optional gene fold.** Genes with no incoming regulation that are pure
  degree-1 pass-throughs to one protein add scheduling cost without modeling
  value. Folding them (keeping regulated genes as the transcription axis) is a
  defensible optimization — but verify it does not drop edges the model needs.
  Discuss with the user first; this changes the entity model.

---

## Phase 5 — Perturbation intake (the product front door)

The end-user enters a perturbation by **chat text or uploaded file**; the model
parses it, **grounds it to canonical graph entry points**, the user **confirms**,
then the simulation runs. No hand-written drug→target table — the LLM infers
targets from entity annotations (decisions to the model; judgment to humans at
the confirm step).

Built offline this session (verified without vLLM):
- `ecoil_sim/sim/grounding.py` — `EntityGrounder`: ranks graph + perturbagen
  entities for a mention (name/alias ≫ annotation). Tested: `recA`→gene.b2699,
  "DNA gyrase"→gyrA/gyrB, "penicillin-binding protein"→PBPs.
- `ecoil_sim/sim/llm_perturbation.py` — `LLMPerturbationParser` (extract→ground→
  resolve→validate) with the LLM injected; `VLLMJsonCompleter` for the real call;
  `PerturbationProposal.render()` for the confirm block; `.to_engine_changes()`
  feeds the engine. Deterministic guard: drops any `entity_id` not in the graph
  or `target_state` outside `allowed_states`.
- `schemas/perturbation_intake.schema.json` (guided_json contract),
  `prompts/perturbation_{parse,ground}.system.md`.
- `scripts/parse_perturbation.py` — both adapters: `--text` (chat), `--file`
  (upload); `--dry-run` previews grounding offline.

Remote work to finish it:
1. **Run it against vLLM** and tune the two prompts:
   `python scripts/parse_perturbation.py --text "knock out recA, add 2mg/L ciprofloxacin" --emit-changes`
   Check: cipro grounds to gyrA/gyrB (`exogenous`), recA to gene.b2699, and
   `target_state`s are valid. The drug→target inference quality lives entirely in
   `prompts/perturbation_parse.system.md` (`target_concepts`) — iterate there.
2. **Web endpoints** (`web/backend/`): `POST /api/perturbation/parse` (body: text
   or uploaded file) → returns `PerturbationProposal` JSON for the UI to render;
   `POST /api/perturbation/run` (body: confirmed/edited perturbations) → kicks off
   a run via the engine. Reuse `LLMPerturbationParser`.
3. **Confirm UI** (`web/frontend/`): show grounded entry points + targets +
   evidence; let the user edit/approve before running. This is the human-judgment
   boundary — do not auto-run.
4. The offline `--dry-run` token preview is noisy on multi-word concepts (it has
   no LLM to clean mentions); that is preview-only and not the production path.

## Guardrails (do not violate)

- **No silent fallback.** If the LLM/endpoint is unreachable, fail loudly. Do not
  route through mock/rules to "make progress" (this is the project's #1 rule).
- **Edges only between canonical ids**; orphans are reported, not dropped.
- **Keep the test suite green** (`python -m pytest -q`) and add a test when you
  lock in any new behaviour.
- When you change a config default or the graph wiring, update
  [`docs/CHANGELOG.md`](CHANGELOG.md) and the relevant memory note.

## Command quick-reference

```bash
python -m pytest -q                                   # 41 tests, must pass
python main.py --mock-llm --entity protein.P03023 --state inhibited   # offline smoke
python main.py --use-llm --perturbation "inhibit lacI" --rounds 5     # real model
python scripts/score_phenotypes.py --mode both --repeat 3             # headline metric
python scripts/eval_baseline.py --mode both --level L2                # qualitative traces
bash web/start.sh                                                     # diagnostic UI
```
