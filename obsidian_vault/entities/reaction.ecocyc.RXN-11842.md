---
entity_id: "reaction.ecocyc.RXN-11842"
entity_type: "reaction"
name: "RXN-11842"
source_database: "EcoCyc"
source_id: "RXN-11842"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11842

`reaction.ecocyc.RXN-11842`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11842`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Uridine32-in-tRNA -> tRNA-pseudouridine32; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Uridine32-in-tRNA -> tRNA-pseudouridine32; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rluA (protein.P0AA37). Substrates: a uridine32 in tRNA (molecule.ecocyc.Uridine32-in-tRNA). Products: a pseudouridine32 in tRNA (molecule.ecocyc.tRNA-pseudouridine32).

## Annotation

Uridine32-in-tRNA -> tRNA-pseudouridine32; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AA37|protein.P0AA37]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine32|molecule.ecocyc.tRNA-pseudouridine32]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Uridine32-in-tRNA|molecule.ecocyc.Uridine32-in-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11842`

## Notes

Uridine32-in-tRNA -> tRNA-pseudouridine32; direction=PHYSIOL-LEFT-TO-RIGHT
