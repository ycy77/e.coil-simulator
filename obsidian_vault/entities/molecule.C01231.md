---
entity_id: "molecule.C01231"
entity_type: "small_molecule"
name: "alpha-D-Glucose 1,6-bisphosphate"
source_database: "KEGG"
source_id: "C01231"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-D-Glucose 1,6-bisphosphate"
  - "alpha-D-Glucose 1,6-biphosphate"
  - "D-Glucose 1,6-bisphosphate"
---

# alpha-D-Glucose 1,6-bisphosphate

`molecule.C01231`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01231`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-D-Glucose 1,6-bisphosphate; alpha-D-Glucose 1,6-biphosphate; D-Glucose 1,6-bisphosphate EcoCyc common name: α-D-glucose 1,6-bisphosphate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

KEGG compound: alpha-D-Glucose 1,6-bisphosphate; alpha-D-Glucose 1,6-biphosphate; D-Glucose 1,6-bisphosphate

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-16997|reaction.ecocyc.RXN-16997]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16998|reaction.ecocyc.RXN-16998]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PHOSPHOGLUCMUT-RXN|reaction.ecocyc.PHOSPHOGLUCMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01231`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
