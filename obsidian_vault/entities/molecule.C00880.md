---
entity_id: "molecule.C00880"
entity_type: "small_molecule"
name: "D-Galactonate"
source_database: "KEGG"
source_id: "C00880"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Galactonate"
  - "D-Galactonic acid"
---

# D-Galactonate

`molecule.C00880`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00880`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Galactonate; D-Galactonic acid

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)

## Annotation

KEGG compound: D-Galactonate; D-Galactonic acid

## Pathways

- `eco00052` Galactose metabolism (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8287|complex.ecocyc.CPLX0-8287]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.GALACTONOLACTONASE-RXN|reaction.ecocyc.GALACTONOLACTONASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-16|reaction.ecocyc.TRANS-RXN-16]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTONDEHYDRAT-RXN|reaction.ecocyc.GALACTONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7315|reaction.ecocyc.RXN0-7315]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-16|reaction.ecocyc.TRANS-RXN-16]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0AA76|protein.P0AA76]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00880`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
