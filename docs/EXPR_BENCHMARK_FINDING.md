# Finding: measured-DE direction is a sign-propagation ceiling, not a coverage gap

Date: 2026-06-15. Status: **negative result, scoping decision recorded** so nobody
re-spends GPU-hours deepening runs that cannot help.

## What we tested
The headline experiment (REMOTE_WORK_PLAN §6.3): knock out each regulator in the
simulator, predict each gene's expression direction, score against **measured**
differential expression from PRECISE-1K (SBRG, Lamoureux 2023; 1035 RNA-seq
samples). Tjaden was unreachable from the GPU host (GFW); PRECISE-1K replaced it
(`scripts/precise1k_to_de.py` → DE table; `scripts/benchmark_expression.py`).

## Numbers (the simulator vs measured fold-change direction)

Full 37-KO mock run:
- overall direction accuracy **0.485** (n=15243); **conflict subset 0.486** (n=4635)

8 master-regulator KOs (crp, cra, fur, oxyR, soxS, gadE, lon), mock vs llm:
| mode | overall | conflict |
| --- | --- | --- |
| mock | 0.572 (n=3394) | **0.557** (n=1010) |
| llm  | 0.560 | **0.544** |

→ LLM does **not** beat mock on the conflict subset; both ≈ chance.

## The decisive diagnostic — is it coverage or accuracy?
`scripts/diag_coverage.py` on `delcrp_glc` (881 measured-significant mappable
genes, 238 conflict), at increasing propagation depth:

| rounds | agents | moved | cov% | acc | conflict acc |
| --- | --- | --- | --- | --- | --- |
| 6 | 256 | 881 | **100.0** | 0.556 | 0.567 |
| 12 | 1024 | 881 | **100.0** | 0.556 | 0.555 |
| 20 | 4096 | 881 | **100.0** | 0.556 | 0.555 |

**Coverage is already 100% at the shallowest setting** (knocking out a global hub
like CRP wakes the whole graph in a few rounds), and **accuracy is invariant to
depth** (~0.556). So the bottleneck is **not** coverage and **not** propagation
depth — deeper runs cannot help.

## Why (the structural reason)
Measured fold-change direction after a global-regulator KO is the **net** of the
full quantitative network plus indirect/global effects (growth-rate shifts, DNA
supercoiling, metabolite-pool rebalancing). This simulator is a **sign-propagation**
model: it computes the sign of the *direct* effect, which is correct for direct
edges (see RegulonDB sign accuracy 100%) but cannot capture net genome-wide
effects. A gene directly de-repressed (↑) by the KO can move ↓ in the measured
data because of global rebalancing. mock and llm both ≈ chance here because the
limit is the *paradigm*, not the decision-maker.

## Decision
- **Do NOT** use genome-wide measured-DE direction as a paper headline. Report it
  as a scoping/limitation result.
- Quantitative claims live where sign-propagation is valid: **direct / single-
  regulator** targets (RegulonDB benchmark ≈ 97% direction accuracy) and the
  RegulonDB sign check (100%).
- The LLM's value is **local conflict resolution** shown by case-study traces, not
  a genome-wide statistic.

See [[measurement-and-plan]], `docs/COEXPRESSION_VALIDATION.md`, `docs/PAPER_FIGURE_PLAN.md`.
