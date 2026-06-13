---
entity_id: "reaction.ecocyc.CHEBTARD-RXN"
entity_type: "reaction"
name: "CHEBTARD-RXN"
source_database: "EcoCyc"
source_id: "CHEBTARD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHEBTARD-RXN

`reaction.ecocyc.CHEBTARD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHEBTARD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a specific instance of the EC# 3.5.1.44 reaction. EcoCyc reaction equation: WATER + TAR-GLN -> AMMONIA + TAR-GLU; direction=LEFT-TO-RIGHT. This is a specific instance of the EC# 3.5.1.44 reaction.

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001). Products: Ammonia (molecule.C00014).

## Annotation

This is a specific instance of the EC# 3.5.1.44 reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CHEBTARD-RXN`

## Notes

WATER + TAR-GLN -> AMMONIA + TAR-GLU; direction=LEFT-TO-RIGHT
