---
entity_id: "reaction.ecocyc.RXN-23584"
entity_type: "reaction"
name: "RXN-23584"
source_database: "EcoCyc"
source_id: "RXN-23584"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23584

`reaction.ecocyc.RXN-23584`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23584`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15554 + WATER -> HOMO-SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15554 + WATER -> HOMO-SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), L-homoserine lactone (molecule.ecocyc.CPD-15554). Products: H+ (molecule.C00080), L-Homoserine (molecule.C00263).

## Annotation

CPD-15554 + WATER -> HOMO-SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23584`

## Notes

CPD-15554 + WATER -> HOMO-SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
