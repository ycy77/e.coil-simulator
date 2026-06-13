# Audit report: small_molecule

- model: `/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B`
- vllm_url: `http://127.0.0.1:8000`
- audited: 9900
- by_class:
  - endogenous: 5089
  - exogenous-drug: 276
  - exogenous-chemical: 4285
  - class-abstraction: 209
  - unsure: 41
- by_name_uniqueness:
  - unique: 9823
  - collides: 77

## Sample decisions

- `molecule.C00001` ('H2O'): endogenous / unique (conf 1.0)
  - rationale: H2O (water) is a fundamental intracellular metabolite produced and consumed by E. coli in metabolic reactions, not an external drug or chemical.
- `molecule.C00004` ('NADH'): endogenous / unique (conf 1.0)
  - rationale: NADH is a central intracellular cofactor produced and utilized by E. coli K-12 in metabolism, fitting the definition of an endogenous small molecule.
- `molecule.C00005` ('NADPH'): endogenous / unique (conf 1.0)
  - rationale: NADPH is a well-known intracellular cofactor produced and utilized by E. coli K-12 in metabolic pathways, fitting the definition of an endogenous small molecule.
- `molecule.C00006` ('NADP+'): endogenous / unique (conf 1.0)
  - rationale: NADP+ is a well-known intracellular cofactor produced and utilized by E. coli K-12 in metabolic pathways, fitting the definition of an endogenous small molecule.
- `molecule.C00034` ('Manganese'): exogenous-chemical / unique (conf 1.0)
  - rationale: Manganese is a heavy metal ion that E. coli does not synthesize; it is an environmental nutrient taken up from the medium, fitting the exogenous-chemical category.

## Ambiguous sample

- `molecule.C00272` ('Tetrahydrobiopterin'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 1 column 113 (char 112)
- `molecule.C00350` ('Phosphatidylethanolamine'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 1 column 113 (char 112)
- `molecule.C00750` ('Spermine'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 1 column 113 (char 112)
- `molecule.C00751` ('Squalene'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 6 column 16 (char 123)
- `molecule.C01036` ('4-Maleylacetoacetate'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 1 column 113 (char 112)
