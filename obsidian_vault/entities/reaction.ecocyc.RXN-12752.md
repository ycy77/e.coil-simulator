---
entity_id: "reaction.ecocyc.RXN-12752"
entity_type: "reaction"
name: "RXN-12752"
source_database: "EcoCyc"
source_id: "RXN-12752"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12752

`reaction.ecocyc.RXN-12752`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12752`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2472 -> CPD-653; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2472 -> CPD-653; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: (R)-NADHX (molecule.ecocyc.CPD0-2472). Products: (S)-NADHX (molecule.ecocyc.CPD-653).

## Annotation

CPD0-2472 -> CPD-653; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-653|molecule.ecocyc.CPD-653]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2472|molecule.ecocyc.CPD0-2472]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12752`

## Notes

CPD0-2472 -> CPD-653; direction=PHYSIOL-LEFT-TO-RIGHT
