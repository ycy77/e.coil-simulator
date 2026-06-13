---
entity_id: "molecule.C03492"
entity_type: "small_molecule"
name: "D-4'-Phosphopantothenate"
source_database: "KEGG"
source_id: "C03492"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-4'-Phosphopantothenate"
  - "(R)-4'-Phosphopantothenate"
---

# D-4'-Phosphopantothenate

`molecule.C03492`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03492`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-4'-Phosphopantothenate; (R)-4'-Phosphopantothenate EcoCyc common name: (R)-4'-phosphopantothenate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: D-4'-Phosphopantothenate; (R)-4'-Phosphopantothenate

## Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.PANTOTHENATE-KIN-RXN|reaction.ecocyc.PANTOTHENATE-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22914|reaction.ecocyc.RXN-22914]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03492`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
