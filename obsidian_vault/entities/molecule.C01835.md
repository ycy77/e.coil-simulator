---
entity_id: "molecule.C01835"
entity_type: "small_molecule"
name: "Maltotriose"
source_database: "KEGG"
source_id: "C01835"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Maltotriose"
  - "Amylotriose"
---

# Maltotriose

`molecule.C01835`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01835`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Maltotriose; Amylotriose

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Maltotriose; Amylotriose

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-158|complex.ecocyc.MONOMER0-158]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.AMYLOMALT-RXN|reaction.ecocyc.AMYLOMALT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21092|reaction.ecocyc.RXN-21092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5182|reaction.ecocyc.RXN0-5182]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7347|reaction.ecocyc.RXN0-7347]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-503|reaction.ecocyc.TRANS-RXN0-503]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.R166-RXN|reaction.ecocyc.R166-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5183|reaction.ecocyc.RXN0-5183]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-503|reaction.ecocyc.TRANS-RXN0-503]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01835`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
