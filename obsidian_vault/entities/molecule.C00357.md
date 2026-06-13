---
entity_id: "molecule.C00357"
entity_type: "small_molecule"
name: "N-Acetyl-D-glucosamine 6-phosphate"
source_database: "KEGG"
source_id: "C00357"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-D-glucosamine 6-phosphate"
  - "N-acetyl-α-D-glucosamine 6-phosphate"
---

# N-Acetyl-D-glucosamine 6-phosphate

`molecule.C00357`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00357`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-D-glucosamine 6-phosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: N-Acetyl-D-glucosamine 6-phosphate

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (9)

- `activates` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-9152|complex.ecocyc.CPLX0-9152]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2261|complex.ecocyc.MONOMER0-2261]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN|reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NANE-RXN|reaction.ecocyc.NANE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4641|reaction.ecocyc.RXN0-4641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-167|reaction.ecocyc.TRANS-RXN-167]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.NAG6PDEACET-RXN|reaction.ecocyc.NAG6PDEACET-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4661|reaction.ecocyc.RXN0-4661]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00357`
- `EcoCyc:CPD-16168`
- `REFMET:N-Acetylglucosamine 6-phosphate`
- `PUBCHEM:90658998`
- `canonicalized_from:molecule.ecocyc.CPD-16168`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.CPD-16168: EcoCyc:CPD-16168
