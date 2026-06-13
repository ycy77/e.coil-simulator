---
entity_id: "reaction.ecocyc.RXN0-385"
entity_type: "reaction"
name: "RXN0-385"
source_database: "EcoCyc"
source_id: "RXN0-385"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-385

`reaction.ecocyc.RXN0-385`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-385`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DGTP + WATER -> PROTON + DGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DGTP + WATER -> PROTON + DGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), dGTP (molecule.C00286). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), dGMP (molecule.C00362).

## Annotation

DGTP + WATER -> PROTON + DGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00362|molecule.C00362]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-385`

## Notes

DGTP + WATER -> PROTON + DGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
