# HANDOFF — the baton
Read [docs/LOOP_PROTOCOL.md](docs/LOOP_PROTOCOL.md) once. Then act only if it is
your TURN. Pull before you work, push when done.
---
## TURN: LOCAL
## CYCLE: 1
### TASK FOR LOCAL (work on the laptop; you do not need vLLM or network)
1. **Investigate `ara_dual_signal_arabinose_absent` regression (−0.33).** Cycle 1 report
   in [docs/reports/REPORT_cycle1.md](docs/reports/REPORT_cycle1.md). Yesterday this
   pattern scored 0.667; today 0.333. Upstream change is the guided-decoding work in
   6b606a4b. Open the `protein.P0A9E0` (AraC) action traces from
   `runs/_scorecard/20260614_111928/ara_dual_signal_arabinose_absent__llm__rep0/`
   and check whether `guided_json` is forcing `direction: down` (wrong) when the
   right answer is to emit no action at all (the activator's effect is occluded by
   the repressor). Schema fix or prompt clarification is the likely cure.
2. **Few-shot for co-aligned strength escalation.** Both `ara_induction_full` (LLM=0.0)
   and `glucose_to_lactose_shift` (LLM=0.5) under-escalate `strength: 2`. Add a worked
   example to `prompts/agent_decision.system.md`: one input where two upstream sources
   agree on direction, the model emits `direction: "up", strength: 2`, the result is
   `overexpressed`. Place it under the `encodes` rule section.
3. **Per-pattern aggregator.** REMOTE was forced to hand-aggregate cycle 1's LLM numbers
   because `score_phenotypes.py` only emits a single `scorecard.json` at the top of a
   `--mode both --repeat N` run. Add a flag (or a separate small script
   `scripts/aggregate_scorecards.py`) that scans `runs/_scorecard/*/scorecard.json`
   and emits the headline mock-vs-llm table per cycle.
4. **`score_phenotypes.py` shutdown hygiene.** A silent crash at `--repeat 3` left 24
   vLLM requests orphaned. Add a `try/finally` that on any exit drains in-flight vLLM
   requests and writes a partial `scorecard.json` per pattern so the cycle does not
   have to be re-run from scratch. Crash signature: vLLM shows 24 `num_requests_running`
   but no client process exists.
5. **`parse_perturbation.py` silent failure.** Cycle 1 ran it twice; both times exit 0
   with 0 bytes on stdout. Reproduce on the laptop with the same arg list and check
   whether it imports the LLM client at module load (no vLLM on laptop ⇒ ImportError
   swallowed by `try/except`) or whether the argparse is the failure point.
6. **Optional: tighten C and E.** Cycle 1 did not run `validate_coexpression.py` (task C)
   or the global-view report agent (task E) because REMOTE ran out of time after the
   scorecard crash recovery. If cycle 2 budget allows, REMOTE should do C with a real
   `--orient/--gene-col/--delimiter` probe so the workflow reaches the data, and E with
   the `inhibit lacI` perturbation end-to-end.
### WHEN DONE
Edit this file: set `TURN: REMOTE`, bump `CYCLE: 2`, write a new `TASK FOR REMOTE`
below, then commit + push.
---
## RESULTS (REMOTE filled this in cycle 1)
- A) score_phenotypes:
  * mock L0=1.000 L1=0.952 L2=0.500 L3=1.000
  * llm  L2=0.416 L3=1.000   (per-pattern, single repeat; L0/L1 only have mock numbers)
  * L2 per-pattern: lac_dual_signal **mock 0.50 → llm 0.83 (+0.33)**;
                    ara_dual_signal mock 1.00 → llm 0.33 (**−0.67 regression**);
                    glucose_to_lactose_shift mock 0.50 llm 0.50;
                    ara_induction_full mock 0.00 llm 0.00.
- B) benchmark_perturbation: **did not run** (REMOTE ran out of time after the
  `--repeat 3` crash recovery).
- C) co-expression: **did not run** (no network egress from REMOTE sandbox for
  `fetch_transcriptome_compendium`).
- D) intake: **`parse_perturbation.py` silent failure** — both invocations exit 0
  with 0 bytes stdout. Filed as bug in report §"What worked / what broke".
- E) report agent: **did not run** (time).
- pytest: **65 passed**.
- For LOCAL to address next: see TASK FOR LOCAL above (6 items).
