---
entity_id: "complex.ecocyc.CPLX0-242"
entity_type: "complex"
name: "thiosulfate sulfurtransferase GlpE"
source_database: "EcoCyc"
source_id: "CPLX0-242"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thiosulfate sulfurtransferase GlpE

`complex.ecocyc.CPLX0-242`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-242`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6V5|protein.P0A6V5]]

## Enriched Summary

GlpE is a sulfurtransferase of the rhodanese family that catalyzes the transfer of sulfur from thiosulfate to a recipient compound such as thioredoxin or cyanide, with thioredoxin thought to be the likely in vivo substrate . GlpE appears to be part of a ACSERLYB-MONOMER CysM-independent pathway for assimilation of thiosulfate . Based on analysis of deletion mutants, GlpE appears to carry out about 10% of the thiosulfate sulfurtransferase activity, with EG10780-MONOMER "PspE" accounting for approximately 85% . Enzymatic activity requires at least one of the protein's cysteine residues; the reaction likely proceeds via an enzyme-sulfur intermediate utilizing a double-displacement mechanism . A crystal structure of GlpE has been determined to 1.06 Å resolution . In contrast to results from native gel chromatography , GlpE is monomeric in the crystal structure . Cys65, the expected catalytic residue, is persulfurated in the crystal structure . NMR resonance assignments have been reported . A ΔEG10193 cysM mutant can grow very slowly on thiosulfate as a sulfur source. Overexpression of GlpE restores growth to wild-type levels . Expression of glpE is positively regulated by cAMP-CRP...

## Biological Role

Catalyzes RXN0-6385 (reaction.ecocyc.RXN0-6385), THIOSULFATE-SULFURTRANSFERASE-RXN (reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN).

## Annotation

GlpE is a sulfurtransferase of the rhodanese family that catalyzes the transfer of sulfur from thiosulfate to a recipient compound such as thioredoxin or cyanide, with thioredoxin thought to be the likely in vivo substrate . GlpE appears to be part of a ACSERLYB-MONOMER CysM-independent pathway for assimilation of thiosulfate . Based on analysis of deletion mutants, GlpE appears to carry out about 10% of the thiosulfate sulfurtransferase activity, with EG10780-MONOMER "PspE" accounting for approximately 85% . Enzymatic activity requires at least one of the protein's cysteine residues; the reaction likely proceeds via an enzyme-sulfur intermediate utilizing a double-displacement mechanism . A crystal structure of GlpE has been determined to 1.06 Å resolution . In contrast to results from native gel chromatography , GlpE is monomeric in the crystal structure . Cys65, the expected catalytic residue, is persulfurated in the crystal structure . NMR resonance assignments have been reported . A ΔEG10193 cysM mutant can grow very slowly on thiosulfate as a sulfur source. Overexpression of GlpE restores growth to wild-type levels . Expression of glpE is positively regulated by cAMP-CRP . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6385|reaction.ecocyc.RXN0-6385]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6V5|protein.P0A6V5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-242`
- `QSPROTEOME:QS00195421`

## Notes

2*protein.P0A6V5
