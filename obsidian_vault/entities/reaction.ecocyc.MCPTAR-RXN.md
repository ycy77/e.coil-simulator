---
entity_id: "reaction.ecocyc.MCPTAR-RXN"
entity_type: "reaction"
name: "MCPTAR-RXN"
source_database: "EcoCyc"
source_id: "MCPTAR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MCPTAR-RXN

`reaction.ecocyc.MCPTAR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MCPTAR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a specific instance of EC# 3.1.1.61 reaction. EcoCyc reaction equation: WATER + TAR-GLUME -> METOH + TAR-GLU; direction=LEFT-TO-RIGHT. This is a specific instance of EC# 3.1.1.61 reaction.

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001). Products: Methanol (molecule.C00132).

## Annotation

This is a specific instance of EC# 3.1.1.61 reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MCPTAR-RXN`

## Notes

WATER + TAR-GLUME -> METOH + TAR-GLU; direction=LEFT-TO-RIGHT
