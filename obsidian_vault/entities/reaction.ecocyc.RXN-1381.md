---
entity_id: "reaction.ecocyc.RXN-1381"
entity_type: "reaction"
name: "RXN-1381"
source_database: "EcoCyc"
source_id: "RXN-1381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-1381

`reaction.ecocyc.RXN-1381`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-1381`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACYL-COA + GLYCEROL-3P -> ACYL-SN-GLYCEROL-3P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACYL-COA + GLYCEROL-3P -> ACYL-SN-GLYCEROL-3P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: Acyl-CoA (molecule.C00040), sn-Glycerol 3-phosphate (molecule.C00093). Products: CoA (molecule.C00010), 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681).

## Enriched Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)

## Annotation

ACYL-COA + GLYCEROL-3P -> ACYL-SN-GLYCEROL-3P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5667` CDP-diacylglycerol biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00681|molecule.C00681]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1457|molecule.ecocyc.CPD0-1457]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1458|molecule.ecocyc.CPD0-1458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2032|molecule.ecocyc.CPD0-2032]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2099|molecule.ecocyc.CPD0-2099]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLGLYOXAL|molecule.ecocyc.PHENYLGLYOXAL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P0A6A8|protein.P0A6A8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-1381`

## Notes

ACYL-COA + GLYCEROL-3P -> ACYL-SN-GLYCEROL-3P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
