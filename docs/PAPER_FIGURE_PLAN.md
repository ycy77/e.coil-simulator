# Paper figure plan — E.coil (methods/systems + tool paper) — DATA-CALIBRATED v2

This revision (2026-06-15) is calibrated to what the validation actually showed.
Three negative results forced a reframe (all recorded, none hidden):
- genome-wide measured-DE direction ≈ chance, invariant to depth — a
  sign-propagation ceiling, not a coverage gap (`EXPR_BENCHMARK_FINDING.md`).
- co-expression validates activation but **not** repression (`COEXPRESSION_VALIDATION.md`).
- the self-authored phenotype battery is small and high-variance (`SCORECARD_REPORT_*`).

## The thesis (what we CAN defend)
**Not** "we predict the transcriptome better than FBA/rules."
**Instead:** a **knowledge-graph-grounded, agent-per-molecule, locally-reasoning
LLM simulator of E. coli that is mechanistically explainable and driven by natural
language** — whose regulatory directions are externally correct, whose direct
perturbation responses are faithful, and whose local model resolves specific
conflicts that deterministic rules abstain on.

Defensible claims, each with a real number/artifact:
1. The graph's regulatory **directions are correct** — RegulonDB sign **100%** (4072/4072).
2. **Direct** perturbation responses are **faithful** — single-regulator direction ≈ **97%**.
3. The local LLM makes **annotation-grounded calls where rules abstain** — conflict case-study traces.
4. A working **NL-perturbation tool** grounds drugs to targets with no hand table (cipro→GyrA/GyrB).
Scope (stated up front): it does **not** predict genome-wide measured fold-changes
(sign-propagation ceiling) — reported as a limitation, which is a rigor signal.

Venue: Bioinformatics (Application Note / methods), PLOS Comp Biol (methods), or
NAR Web Server (if UI-led). NOT a "predict the transcriptome" venue.

Status legend: ✅ now (offline) · 🖥️ remote (vLLM) · 🌐 net (host only).

---

## Figure 1 — The paradigm: agent-per-molecule with strict locality (HERO, unchanged)
| Panel | Content | Status |
|---|---|---|
| 1a | Three-layer thesis: cell=graph rules / model=LLM weighs conflicting signals / human=confirm+curation | ✅ |
| 1b | Locality contract: what an agent sees vs cannot see (lacZ example) — the novelty panel | ✅ |
| 1c | One round: perturbation → BFS wake → local LLM decision → validate → propagate; two-axis state | ✅ |
| 1d | vs FBA / Boolean / ODE / GNN: handles conflict · explainable · replayable · no fitted params | ✅ |

## Figure 2 — The substrate: curated, multi-source, validated KG (unchanged, strengthen)
| Panel | Content | Status |
|---|---|---|
| 2a | Entity-type + edge-relation composition; 4.6 edges/entity, 26,389 STRING PPIs | ✅ |
| 2b | Degree distribution (log–log), hubs CRP/OxyR/LexA | ✅ |
| 2c | Multi-source provenance (EcoCyc/KEGG/NCBI/UniProt/RegulonDB/STRING) | ✅ |
| 2d | Curation impact: audit + canonicalize_v2 (24,369 → unique; collisions resolved) | ✅ |
| 2e | Literature-grounded overlay: novel edges, separate from the validation graph (no recall inflation) | ✅ |

## Figure 3 — External validation: directions are correct (REWORKED — RegulonDB primary)
| Panel | Content | Source | Status |
|---|---|---|---|
| 3a | RegulonDB coverage waterfall: regulators 95.1% → targets 99.8% → present-as-edge 58.8% | validate_kg.py | ✅ |
| 3b | **Sign accuracy 100%** (4072/4072) — the headline correctness number | validate_kg.py | ✅ |
| 3c | **Direct/single-regulator perturbation ≈ 97% direction** — propagation fidelity where sign-prop is valid | benchmark_perturbation.py | 🖥️ |
| 3d | Structural gap: sigma/sRNA/ppGpp (362 interactions a gene→gene graph can't hold) | validate_kg.py | ✅ |
| 3e | (small) Co-expression on PRECISE-1K: **activation** corroborated (mean r +0.18, 73% r>0); note repression limit | validate_coexpression.py | ✅ (done) |

## Figure 4 — Explainability + conflict resolution (REWORKED — case studies, not a battery)
The LLM-value claim is narrow and shown by mechanism, not a noisy statistic.
| Panel | Content | Source | Status |
|---|---|---|---|
| 4a | Causal cascade of one perturbation over rounds (BFS frontier; reasons on each edge) | run history / report | ✅ |
| 4b | Feedback-loop detection (e.g. RpoS⇄RssB closes; cascade returns to source flagged) | report agent | ✅ |
| 4c | **Conflict case study — lac dual-signal**: the exact local view → LLM reasoning trace → action, vs why rules abstain | eval_baseline.py | 🖥️ |
| 4d | 1–2 more conflict traces (ara operator / SOS LexA) — literature-grounded, with DOI | eval_baseline.py | 🖥️ |
| 4e | (small) L2 battery mock vs llm as supporting evidence, framed as illustrative + honest variance | score_phenotypes.py | 🖥️ |

## Figure 5 — The product: NL perturbation intake + diagnostic UI (PROMOTED to main)
| Panel | Content | Status |
|---|---|---|
| 5a | NL intake end-to-end: "knock out recA, add 2mg/L ciprofloxacin" → recA→gene.b2699, cipro→GyrA/GyrB (no hand drug→target table) → confirm | 🖥️ (verified) |
| 5b | Diagnostic UI: graph + entity timeline + 验证看板 (KG/scorecard/literature panels) | ✅ |
| 5c | Scale: throughput vs agents-per-gpu (only if a clean scaling run lands) | 🖥️ optional |

## Appendix / Limitations (turn negatives into rigor)
- Measured-DE direction ≈ chance, invariant to depth — sign-propagation ceiling
  (`EXPR_BENCHMARK_FINDING.md`). Stated as the paradigm's boundary.
- Co-expression does not corroborate repression (repressor mRNA ≠ activity).
- Phenotype battery is curated/small — used for mechanism illustration, not as a
  primary quantitative claim.

---

## What changed from v1 and why
- Fig 3 main axis moved from "recall + co-expression" to **RegulonDB sign 100% +
  single-regulator 97%** (the numbers that survive scrutiny).
- Fig 4 changed from "LLM-beats-rules statistical battery" to **explainability +
  conflict case-study traces** (the battery was circular/noisy; measured-DE failed).
- Fig 5 (product) promoted from optional to a main figure — it's a real, demoable
  differentiator.
- Co-expression demoted to one supporting panel (activation only).
- Measured-DE moved to Limitations.

## Build order
Offline now: Fig 1, 2, 3a/b/d/e, 4a/b, 5b. Remote (vLLM): 3c, 4c/d/e, 5a. The
remote set is small, bounded, and on validators that hold — no more open-ended
"beat measured DE" runs.
