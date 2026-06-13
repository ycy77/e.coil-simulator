---
entity_id: "reaction.ecocyc.RXN-15139"
entity_type: "reaction"
name: "RXN-15139"
source_database: "EcoCyc"
source_id: "RXN-15139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15139

`reaction.ecocyc.RXN-15139`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENINE + CPD-12377 -> CPD0-2461 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADENINE + CPD-12377 -> CPD0-2461 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Adenine (molecule.C00147), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), isoguanine (molecule.ecocyc.CPD0-2461).

## Annotation

ADENINE + CPD-12377 -> CPD0-2461 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2461|molecule.ecocyc.CPD0-2461]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15139`

## Notes

ADENINE + CPD-12377 -> CPD0-2461 + WATER; direction=LEFT-TO-RIGHT
