---
entity_id: "complex.ecocyc.CPLX0-8614"
entity_type: "complex"
name: "dTDP-4-amino-4,6-dideoxy-D-galactose acyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8614"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "dTDP-fucosamine acetyltransferase"
---

# dTDP-4-amino-4,6-dideoxy-D-galactose acyltransferase

`complex.ecocyc.CPLX0-8614`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8614`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27832|protein.P27832]]

## Enriched Summary

dTDP-fucosamine acetyltransferase catalyzes the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in the biosynthesis of Enterobacterial Common Antigen (ECA). Very little experimental work on this enzyme has been published. Crystal structures of RffC from the uropathogenic strain CFT073 (99% identical to the K-12 enzyme), both in the apo form and in complex with acetyl-CoA, have been solved at 1.95 and 1.66 Å resolution, respectively. The enzyme is homodimeric both in solution and in the crystal structure . Mutants with a defective rffC gene accumulate lipid III . An rffC EG11002 thyA double mutant, like wecF-, rfe-, and rffM-thyA double mutants, is hypersensitive to thymine starvation, likely because these mutants are unable to release dTDP from C55-PP-GLCNAC-MANNACA . Both rffC and wecF mutants show increased sensitivity to trimethoprim (which causes thymine/thymidine starvation). The increased sensitivity can be relieved by supplementation with deoxythymidine . dTDP-fucosamine acetyltransferase catalyzes the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in the biosynthesis of Enterobacterial Common Antigen (ECA). Very little experimental work on this enzyme has been published...

## Biological Role

Catalyzes TDPFUCACTRANS-RXN (reaction.ecocyc.TDPFUCACTRANS-RXN).

## Annotation

dTDP-fucosamine acetyltransferase catalyzes the synthesis of TDP-4-acetamido-4,6-dideoxy-D-galactose, which is utilized in the biosynthesis of Enterobacterial Common Antigen (ECA). Very little experimental work on this enzyme has been published. Crystal structures of RffC from the uropathogenic strain CFT073 (99% identical to the K-12 enzyme), both in the apo form and in complex with acetyl-CoA, have been solved at 1.95 and 1.66 Å resolution, respectively. The enzyme is homodimeric both in solution and in the crystal structure . Mutants with a defective rffC gene accumulate lipid III . An rffC EG11002 thyA double mutant, like wecF-, rfe-, and rffM-thyA double mutants, is hypersensitive to thymine starvation, likely because these mutants are unable to release dTDP from C55-PP-GLCNAC-MANNACA . Both rffC and wecF mutants show increased sensitivity to trimethoprim (which causes thymine/thymidine starvation). The increased sensitivity can be relieved by supplementation with deoxythymidine .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TDPFUCACTRANS-RXN|reaction.ecocyc.TDPFUCACTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P27832|protein.P27832]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8614`
- `QSPROTEOME:QS00182049`

## Notes

2*protein.P27832
