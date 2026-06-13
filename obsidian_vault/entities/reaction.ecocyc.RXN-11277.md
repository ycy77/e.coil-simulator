---
entity_id: "reaction.ecocyc.RXN-11277"
entity_type: "reaction"
name: "RXN-11277"
source_database: "EcoCyc"
source_id: "RXN-11277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11277

`reaction.ecocyc.RXN-11277`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11277`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

DIACYLGLYCEROL-PYROPHOSPHATE + WATER -> L-PHOSPHATIDATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIACYLGLYCEROL-PYROPHOSPHATE + WATER -> L-PHOSPHATIDATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pgpB (protein.P0A924). Substrates: H2O (molecule.C00001), a 1,2-diacyl-sn-glycerol 3-diphosphate (molecule.ecocyc.DIACYLGLYCEROL-PYROPHOSPHATE). Products: H+ (molecule.C00080), Phosphatidate (molecule.C00416), phosphate (molecule.ecocyc.Pi).

## Annotation

DIACYLGLYCEROL-PYROPHOSPHATE + WATER -> L-PHOSPHATIDATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A924|protein.P0A924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DIACYLGLYCEROL-PYROPHOSPHATE|molecule.ecocyc.DIACYLGLYCEROL-PYROPHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-11277`

## Notes

DIACYLGLYCEROL-PYROPHOSPHATE + WATER -> L-PHOSPHATIDATE + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
