---
entity_id: "reaction.ecocyc.RXN-24143"
entity_type: "reaction"
name: "RXN-24143"
source_database: "EcoCyc"
source_id: "RXN-24143"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24143

`reaction.ecocyc.RXN-24143`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24143`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-26685 + WATER -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-26685 + WATER -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), adenylyl MoO2(OH)-molybdopterin cofactor (molecule.ecocyc.CPD-26685). Products: AMP (molecule.C00020), H+ (molecule.C00080), Molybdoenzyme molybdenum cofactor (molecule.C18237).

## Annotation

CPD-26685 + WATER -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26685|molecule.ecocyc.CPD-26685]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24143`

## Notes

CPD-26685 + WATER -> CPD-15870 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
