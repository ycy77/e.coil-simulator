---
entity_id: "molecule.C03383"
entity_type: "small_molecule"
name: "D-Galactono-1,4-lactone"
source_database: "KEGG"
source_id: "C03383"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Galactono-1,4-lactone"
  - "gamma-D-Galactonolactone"
---

# D-Galactono-1,4-lactone

`molecule.C03383`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03383`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Galactono-1,4-lactone; gamma-D-Galactonolactone

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)

## Annotation

KEGG compound: D-Galactono-1,4-lactone; gamma-D-Galactonolactone

## Pathways

- `eco00052` Galactose metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-522|reaction.ecocyc.TRANS-RXN0-522]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTONOLACTONASE-RXN|reaction.ecocyc.GALACTONOLACTONASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-522|reaction.ecocyc.TRANS-RXN0-522]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03383`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
