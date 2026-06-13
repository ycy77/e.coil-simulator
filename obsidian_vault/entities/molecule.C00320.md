---
entity_id: "molecule.C00320"
entity_type: "small_molecule"
name: "Thiosulfate"
source_database: "KEGG"
source_id: "C00320"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thiosulfate"
  - "Hyposulfite"
---

# Thiosulfate

`molecule.C00320`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00320`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thiosulfate; Hyposulfite

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Thiosulfate; Hyposulfite

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (11)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9022|complex.ecocyc.CPLX0-9022]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-7-RXN|reaction.ecocyc.ABC-7-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-496|reaction.ecocyc.TRANS-RXN-496]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03132|reaction.R03132]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_substrate_of` --> [[reaction.ecocyc.ABC-7-RXN|reaction.ecocyc.ABC-7-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19033|reaction.ecocyc.RXN-19033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6385|reaction.ecocyc.RXN0-6385]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SULFOCYS-RXN|reaction.ecocyc.SULFOCYS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE--THIOL-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-496|reaction.ecocyc.TRANS-RXN-496]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-70-CPLX|complex.ecocyc.ABC-70-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00320`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
