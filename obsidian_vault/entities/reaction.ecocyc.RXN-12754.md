---
entity_id: "reaction.ecocyc.RXN-12754"
entity_type: "reaction"
name: "RXN-12754"
source_database: "EcoCyc"
source_id: "RXN-12754"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12754

`reaction.ecocyc.RXN-12754`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12754`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADH + WATER -> CPD0-2472; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NADH + WATER -> CPD0-2472; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), NADH (molecule.C00004). Products: (R)-NADHX (molecule.ecocyc.CPD0-2472).

## Annotation

NADH + WATER -> CPD0-2472; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-2472|molecule.ecocyc.CPD0-2472]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12754`

## Notes

NADH + WATER -> CPD0-2472; direction=LEFT-TO-RIGHT
