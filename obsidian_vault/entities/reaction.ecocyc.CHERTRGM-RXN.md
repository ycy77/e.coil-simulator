---
entity_id: "reaction.ecocyc.CHERTRGM-RXN"
entity_type: "reaction"
name: "CHERTRGM-RXN"
source_database: "EcoCyc"
source_id: "CHERTRGM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHERTRGM-RXN

`reaction.ecocyc.CHERTRGM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHERTRGM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is a specific instance of EC# 2.1.1.80 reaction. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + TRG-GLU -> ADENOSYL-HOMO-CYS + TRG-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is a specific instance of EC# 2.1.1.80 reaction.

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

- `EcoCyc:CHERTRGM-RXN`

## Notes

S-ADENOSYLMETHIONINE + TRG-GLU -> ADENOSYL-HOMO-CYS + TRG-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT
