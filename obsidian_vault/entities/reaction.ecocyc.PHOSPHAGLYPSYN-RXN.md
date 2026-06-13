---
entity_id: "reaction.ecocyc.PHOSPHAGLYPSYN-RXN"
entity_type: "reaction"
name: "PHOSPHAGLYPSYN-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHAGLYPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHAGLYPSYN-RXN

`reaction.ecocyc.PHOSPHAGLYPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHAGLYPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is at a branch point and is the committed step in the biosynthesis of the acidic phospholipids. EcoCyc reaction equation: CDPDIACYLGLYCEROL + GLYCEROL-3P -> CMP + L-1-PHOSPHATIDYL-GLYCEROL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is at a branch point and is the committed step in the biosynthesis of the acidic phospholipids.

## Biological Role

Catalyzed by pgsA (protein.P0ABF8). Substrates: sn-Glycerol 3-phosphate (molecule.C00093), CDP-diacylglycerol (molecule.C00269). Products: CMP (molecule.C00055), H+ (molecule.C00080), Phosphatidylglycerophosphate (molecule.C03892).

## Enriched Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Annotation

This reaction is at a branch point and is the committed step in the biosynthesis of the acidic phospholipids.

## Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0ABF8|protein.P0ABF8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03892|molecule.C03892]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSPHAGLYPSYN-RXN`

## Notes

CDPDIACYLGLYCEROL + GLYCEROL-3P -> CMP + L-1-PHOSPHATIDYL-GLYCEROL-P + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
