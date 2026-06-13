---
entity_id: "reaction.ecocyc.RXN-20900"
entity_type: "reaction"
name: "RXN-20900"
source_database: "EcoCyc"
source_id: "RXN-20900"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20900

`reaction.ecocyc.RXN-20900`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20900`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15382 + LYS -> CPD-21707 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15382 + LYS -> CPD-21707 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Lysine (molecule.C00047), keto-D-fructose (molecule.ecocyc.CPD-15382). Products: H2O (molecule.C00001), Glucoselysine (molecule.C20978).

## Annotation

CPD-15382 + LYS -> CPD-21707 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20978|molecule.C20978]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15382|molecule.ecocyc.CPD-15382]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20900`

## Notes

CPD-15382 + LYS -> CPD-21707 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
