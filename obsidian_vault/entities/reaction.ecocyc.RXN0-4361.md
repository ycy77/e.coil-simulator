---
entity_id: "reaction.ecocyc.RXN0-4361"
entity_type: "reaction"
name: "RXN0-4361"
source_database: "EcoCyc"
source_id: "RXN0-4361"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4361

`reaction.ecocyc.RXN0-4361`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4361`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-BETA-D-HEPTOSE-17-DIPHOSPHATE + WATER -> D-BETA-D-HEPTOSE-1-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-BETA-D-HEPTOSE-17-DIPHOSPHATE + WATER -> D-BETA-D-HEPTOSE-1-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by gmhB (protein.P63228). Substrates: H2O (molecule.C00001), D-glycero-beta-D-manno-Heptose 1,7-bisphosphate (molecule.C11472). Products: D-glycero-beta-D-manno-Heptose 1-phosphate (molecule.C07838), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Annotation

D-BETA-D-HEPTOSE-17-DIPHOSPHATE + WATER -> D-BETA-D-HEPTOSE-1-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1241` ADP-L-glycero-β-D-manno-heptose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P63228|protein.P63228]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C07838|molecule.C07838]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11472|molecule.C11472]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01100|molecule.C01100]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4361`

## Notes

D-BETA-D-HEPTOSE-17-DIPHOSPHATE + WATER -> D-BETA-D-HEPTOSE-1-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
