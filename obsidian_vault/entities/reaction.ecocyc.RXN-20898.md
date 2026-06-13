---
entity_id: "reaction.ecocyc.RXN-20898"
entity_type: "reaction"
name: "RXN-20898"
source_database: "EcoCyc"
source_id: "RXN-20898"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20898

`reaction.ecocyc.RXN-20898`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20898`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15374 + LYS -> FRUCTOSELYSINE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15374 + LYS -> FRUCTOSELYSINE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Lysine (molecule.C00047), aldehydo-D-glucose (molecule.ecocyc.CPD-15374). Products: H2O (molecule.C00001), Fructoselysine (molecule.C16488).

## Annotation

CPD-15374 + LYS -> FRUCTOSELYSINE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16488|molecule.C16488]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15374|molecule.ecocyc.CPD-15374]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20898`

## Notes

CPD-15374 + LYS -> FRUCTOSELYSINE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
