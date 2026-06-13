---
entity_id: "reaction.ecocyc.RXN-17701"
entity_type: "reaction"
name: "RXN-17701"
source_database: "EcoCyc"
source_id: "RXN-17701"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17701

`reaction.ecocyc.RXN-17701`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17701`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19111 + WATER -> CPD-21685 + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19111 + WATER -> CPD-21685 + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yihQ (protein.P32138). Substrates: H2O (molecule.C00001), 3-(6-sulfo-α-D-quinovosyl)-sn-glycerol (molecule.ecocyc.CPD-19111). Products: Glycerol (molecule.C00116), 6-sulfo-α-D-quinovose (molecule.ecocyc.CPD-21685).

## Enriched Pathways

- `ecocyc.PWY-8351` sulfoquinovosyl diacylglycerides and sulfoquinovosyl glycerol degradation (EcoCyc)

## Annotation

CPD-19111 + WATER -> CPD-21685 + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8351` sulfoquinovosyl diacylglycerides and sulfoquinovosyl glycerol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P32138|protein.P32138]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21685|molecule.ecocyc.CPD-21685]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19111|molecule.ecocyc.CPD-19111]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17701`

## Notes

CPD-19111 + WATER -> CPD-21685 + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT
