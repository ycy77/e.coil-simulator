---
entity_id: "reaction.ecocyc.RXN-3482"
entity_type: "reaction"
name: "RXN-3482"
source_database: "EcoCyc"
source_id: "RXN-3482"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-3482

`reaction.ecocyc.RXN-3482`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-3482`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + HYDROXYLAMINE -> CPD-3344 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + HYDROXYLAMINE -> CPD-3344 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Pyruvate (molecule.C00022), Hydroxylamine (molecule.C00192). Products: H2O (molecule.C00001), pyruvic oxime (molecule.ecocyc.CPD-3344).

## Annotation

PYRUVATE + HYDROXYLAMINE -> CPD-3344 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3344|molecule.ecocyc.CPD-3344]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-3482`

## Notes

PYRUVATE + HYDROXYLAMINE -> CPD-3344 + WATER; direction=LEFT-TO-RIGHT
