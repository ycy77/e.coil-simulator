---
entity_id: "reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN"
entity_type: "reaction"
name: "2-DEHYDROPANTOATE-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "2-DEHYDROPANTOATE-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-DEHYDROPANTOATE-REDUCT-RXN

`reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-DEHYDROPANTOATE-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in pantothenate biosynthesis. EcoCyc reaction equation: L-PANTOATE + NADP -> PROTON + 2-DEHYDROPANTOATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT. This is the second reaction in pantothenate biosynthesis.

## Biological Role

Catalyzed by ketol-acid reductoisomerase (NADP+) (complex.ecocyc.CPLX0-7643), panE (protein.P0A9J4). Substrates: NADP+ (molecule.C00006), (R)-Pantoate (molecule.C00522). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 2-Dehydropantoate (molecule.C00966).

## Enriched Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Annotation

This is the second reaction in pantothenate biosynthesis.

## Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7643|complex.ecocyc.CPLX0-7643]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A9J4|protein.P0A9J4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00966|molecule.C00966]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00522|molecule.C00522]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00522|molecule.C00522]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2-DEHYDROPANTOATE-REDUCT-RXN`

## Notes

L-PANTOATE + NADP -> PROTON + 2-DEHYDROPANTOATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
