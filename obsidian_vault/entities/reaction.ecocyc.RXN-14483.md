---
entity_id: "reaction.ecocyc.RXN-14483"
entity_type: "reaction"
name: "RXN-14483"
source_database: "EcoCyc"
source_id: "RXN-14483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14483

`reaction.ecocyc.RXN-14483`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14483`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hexose-phosphates + WATER -> Hexoses + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hexose-phosphates + WATER -> Hexoses + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a hexose phosphate (molecule.ecocyc.Hexose-phosphates). Products: a hexose (molecule.ecocyc.Hexoses), phosphate (molecule.ecocyc.Pi).

## Annotation

Hexose-phosphates + WATER -> Hexoses + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Hexoses|molecule.ecocyc.Hexoses]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hexose-phosphates|molecule.ecocyc.Hexose-phosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14483`

## Notes

Hexose-phosphates + WATER -> Hexoses + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
