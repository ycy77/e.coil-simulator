# Audit report: reaction

- model: `/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B`
- vllm_url: `http://127.0.0.1:8000`
- audited: 2086
- by_class:
  - endogenous: 2025
  - exogenous-drug: 18
  - exogenous-chemical: 40
  - class-abstraction: 0
  - unsure: 3
- by_name_uniqueness:
  - unique: 2085
  - collides: 1

## Sample decisions

- `reaction.ecocyc.RXN-17008` ('RXN-17008'): endogenous / unique (conf 1.0)
  - rationale: This reaction is encoded by E. coli genes and catalyzes a physiological lipid metabolism step (acyl-CoA synthesis) using intracellular substrates, fitting the definition of an endogenous reaction.
- `reaction.ecocyc.RXN-16650` ('RXN-16650'): endogenous / unique (conf 1.0)
  - rationale: RXN-16650 is a peptidoglycan glycosyltransferase reaction encoded by E. coli K-12 and catalyzes a physiological step in cell wall biosynthesis, making it an endogenous reaction.
- `reaction.ecocyc.RXN-16909` ('RXN-16909'): endogenous / unique (conf 1.0)
  - rationale: The reaction HCO3 + ATP -> CPD-18238 + ADP is encoded by E. coli genes and catalyzed by endogenous enzymes, making it an intracellular metabolic reaction present in E. coli K-12 metabolism.
- `reaction.ecocyc.RXN-16330` ('RXN-16330'): endogenous / unique (conf 1.0)
  - rationale: This reaction (RXN-16330) is encoded in EcoCyc for E. coli K-12 and represents a metabolic step converting protoporphyrin IX to protoporphyrinogen, a process catalyzed by endogenous enzymes within the cell.
- `reaction.ecocyc.RXN-16804` ('RXN-16804'): endogenous / unique (conf 1.0)
  - rationale: This reaction (ARABINOSE-5P -> CPD-1818) is encoded by E. coli genes and catalyzed by the cell's own enzymes, making it an endogenous metabolic reaction present in E. coli K-12 metabolism.

## Ambiguous sample

- `reaction.ecocyc.RXN-16788` ('RXN-16788'): unsure (conf 0.9)
  - rationale: The annotation explicitly states that this reaction is in the Salmonella cobalamin biosynthetic pathway and it is not known if E. coli has an equivalent reaction. Since the reaction is not confirmed to be present in E. coli K-12, it cannot 
- `reaction.ecocyc.1.13.11.16-RXN` ('1.13.11.16-RXN'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 1 column 1623 (char 1622)
- `reaction.ecocyc.TRANS-RXN0-496` ('enterobactin export'): unsure (conf 0.0)
  - rationale: model reply was not parseable JSON: Unterminated string starting at: line 6 column 16 (char 123)
