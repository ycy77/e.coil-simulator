---
entity_id: "reaction.ecocyc.TRANS-RXN-496"
entity_type: "reaction"
name: "TRANS-RXN-496"
source_database: "EcoCyc"
source_id: "TRANS-RXN-496"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-496

`reaction.ecocyc.TRANS-RXN-496`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-496`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

S2O3 -> S2O3; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S2O3 -> S2O3; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tsuA (protein.P33015). Substrates: Thiosulfate (molecule.C00320). Products: Thiosulfate (molecule.C00320).

## Annotation

S2O3 -> S2O3; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P33015|protein.P33015]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-496`

## Notes

S2O3 -> S2O3; direction=LEFT-TO-RIGHT
