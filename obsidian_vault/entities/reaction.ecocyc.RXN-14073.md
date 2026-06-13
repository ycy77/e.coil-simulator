---
entity_id: "reaction.ecocyc.RXN-14073"
entity_type: "reaction"
name: "RXN-14073"
source_database: "EcoCyc"
source_id: "RXN-14073"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14073

`reaction.ecocyc.RXN-14073`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14073`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCEROPHOSPHOGLYCEROL + WATER -> GLYCEROL + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLYCEROPHOSPHOGLYCEROL + WATER -> GLYCEROL + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ugpQ (protein.P10908). Substrates: H2O (molecule.C00001), glycerophosphoglycerol (molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL). Products: H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093), Glycerol (molecule.C00116).

## Annotation

GLYCEROPHOSPHOGLYCEROL + WATER -> GLYCEROL + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P10908|protein.P10908]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL|molecule.ecocyc.GLYCEROPHOSPHOGLYCEROL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14073`

## Notes

GLYCEROPHOSPHOGLYCEROL + WATER -> GLYCEROL + GLYCEROL-3P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
