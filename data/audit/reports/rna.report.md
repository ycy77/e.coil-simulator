# Audit report: rna

- model: `/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B`
- vllm_url: `http://127.0.0.1:8000`
- audited: 215
- by_class:
  - endogenous: 215
  - exogenous-drug: 0
  - exogenous-chemical: 0
  - class-abstraction: 0
  - unsure: 0
- by_name_uniqueness:
  - unique: 215
  - collides: 0

## Sample decisions

- `rna.b0668` ('glnW'): endogenous / unique (conf 1.0)
  - rationale: glnW is a tRNA-Gln encoded by E. coli K-12, present in its intracellular system, and not an external perturbation.
- `rna.b0244` ('thrW'): endogenous / unique (conf 1.0)
  - rationale: thrW is a tRNA-Thr encoded by E. coli K-12 (gene b0244), making it an endogenous RNA component of the cell.
- `rna.b0664` ('glnX'): endogenous / unique (conf 1.0)
  - rationale: glnX (b0664) is a tRNA-Gln encoded by the E. coli K-12 genome and is a standard intracellular RNA component.
- `rna.b0673` ('metT'): endogenous / unique (conf 1.0)
  - rationale: metT (b0673) is a tRNA-Met encoded by the E. coli K-12 genome and is a standard intracellular RNA component.
- `rna.b0536` ('argU'): endogenous / unique (conf 1.0)
  - rationale: argU (b0536) is a tRNA-Arg encoded by the E. coli K-12 genome and is a standard intracellular component used in protein synthesis.

## Ambiguous sample

