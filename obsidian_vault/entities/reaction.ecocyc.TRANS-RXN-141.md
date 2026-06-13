---
entity_id: "reaction.ecocyc.TRANS-RXN-141"
entity_type: "reaction"
name: "TRANS-RXN-141"
source_database: "EcoCyc"
source_id: "TRANS-RXN-141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-141

`reaction.ecocyc.TRANS-RXN-141`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-141`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MG+2 -> MG+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MG+2 -> MG+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by corA (protein.P0ABI4). Substrates: Magnesium cation (molecule.C00305). Products: Magnesium cation (molecule.C00305).

## Annotation

MG+2 -> MG+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ABI4|protein.P0ABI4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-141`

## Notes

MG+2 -> MG+2; direction=LEFT-TO-RIGHT
