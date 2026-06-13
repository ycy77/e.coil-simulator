---
entity_id: "reaction.ecocyc.RXN-22606"
entity_type: "reaction"
name: "RXN-22606"
source_database: "EcoCyc"
source_id: "RXN-22606"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22606

`reaction.ecocyc.RXN-22606`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22606`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS + FUM -> CPD8J2-27; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS + FUM -> CPD8J2-27; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Cysteine (molecule.C00097), Fumarate (molecule.C00122). Products: S-(2-succinyl)-L-cysteine (molecule.ecocyc.CPD8J2-27).

## Annotation

CYS + FUM -> CPD8J2-27; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD8J2-27|molecule.ecocyc.CPD8J2-27]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22606`

## Notes

CYS + FUM -> CPD8J2-27; direction=PHYSIOL-LEFT-TO-RIGHT
