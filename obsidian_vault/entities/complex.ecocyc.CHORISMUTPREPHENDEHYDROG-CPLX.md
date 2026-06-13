---
entity_id: "complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX"
entity_type: "complex"
name: "fused chorismate mutase/prephenate dehydrogenase"
source_database: "EcoCyc"
source_id: "CHORISMUTPREPHENDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "T-protein"
  - "chorismate mutase-prephenate dehydrogenase"
  - "chorismate mutase-prephenate:NAD+ oxidoreductase(decarboxylating)"
---

# fused chorismate mutase/prephenate dehydrogenase

`complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CHORISMUTPREPHENDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07023|protein.P07023]]

## Enriched Summary

Bifunctional chorismate mutase / prephenate dehydrogenase (TyrA) carries out the shared first step in the parallel biosynthetic pathways for the aromatic amino acids tyrosine and phenylalanine, as well as the second step in tyrosine biosynthesis. TyrA catalyzes both the conversion of chorismate into prephenate and the subsequent NAD+-dependent oxidative decarboxylation of prephenate . The two catalytic activities of TyrA occur in separate portions of the protein, and are partially separable via mutation. Specifically, the chorismate mutase activity requires the amino-terminal portion of the protein, and the prephenate dehydrogenase activity is in the carboxy-terminal portion of the protein. Each isolated activity is markedly diminished when compared with its normal levels in whole TyrA . The dehydrogenase activity can also be deactivated via point mutations that disrupt NAD+ binding. These mutations do not, in turn, disable chorismate mutase function . A single sulfhydryl group within the protein is critical for both activities, despite their apparent localizations in different portions of the protein . TyrA can occur as both a dimer and a tetramer. It is typically detected as an active dimer, and even the isolated amino- and carboy-terminal portions described above can dimerize independent of their missing halves...

## Biological Role

Catalyzes CHORISMATEMUT-RXN (reaction.ecocyc.CHORISMATEMUT-RXN), PREPHENATEDEHYDROG-RXN (reaction.ecocyc.PREPHENATEDEHYDROG-RXN).

## Annotation

Bifunctional chorismate mutase / prephenate dehydrogenase (TyrA) carries out the shared first step in the parallel biosynthetic pathways for the aromatic amino acids tyrosine and phenylalanine, as well as the second step in tyrosine biosynthesis. TyrA catalyzes both the conversion of chorismate into prephenate and the subsequent NAD+-dependent oxidative decarboxylation of prephenate . The two catalytic activities of TyrA occur in separate portions of the protein, and are partially separable via mutation. Specifically, the chorismate mutase activity requires the amino-terminal portion of the protein, and the prephenate dehydrogenase activity is in the carboxy-terminal portion of the protein. Each isolated activity is markedly diminished when compared with its normal levels in whole TyrA . The dehydrogenase activity can also be deactivated via point mutations that disrupt NAD+ binding. These mutations do not, in turn, disable chorismate mutase function . A single sulfhydryl group within the protein is critical for both activities, despite their apparent localizations in different portions of the protein . TyrA can occur as both a dimer and a tetramer. It is typically detected as an active dimer, and even the isolated amino- and carboy-terminal portions described above can dimerize independent of their missing halves . A mol of dimerized TyrA can bind roughly one mol of NAD+, one mol of tyrosine, or one mol of prephenate. In the simultaneous presence of NAD+ and tyrosine, TyrA forms a tetramer rather than a dimer . In addition to the 88 kD value, molecular weights of 78.8 kD for the dimer and 136 kD for the tetrameric form have been reported . TyrA and engineered derivatives of TyrA have been used in metabolic engineering studies for the overproduction of L-tyrosine in Esc

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PREPHENATEDEHYDROG-RXN|reaction.ecocyc.PREPHENATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07023|protein.P07023]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CHORISMUTPREPHENDEHYDROG-CPLX`
- `QSPROTEOME:QS00049582`

## Notes

2*protein.P07023
