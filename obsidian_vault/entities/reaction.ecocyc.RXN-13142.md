---
entity_id: "reaction.ecocyc.RXN-13142"
entity_type: "reaction"
name: "RXN-13142"
source_database: "EcoCyc"
source_id: "RXN-13142"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13142

`reaction.ecocyc.RXN-13142`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13142`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14133 -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14133 -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nnr (protein.P31806). Substrates: (R)-NADPHX (molecule.ecocyc.CPD-14133). Products: (S)-NADPHX (molecule.ecocyc.CPD0-2474).

## Annotation

CPD-14133 -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P31806|protein.P31806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2474|molecule.ecocyc.CPD0-2474]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14133|molecule.ecocyc.CPD-14133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13142`

## Notes

CPD-14133 -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT
