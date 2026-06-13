---
entity_id: "reaction.ecocyc.RXN-11776"
entity_type: "reaction"
name: "RXN-11776"
source_database: "EcoCyc"
source_id: "RXN-11776"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11776

`reaction.ecocyc.RXN-11776`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11776`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FARNESYL-PP + WATER -> PROTON + CPD-12587 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FARNESYL-PP + WATER -> PROTON + CPD-12587 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by uppP (protein.P60932). Substrates: H2O (molecule.C00001), trans,trans-Farnesyl diphosphate (molecule.C00448). Products: H+ (molecule.C00080), trans,trans-Farnesyl phosphate (molecule.C20121), phosphate (molecule.ecocyc.Pi).

## Annotation

FARNESYL-PP + WATER -> PROTON + CPD-12587 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P60932|protein.P60932]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20121|molecule.C20121]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00448|molecule.C00448]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11776`

## Notes

FARNESYL-PP + WATER -> PROTON + CPD-12587 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
