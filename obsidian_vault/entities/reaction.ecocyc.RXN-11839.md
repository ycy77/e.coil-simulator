---
entity_id: "reaction.ecocyc.RXN-11839"
entity_type: "reaction"
name: "RXN-11839"
source_database: "EcoCyc"
source_id: "RXN-11839"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11839

`reaction.ecocyc.RXN-11839`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11839`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine55 -> tRNA-pseudouridine55; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine55 -> tRNA-pseudouridine55; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by truB (protein.P60340). Substrates: a uridine55 in tRNA (molecule.ecocyc.tRNA-uridine55). Products: a pseudouridine55 in tRNA (molecule.ecocyc.tRNA-pseudouridine55).

## Annotation

tRNA-uridine55 -> tRNA-pseudouridine55; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P60340|protein.P60340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine55|molecule.ecocyc.tRNA-pseudouridine55]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine55|molecule.ecocyc.tRNA-uridine55]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11839`

## Notes

tRNA-uridine55 -> tRNA-pseudouridine55; direction=PHYSIOL-LEFT-TO-RIGHT
