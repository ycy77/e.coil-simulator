# HANDOFF — the baton

Read [docs/LOOP_PROTOCOL.md](docs/LOOP_PROTOCOL.md) once. Then act only if it is
your TURN. Pull before you work, push when done.

---

## TURN: REMOTE
## CYCLE: 1

### TASK FOR REMOTE (run on the GPU host; needs vLLM + network)

```bash
cd /home/zkyd/data1/ycy/P_world/coil
git pull --rebase origin main
python -m pytest -q                                   # expect: 65 passed
curl -sS --max-time 5 http://127.0.0.1:8000/v1/models | head   # confirm vLLM up

# A) headline: does guided decoding lift L2 accuracy / cut variance?
python scripts/score_phenotypes.py --mode both --repeat 3

# B) RegulonDB-grounded perturbation benchmark, mock vs LLM
python scripts/benchmark_perturbation.py --mode both --max-tfs 80

# C) independent co-expression validation (Tjaden 2023 compendium)
python scripts/fetch_transcriptome_compendium.py --list      # inspect file names first
python scripts/fetch_transcriptome_compendium.py             # download expr + operon tables
python scripts/validate_coexpression.py --matrix data/raw/transcriptome_compendium/<EXPR_FILE>
#   if the header is genes-as-columns or odd, add --orient cols / --gene-col N / --delimiter ','

# D) try the LLM perturbation intake end to end
python scripts/parse_perturbation.py --text "knock out recA, add 2mg/L ciprofloxacin" --emit-changes

# E) try the global-view report agent on a real run
python main.py --use-llm --llm-report --perturbation "inhibit lacI" --rounds 5
```

### WHAT TO REPORT (write docs/reports/REPORT_cycle1.md from docs/reports/TEMPLATE.md)
- A) per-level mock vs llm means + L2 stdev across repeats.
- B) llm vs mock direction_accuracy + unreachable count.
- C) the expression file name you used, and activates `mean_r` vs represses `mean_r` + sign agreement.
- D) did cipro ground to gyrA/gyrB and recA to its gene? paste the proposal.
- E) paste the report agent's biological report; is it grounded / sensible?

### FIXES REMOTE MAY APPLY THIS CYCLE
- Only: the `validate_coexpression.py` flags (`--orient/--gene-col/--delimiter`) if the
  matrix format needs them — record the working invocation in the report.
- Anything else that breaks: describe it in the report, do NOT rewrite code.

### WHEN DONE
Edit this file: set `TURN: LOCAL`, bump nothing (LOCAL bumps CYCLE), fill RESULTS
below, then commit + push.

---

## RESULTS (REMOTE fills this before handing back)

- A) score_phenotypes:
- B) benchmark:
- C) co-expression:
- D) intake:
- E) report agent:
- pytest: 
- For LOCAL to address next:
