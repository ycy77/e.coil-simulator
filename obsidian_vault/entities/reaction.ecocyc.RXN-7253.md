---
entity_id: "reaction.ecocyc.RXN-7253"
entity_type: "reaction"
name: "RXN-7253"
source_database: "EcoCyc"
source_id: "RXN-7253"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7253

`reaction.ecocyc.RXN-7253`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7253`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-6746 + WATER -> MYO-INOSITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-6746 + WATER -> MYO-INOSITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by suhB (protein.P0ADG4). Substrates: H2O (molecule.C00001), 1D-myo-inositol 2-phosphate (molecule.ecocyc.CPD-6746). Products: myo-Inositol (molecule.C00137), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-6746 + WATER -> MYO-INOSITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ADG4|protein.P0ADG4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00137|molecule.C00137]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-6746|molecule.ecocyc.CPD-6746]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7253`

## Notes

CPD-6746 + WATER -> MYO-INOSITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
