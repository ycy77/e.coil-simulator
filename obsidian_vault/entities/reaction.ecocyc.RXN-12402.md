---
entity_id: "reaction.ecocyc.RXN-12402"
entity_type: "reaction"
name: "RXN-12402"
source_database: "EcoCyc"
source_id: "RXN-12402"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12402

`reaction.ecocyc.RXN-12402`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12402`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1202 + WATER -> Glucopyranose + CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1202 + WATER -> Glucopyranose + CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by α-D-xyloside xylohydrolase (complex.ecocyc.CPLX0-3901). Substrates: H2O (molecule.C00001), isoprimeverose (molecule.ecocyc.CPD0-1202). Products: D-Glucose (molecule.C00031), α-D-xylopyranose (molecule.ecocyc.CPD-25028).

## Annotation

CPD0-1202 + WATER -> Glucopyranose + CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3901|complex.ecocyc.CPLX0-3901]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-25028|molecule.ecocyc.CPD-25028]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1202|molecule.ecocyc.CPD0-1202]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12402`

## Notes

CPD0-1202 + WATER -> Glucopyranose + CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT
