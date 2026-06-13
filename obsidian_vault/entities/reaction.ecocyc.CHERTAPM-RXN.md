---
entity_id: "reaction.ecocyc.CHERTAPM-RXN"
entity_type: "reaction"
name: "CHERTAPM-RXN"
source_database: "EcoCyc"
source_id: "CHERTAPM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHERTAPM-RXN

`reaction.ecocyc.CHERTAPM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHERTAPM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is a specific instance of EC# 2.1.1.80 reaction. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + TAP-GLU -> ADENOSYL-HOMO-CYS + TAP-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is a specific instance of EC# 2.1.1.80 reaction.

## Biological Role

Catalyzed by cheR (protein.P07364). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

This reaction is a specific instance of EC# 2.1.1.80 reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07364|protein.P07364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CHERTAPM-RXN`

## Notes

S-ADENOSYLMETHIONINE + TAP-GLU -> ADENOSYL-HOMO-CYS + TAP-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT
