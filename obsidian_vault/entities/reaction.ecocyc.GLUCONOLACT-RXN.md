---
entity_id: "reaction.ecocyc.GLUCONOLACT-RXN"
entity_type: "reaction"
name: "GLUCONOLACT-RXN"
source_database: "EcoCyc"
source_id: "GLUCONOLACT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCONOLACT-RXN

`reaction.ecocyc.GLUCONOLACT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCONOLACT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction continues the breakdown of glucose, yielding gluconate, from which E. coli can produce pentose. EcoCyc reaction equation: GLC-D-LACTONE + WATER -> PROTON + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction continues the breakdown of glucose, yielding gluconate, from which E. coli can produce pentose.

## Biological Role

Catalyzed by GLUCONOLACT-MONOMER (protein.ecocyc.GLUCONOLACT-MONOMER). Substrates: H2O (molecule.C00001), D-Glucono-1,5-lactone (molecule.C00198). Products: H+ (molecule.C00080), D-Gluconic acid (molecule.C00257).

## Enriched Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Annotation

This reaction continues the breakdown of glucose, yielding gluconate, from which E. coli can produce pentose.

## Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.GLUCONOLACT-MONOMER|protein.ecocyc.GLUCONOLACT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00198|molecule.C00198]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUCONOLACT-RXN`

## Notes

GLC-D-LACTONE + WATER -> PROTON + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT
