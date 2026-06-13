---
entity_id: "complex.ecocyc.CPLX0-7946"
entity_type: "complex"
name: "ribosomal protein S6 modification protein"
source_database: "EcoCyc"
source_id: "CPLX0-7946"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribosomal protein S6 modification protein

`complex.ecocyc.CPLX0-7946`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7946`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0C0U4|protein.P0C0U4]]

## Enriched Summary

RimK is an L-glutamate ligase that catalyzes post-translational addition of up to four C-terminal glutamate residues to EG10905-MONOMER (RpsF) . In addition, the enzyme is able to catalyze synthesis of poly-α-glutamate in vitro. The number of glutamate residues added to either RpsF or to poly-α-glutamate depends on the pH . RimK has a sequence motif that is predicted to mediate interaction with RNA . RimK is a member of the ATP-grasp superfamily; a crystal structure has been solved at 2.85 Å resolution . A rimK mutant exhibits a defect in the wild-type post-translational addition of C-terminal glutamate residues to RpsF . A mutation in rimK was found to confer neomycin and kanamycin resistance (nek) . Both rimK and rpsF deletion mutants reduce the basal level of SOS response and increase resistance to hydroxyurea . Nek: "neomycin and kanamycin" RimK is an L-glutamate ligase that catalyzes post-translational addition of up to four C-terminal glutamate residues to EG10905-MONOMER (RpsF) . In addition, the enzyme is able to catalyze synthesis of poly-α-glutamate in vitro. The number of glutamate residues added to either RpsF or to poly-α-glutamate depends on the pH . RimK has a sequence motif that is predicted to mediate interaction with RNA . RimK is a member of the ATP-grasp superfamily; a crystal structure has been solved at 2.85 Å resolution...

## Biological Role

Catalyzes RXN0-6726 (reaction.ecocyc.RXN0-6726).

## Annotation

RimK is an L-glutamate ligase that catalyzes post-translational addition of up to four C-terminal glutamate residues to EG10905-MONOMER (RpsF) . In addition, the enzyme is able to catalyze synthesis of poly-α-glutamate in vitro. The number of glutamate residues added to either RpsF or to poly-α-glutamate depends on the pH . RimK has a sequence motif that is predicted to mediate interaction with RNA . RimK is a member of the ATP-grasp superfamily; a crystal structure has been solved at 2.85 Å resolution . A rimK mutant exhibits a defect in the wild-type post-translational addition of C-terminal glutamate residues to RpsF . A mutation in rimK was found to confer neomycin and kanamycin resistance (nek) . Both rimK and rpsF deletion mutants reduce the basal level of SOS response and increase resistance to hydroxyurea . Nek: "neomycin and kanamycin"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6726|reaction.ecocyc.RXN0-6726]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C0U4|protein.P0C0U4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7946`
- `QSPROTEOME:QS00192115`

## Notes

4*protein.P0C0U4
