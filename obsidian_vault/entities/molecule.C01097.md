---
entity_id: "molecule.C01097"
entity_type: "small_molecule"
name: "D-Tagatose 6-phosphate"
source_database: "KEGG"
source_id: "C01097"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Tagatose 6-phosphate"
---

# D-Tagatose 6-phosphate

`molecule.C01097`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01097`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Tagatose 6-phosphate EcoCyc common name: D-tagatofuranose 6-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)

## Annotation

KEGG compound: D-Tagatose 6-phosphate

## Pathways

- `eco00052` Galactose metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-13548|reaction.ecocyc.RXN-13548]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16992|reaction.ecocyc.RXN-16992]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TAGAKIN-RXN|reaction.ecocyc.TAGAKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01097`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
