---
entity_id: "reaction.ecocyc.CARDIOLIPSYN-RXN"
entity_type: "reaction"
name: "CARDIOLIPSYN-RXN"
source_database: "EcoCyc"
source_id: "CARDIOLIPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CARDIOLIPSYN-RXN

`reaction.ecocyc.CARDIOLIPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CARDIOLIPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of phospholipid biosynthesis. EcoCyc reaction equation: L-1-PHOSPHATIDYL-GLYCEROL -> CARDIOLIPIN + GLYCEROL; direction=LEFT-TO-RIGHT. This reaction is part of phospholipid biosynthesis.

## Biological Role

Catalyzed by clsA (protein.P0A6H8), clsB (protein.P0AA84). Substrates: Phosphatidylglycerol (molecule.C00344). Products: Glycerol (molecule.C00116), Cardiolipin (molecule.C05980).

## Enriched Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)

## Annotation

This reaction is part of phospholipid biosynthesis.

## Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `activates` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01194|molecule.C01194]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C02737|molecule.C02737]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A6H8|protein.P0A6H8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AA84|protein.P0AA84]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1422|molecule.ecocyc.CPD0-1422]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1423|molecule.ecocyc.CPD0-1423]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1425|molecule.ecocyc.CPD0-1425]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CARDIOLIPSYN-RXN`

## Notes

L-1-PHOSPHATIDYL-GLYCEROL -> CARDIOLIPIN + GLYCEROL; direction=LEFT-TO-RIGHT
