---
entity_id: "reaction.ecocyc.RXN-14136"
entity_type: "reaction"
name: "RXN-14136"
source_database: "EcoCyc"
source_id: "RXN-14136"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14136

`reaction.ecocyc.RXN-14136`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14136`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2030 + WATER -> GLYCEROL-3P + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2030 + WATER -> GLYCEROL-3P + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ugpQ (protein.P10908). Substrates: H2O (molecule.C00001), glycerophosphoserine (molecule.ecocyc.CPD0-2030). Products: L-Serine (molecule.C00065), H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093).

## Annotation

CPD0-2030 + WATER -> GLYCEROL-3P + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P10908|protein.P10908]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2030|molecule.ecocyc.CPD0-2030]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14136`

## Notes

CPD0-2030 + WATER -> GLYCEROL-3P + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
