---
entity_id: "reaction.ecocyc.TRANS-RXN0-495"
entity_type: "reaction"
name: "TRANS-RXN0-495"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-495"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-495

`reaction.ecocyc.TRANS-RXN0-495`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-495`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-SERINE -> D-SERINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-SERINE -> D-SERINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dsdX (protein.P08555). Substrates: D-Serine (molecule.C00740). Products: D-Serine (molecule.C00740).

## Annotation

D-SERINE -> D-SERINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P08555|protein.P08555]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-495`

## Notes

D-SERINE -> D-SERINE; direction=LEFT-TO-RIGHT
