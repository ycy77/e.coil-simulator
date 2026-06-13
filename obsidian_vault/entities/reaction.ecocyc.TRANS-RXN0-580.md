---
entity_id: "reaction.ecocyc.TRANS-RXN0-580"
entity_type: "reaction"
name: "TRANS-RXN0-580"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-580"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-580

`reaction.ecocyc.TRANS-RXN0-580`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-580`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-10247 -> CPD-10247; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10247 -> CPD-10247; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yihO (protein.P32136). Substrates: 6-sulfo-D-quinovose (molecule.ecocyc.CPD-10247). Products: 6-sulfo-D-quinovose (molecule.ecocyc.CPD-10247).

## Annotation

CPD-10247 -> CPD-10247; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P32136|protein.P32136]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-10247|molecule.ecocyc.CPD-10247]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10247|molecule.ecocyc.CPD-10247]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-580`

## Notes

CPD-10247 -> CPD-10247; direction=LEFT-TO-RIGHT
