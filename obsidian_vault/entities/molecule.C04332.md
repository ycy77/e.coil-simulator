---
entity_id: "molecule.C04332"
entity_type: "small_molecule"
name: "6,7-Dimethyl-8-(D-ribityl)lumazine"
source_database: "KEGG"
source_id: "C04332"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "6,7-Dimethyl-8-(D-ribityl)lumazine"
---

# 6,7-Dimethyl-8-(D-ribityl)lumazine

`molecule.C04332`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04332`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 6,7-Dimethyl-8-(D-ribityl)lumazine EcoCyc common name: 6,7-dimethyl-8-(1-D-ribityl)lumazine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: 6,7-Dimethyl-8-(D-ribityl)lumazine

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.LUMAZINESYN-RXN|reaction.ecocyc.LUMAZINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00066|reaction.R00066]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732
- `is_substrate_of` --> [[reaction.ecocyc.RIBOFLAVIN-SYN-RXN|reaction.ecocyc.RIBOFLAVIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04332`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
