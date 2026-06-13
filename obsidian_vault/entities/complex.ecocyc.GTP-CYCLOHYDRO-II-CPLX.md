---
entity_id: "complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX"
entity_type: "complex"
name: "GTP cyclohydrolase 2"
source_database: "EcoCyc"
source_id: "GTP-CYCLOHYDRO-II-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GTP cyclohydrolase 2

`complex.ecocyc.GTP-CYCLOHYDRO-II-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GTP-CYCLOHYDRO-II-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7I7|protein.P0A7I7]]

## Enriched Summary

GTP cyclohydrolase II (RibA) catalyzes the opening of the imidazole ring of GTP and removal of pyrophosphate, the first committed step in riboflavin biosynthesis. GTP cyclohydrolase II is distinct from FOLE-CPLX, which is part of the FOLSYN-PWY tetrahydrofolate biosynthesis pathway. The removal of pyrophosphate without the ring-opening reaction is a side reaction of GTP cyclohydrolase II, yielding GMP as approximately 10% of the overall product . Purified GTP cyclohydrolase II is able to hydrolyze the damaged nucleotides 8-oxo-dGTP and 8-oxo-GTP to the respective monophosphates . The catalytic mechanism and kinetics of the enzyme have been studied . The reaction may involve the slow formation of a covalent phosphoguanosyl derivative during release of pyrophosphate . Three conserved cysteine residues are required for Zn2+ binding and catalytic activity of GTP cyclohydrolase II; zinc is not required for the pyrophosphate removal subreaction . Reinvestigation of the reaction found that RibA also hydrolyzes the reaction intermediate pyrophosphate, and that this cleavage reaction results in conformational changes of the enzyme . Crystal structures of GTP cyclohydrolase II alone and in complex with a GTP analogue have been determined, elucidating active site residues and enabling further insights into the catalytic mechanism...

## Biological Role

Catalyzes GTP-CYCLOHYDRO-II-RXN (reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN). Bound by Zinc cation (molecule.C00038), Magnesium cation (molecule.C00305).

## Annotation

GTP cyclohydrolase II (RibA) catalyzes the opening of the imidazole ring of GTP and removal of pyrophosphate, the first committed step in riboflavin biosynthesis. GTP cyclohydrolase II is distinct from FOLE-CPLX, which is part of the FOLSYN-PWY tetrahydrofolate biosynthesis pathway. The removal of pyrophosphate without the ring-opening reaction is a side reaction of GTP cyclohydrolase II, yielding GMP as approximately 10% of the overall product . Purified GTP cyclohydrolase II is able to hydrolyze the damaged nucleotides 8-oxo-dGTP and 8-oxo-GTP to the respective monophosphates . The catalytic mechanism and kinetics of the enzyme have been studied . The reaction may involve the slow formation of a covalent phosphoguanosyl derivative during release of pyrophosphate . Three conserved cysteine residues are required for Zn2+ binding and catalytic activity of GTP cyclohydrolase II; zinc is not required for the pyrophosphate removal subreaction . Reinvestigation of the reaction found that RibA also hydrolyzes the reaction intermediate pyrophosphate, and that this cleavage reaction results in conformational changes of the enzyme . Crystal structures of GTP cyclohydrolase II alone and in complex with a GTP analogue have been determined, elucidating active site residues and enabling further insights into the catalytic mechanism . Expression of ribA is inducible by paraquat and other superoxide-generating compounds and is dependent on SoxS . Overproduction of ribA reduces the mutation frequency of a mutT mutant strain . ribA is an essential gene . A ΔribA mutant is able to grow in medium supplemented with riboflavin . RibA: "riboflavin"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-II-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7I7|protein.P0A7I7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GTP-CYCLOHYDRO-II-CPLX`
- `QSPROTEOME:QS00195921`

## Notes

2*protein.P0A7I7
