---
entity_id: "reaction.ecocyc.RXN0-5395"
entity_type: "reaction"
name: "RXN0-5395"
source_database: "EcoCyc"
source_id: "RXN0-5395"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5395

`reaction.ecocyc.RXN0-5395`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5395`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-BETA-D-GLUCOSYLGLUCOSE + WATER -> Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-BETA-D-GLUCOSYLGLUCOSE + WATER -> Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ygjK (protein.P42592). Substrates: H2O (molecule.C00001), nigerose (molecule.ecocyc.3-BETA-D-GLUCOSYLGLUCOSE). Products: D-Glucose (molecule.C00031).

## Annotation

3-BETA-D-GLUCOSYLGLUCOSE + WATER -> Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P42592|protein.P42592]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.3-BETA-D-GLUCOSYLGLUCOSE|molecule.ecocyc.3-BETA-D-GLUCOSYLGLUCOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5395`

## Notes

3-BETA-D-GLUCOSYLGLUCOSE + WATER -> Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
