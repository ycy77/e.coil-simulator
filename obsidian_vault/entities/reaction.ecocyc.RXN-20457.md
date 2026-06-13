---
entity_id: "reaction.ecocyc.RXN-20457"
entity_type: "reaction"
name: "RXN-20457"
source_database: "EcoCyc"
source_id: "RXN-20457"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20457

`reaction.ecocyc.RXN-20457`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20457`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADPH + WATER -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NADPH + WATER -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), NADPH (molecule.C00005). Products: (S)-NADPHX (molecule.ecocyc.CPD0-2474).

## Annotation

NADPH + WATER -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-2474|molecule.ecocyc.CPD0-2474]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20457`

## Notes

NADPH + WATER -> CPD0-2474; direction=PHYSIOL-LEFT-TO-RIGHT
