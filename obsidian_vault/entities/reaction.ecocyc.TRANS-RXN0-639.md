---
entity_id: "reaction.ecocyc.TRANS-RXN0-639"
entity_type: "reaction"
name: "TRANS-RXN0-639"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-639"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-639

`reaction.ecocyc.TRANS-RXN0-639`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-639`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CU+2 -> CU+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CU+2 -> CU+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yebZ (protein.P76278). Substrates: Cu2+ (molecule.ecocyc.CU_2). Products: Cu2+ (molecule.ecocyc.CU_2).

## Annotation

CU+2 -> CU+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76278|protein.P76278]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-639`

## Notes

CU+2 -> CU+2; direction=LEFT-TO-RIGHT
