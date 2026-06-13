---
entity_id: "reaction.ecocyc.RXN-23715"
entity_type: "reaction"
name: "RXN-23715"
source_database: "EcoCyc"
source_id: "RXN-23715"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23715

`reaction.ecocyc.RXN-23715`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23715`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-660 + NAD -> OXALACETIC_ACID + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-660 + NAD -> OXALACETIC_ACID + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), (R)-Malate (molecule.C00497). Products: NADH (molecule.C00004), Oxaloacetate (molecule.C00036), H+ (molecule.C00080).

## Annotation

CPD-660 + NAD -> OXALACETIC_ACID + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23715`

## Notes

CPD-660 + NAD -> OXALACETIC_ACID + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
