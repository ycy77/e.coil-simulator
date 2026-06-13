---
entity_id: "reaction.ecocyc.RXN-14290"
entity_type: "reaction"
name: "RXN-14290"
source_database: "EcoCyc"
source_id: "RXN-14290"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14290

`reaction.ecocyc.RXN-14290`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14290`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DATP + CPD-12377 -> CPD-13851 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DATP + CPD-12377 -> CPD-13851 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: dATP (molecule.C00131), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), 2-hydroxy-dATP (molecule.ecocyc.CPD-13851).

## Annotation

DATP + CPD-12377 -> CPD-13851 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13851|molecule.ecocyc.CPD-13851]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14290`

## Notes

DATP + CPD-12377 -> CPD-13851 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
