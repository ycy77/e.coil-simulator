---
entity_id: "reaction.ecocyc.RXN-11841"
entity_type: "reaction"
name: "RXN-11841"
source_database: "EcoCyc"
source_id: "RXN-11841"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11841

`reaction.ecocyc.RXN-11841`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11841`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-uridine13 -> tRNA-pseudouridine13; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tRNA-uridine13 -> tRNA-pseudouridine13; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by truD (protein.Q57261). Substrates: a uridine13 in tRNA (molecule.ecocyc.tRNA-uridine13). Products: a pseudouridine13 in tRNA (molecule.ecocyc.tRNA-pseudouridine13).

## Annotation

tRNA-uridine13 -> tRNA-pseudouridine13; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.Q57261|protein.Q57261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.tRNA-pseudouridine13|molecule.ecocyc.tRNA-pseudouridine13]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine13|molecule.ecocyc.tRNA-uridine13]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11841`

## Notes

tRNA-uridine13 -> tRNA-pseudouridine13; direction=PHYSIOL-LEFT-TO-RIGHT
