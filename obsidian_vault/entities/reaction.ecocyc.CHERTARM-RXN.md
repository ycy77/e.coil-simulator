---
entity_id: "reaction.ecocyc.CHERTARM-RXN"
entity_type: "reaction"
name: "CHERTARM-RXN"
source_database: "EcoCyc"
source_id: "CHERTARM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHERTARM-RXN

`reaction.ecocyc.CHERTARM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHERTARM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is a specific instance of EC# 2.1.1.80 reaction. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + TAR-GLU -> ADENOSYL-HOMO-CYS + TAR-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is a specific instance of EC# 2.1.1.80 reaction.

## Biological Role

Catalyzed by cheR (protein.P07364). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

This reaction is a specific instance of EC# 2.1.1.80 reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P07364|protein.P07364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[protein.ecocyc.TAR-GLUME|protein.ecocyc.TAR-GLUME]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CHERTARM-RXN`

## Notes

S-ADENOSYLMETHIONINE + TAR-GLU -> ADENOSYL-HOMO-CYS + TAR-GLUME; direction=PHYSIOL-LEFT-TO-RIGHT
