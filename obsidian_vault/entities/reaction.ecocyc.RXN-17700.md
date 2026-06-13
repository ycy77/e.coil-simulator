---
entity_id: "reaction.ecocyc.RXN-17700"
entity_type: "reaction"
name: "RXN-17700"
source_database: "EcoCyc"
source_id: "RXN-17700"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17700

`reaction.ecocyc.RXN-17700`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17700`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SULFOQUINOVOSYLDIACYLGLYCEROL + WATER -> CPD-21685 + 1-2-Diglycerides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SULFOQUINOVOSYLDIACYLGLYCEROL + WATER -> CPD-21685 + 1-2-Diglycerides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yihQ (protein.P32138). Substrates: H2O (molecule.C00001), Sulfoquinovosyldiacylglycerol (molecule.C13508). Products: a 1,2-diglyceride (molecule.ecocyc.1-2-Diglycerides), 6-sulfo-α-D-quinovose (molecule.ecocyc.CPD-21685).

## Enriched Pathways

- `ecocyc.PWY-8351` sulfoquinovosyl diacylglycerides and sulfoquinovosyl glycerol degradation (EcoCyc)

## Annotation

SULFOQUINOVOSYLDIACYLGLYCEROL + WATER -> CPD-21685 + 1-2-Diglycerides; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8351` sulfoquinovosyl diacylglycerides and sulfoquinovosyl glycerol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P32138|protein.P32138]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.1-2-Diglycerides|molecule.ecocyc.1-2-Diglycerides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21685|molecule.ecocyc.CPD-21685]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C13508|molecule.C13508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17700`

## Notes

SULFOQUINOVOSYLDIACYLGLYCEROL + WATER -> CPD-21685 + 1-2-Diglycerides; direction=PHYSIOL-LEFT-TO-RIGHT
