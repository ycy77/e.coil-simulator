---
entity_id: "reaction.ecocyc.RXN-14552"
entity_type: "reaction"
name: "RXN-14552"
source_database: "EcoCyc"
source_id: "RXN-14552"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14552

`reaction.ecocyc.RXN-14552`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14552`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBAMOYL-P + ATP + WATER -> PPI + CPD-15424 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CARBAMOYL-P + ATP + WATER -> PPI + CPD-15424 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Carbamoyl phosphate (molecule.C00169). Products: Diphosphate (molecule.C00013), (O-carbamoyl)adenylate (molecule.ecocyc.CPD-15424), phosphate (molecule.ecocyc.Pi).

## Annotation

CARBAMOYL-P + ATP + WATER -> PPI + CPD-15424 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15424|molecule.ecocyc.CPD-15424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14552`

## Notes

CARBAMOYL-P + ATP + WATER -> PPI + CPD-15424 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
