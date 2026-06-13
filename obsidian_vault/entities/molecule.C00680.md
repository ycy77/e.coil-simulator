---
entity_id: "molecule.C00680"
entity_type: "small_molecule"
name: "meso-2,6-Diaminoheptanedioate"
source_database: "KEGG"
source_id: "C00680"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "meso-2,6-Diaminoheptanedioate"
  - "meso-2,6-Diaminopimelate"
  - "meso-2,6-Diaminopimelic acid"
  - "meso-Diaminoheptanedioate"
---

# meso-2,6-Diaminoheptanedioate

`molecule.C00680`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00680`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: meso-2,6-Diaminoheptanedioate; meso-2,6-Diaminopimelate; meso-2,6-Diaminopimelic acid; meso-Diaminoheptanedioate EcoCyc common name: meso-diaminopimelate.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

KEGG compound: meso-2,6-Diaminoheptanedioate; meso-2,6-Diaminopimelate; meso-2,6-Diaminopimelic acid; meso-Diaminoheptanedioate

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.DIAMINOPIMEPIM-RXN|reaction.ecocyc.DIAMINOPIMEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-961|reaction.ecocyc.RXN0-961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-291|reaction.ecocyc.TRANS-RXN-291]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00451|reaction.R00451]] `KEGG` `database` - C00680 <=> C00047 + C00011
- `is_substrate_of` --> [[reaction.R02788|reaction.R02788]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_substrate_of` --> [[reaction.ecocyc.DIAMINOPIMDECARB-RXN|reaction.ecocyc.DIAMINOPIMDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-291|reaction.ecocyc.TRANS-RXN-291]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00680`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
