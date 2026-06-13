---
entity_id: "reaction.ecocyc.RXN-11840"
entity_type: "reaction"
name: "RXN-11840"
source_database: "EcoCyc"
source_id: "RXN-11840"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11840

`reaction.ecocyc.RXN-11840`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11840`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine65 -> tRNA-pseudouridine65; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine65 -> tRNA-pseudouridine65; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by truC (protein.P0AA41). Substrates: a uridine65 in tRNA (molecule.ecocyc.tRNA-uridine65). Products: a pseudouridine65 in tRNA (molecule.ecocyc.tRNA-pseudouridine65).

## Annotation

tRNA-uridine65 -> tRNA-pseudouridine65; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AA41|protein.P0AA41]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine65|molecule.ecocyc.tRNA-pseudouridine65]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine65|molecule.ecocyc.tRNA-uridine65]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11840`

## Notes

tRNA-uridine65 -> tRNA-pseudouridine65; direction=PHYSIOL-LEFT-TO-RIGHT
