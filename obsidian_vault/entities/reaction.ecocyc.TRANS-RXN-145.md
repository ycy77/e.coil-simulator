---
entity_id: "reaction.ecocyc.TRANS-RXN-145"
entity_type: "reaction"
name: "TRANS-RXN-145"
source_database: "EcoCyc"
source_id: "TRANS-RXN-145"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-145

`reaction.ecocyc.TRANS-RXN-145`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-145`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

WATER -> WATER; direction=REVERSIBLE EcoCyc reaction equation: WATER -> WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by water channel AqpZ (complex.ecocyc.CPLX0-7653). Substrates: H2O (molecule.C00001). Products: H2O (molecule.C00001).

## Annotation

WATER -> WATER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7653|complex.ecocyc.CPLX0-7653]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-145`

## Notes

WATER -> WATER; direction=REVERSIBLE
