---
entity_id: "complex.ecocyc.FORMYLTHFDEFORMYL-CPLX"
entity_type: "complex"
name: "formyltetrahydrofolate deformylase"
source_database: "EcoCyc"
source_id: "FORMYLTHFDEFORMYL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "formyl-FH<sub>4</sub> hydrolase"
  - "formylTHF deformylase"
---

# formyltetrahydrofolate deformylase

`complex.ecocyc.FORMYLTHFDEFORMYL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FORMYLTHFDEFORMYL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37051|protein.P37051]]

## Enriched Summary

Formyltetrahydrofolate deformylase (PurU) appears to have two roles in E. coli metabolism. The first role is to provide the major source of formate to the cell under aerobic growth conditions. This was supported by the fact that a purU purN double mutant shows auxotrophy for either purine or formate under aerobic conditions. The second and possibly major role is to balance the pools of THF and 1-C-THF to ensure that synthesis of glycine can be maintained when the cell has excess purines, methionine and histidine and the biosynthetic pathways for these molecules are shut down . PurU activity is activated by methionine and inhibited by glycine . A hybrid protein created by assembling the C-terminal (N10-formyltetrahydrofolate binding) region of PurU and the N-terminal (GAR binding) region of GART-MONOMER PurN shows better activity and stability in terms of glycinamide ribonucleotide (GAR) transformylase activity . There is contradicting data regarding the growth phenotype of a purU mutant. report that a single purU mutant has no significant growth defect on minimal medium, while report that the severe growth defect of a strain containing a deletion of the C-terminal region of purU can be complemented by purU. A purU purN double mutant shows auxotrophy for either purine or formate under aerobic conditions...

## Biological Role

Catalyzes FORMYLTHFDEFORMYL-RXN (reaction.ecocyc.FORMYLTHFDEFORMYL-RXN).

## Annotation

Formyltetrahydrofolate deformylase (PurU) appears to have two roles in E. coli metabolism. The first role is to provide the major source of formate to the cell under aerobic growth conditions. This was supported by the fact that a purU purN double mutant shows auxotrophy for either purine or formate under aerobic conditions. The second and possibly major role is to balance the pools of THF and 1-C-THF to ensure that synthesis of glycine can be maintained when the cell has excess purines, methionine and histidine and the biosynthetic pathways for these molecules are shut down . PurU activity is activated by methionine and inhibited by glycine . A hybrid protein created by assembling the C-terminal (N10-formyltetrahydrofolate binding) region of PurU and the N-terminal (GAR binding) region of GART-MONOMER PurN shows better activity and stability in terms of glycinamide ribonucleotide (GAR) transformylase activity . There is contradicting data regarding the growth phenotype of a purU mutant. report that a single purU mutant has no significant growth defect on minimal medium, while report that the severe growth defect of a strain containing a deletion of the C-terminal region of purU can be complemented by purU. A purU purN double mutant shows auxotrophy for either purine or formate under aerobic conditions . Tgs: "transient glycine starvation" PurU:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FORMYLTHFDEFORMYL-RXN|reaction.ecocyc.FORMYLTHFDEFORMYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37051|protein.P37051]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:FORMYLTHFDEFORMYL-CPLX`
- `QSPROTEOME:QS00049707`

## Notes

6*protein.P37051
