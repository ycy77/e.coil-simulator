---
entity_id: "molecule.C03785"
entity_type: "small_molecule"
name: "D-Tagatose 1,6-bisphosphate"
source_database: "KEGG"
source_id: "C03785"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Tagatose 1,6-bisphosphate"
---

# D-Tagatose 1,6-bisphosphate

`molecule.C03785`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03785`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Tagatose 1,6-bisphosphate EcoCyc common name: D-tagatofuranose 1,6-bisphosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)

## Annotation

KEGG compound: D-Tagatose 1,6-bisphosphate

## Pathways

- `eco00052` Galactose metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TAGAKIN-RXN|reaction.ecocyc.TAGAKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03785`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
