---
entity_id: "reaction.ecocyc.TRANS-RXN0-574"
entity_type: "reaction"
name: "TRANS-RXN0-574"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-574"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-574

`reaction.ecocyc.TRANS-RXN0-574`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-574`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Glucopyranose -> Glucopyranose; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Glucopyranose -> Glucopyranose; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by malX (protein.P19642). Substrates: D-Glucose (molecule.C00031). Products: D-Glucose (molecule.C00031).

## Annotation

Glucopyranose -> Glucopyranose; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P19642|protein.P19642]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-574`

## Notes

Glucopyranose -> Glucopyranose; direction=LEFT-TO-RIGHT
