---
entity_id: "reaction.ecocyc.RXN0-312"
entity_type: "reaction"
name: "RXN0-312"
source_database: "EcoCyc"
source_id: "RXN0-312"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-312

`reaction.ecocyc.RXN0-312`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-312`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-ARCB717 + WATER -> ARCB-CPLX + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-ARCB717 + WATER -> ARCB-CPLX + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sixA (protein.P76502). Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

PHOSPHO-ARCB717 + WATER -> ARCB-CPLX + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76502|protein.P76502]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-312`

## Notes

PHOSPHO-ARCB717 + WATER -> ARCB-CPLX + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
