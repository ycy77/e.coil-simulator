---
entity_id: "reaction.ecocyc.RXN-15312"
entity_type: "reaction"
name: "RXN-15312"
source_database: "EcoCyc"
source_id: "RXN-15312"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15312

`reaction.ecocyc.RXN-15312`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15312`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALPHA-GLC-6-P + WATER -> ALPHA-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ALPHA-GLC-6-P + WATER -> ALPHA-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), alpha-D-Glucose 6-phosphate (molecule.C00668). Products: alpha-D-Glucose (molecule.C00267), phosphate (molecule.ecocyc.Pi).

## Annotation

ALPHA-GLC-6-P + WATER -> ALPHA-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00668|molecule.C00668]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15312`

## Notes

ALPHA-GLC-6-P + WATER -> ALPHA-GLUCOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
