---
entity_id: "reaction.ecocyc.TRANS-RXN0-575"
entity_type: "reaction"
name: "TRANS-RXN0-575"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-575"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-575

`reaction.ecocyc.TRANS-RXN0-575`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-575`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by malX (protein.P19642). Substrates: Maltose (molecule.C00208). Products: Maltose (molecule.C00208).

## Annotation

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P19642|protein.P19642]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-575`

## Notes

MALTOSE -> MALTOSE; direction=LEFT-TO-RIGHT
