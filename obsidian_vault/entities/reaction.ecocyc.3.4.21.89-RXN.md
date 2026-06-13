---
entity_id: "reaction.ecocyc.3.4.21.89-RXN"
entity_type: "reaction"
name: "3.4.21.89-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.89-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Bacterial leader peptidase I"
  - "SPase I"
  - "Phage-procoat-leader peptidase"
---

# 3.4.21.89-RXN

`reaction.ecocyc.3.4.21.89-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.89-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Peptides-with-Leader-Sequence + WATER -> Peptides-holder + Leader-Sequences; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Peptides-with-Leader-Sequence + WATER -> Peptides-holder + Leader-Sequences; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lepB (protein.P00803). Substrates: H2O (molecule.C00001).

## Annotation

Peptides-with-Leader-Sequence + WATER -> Peptides-holder + Leader-Sequences; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P00803|protein.P00803]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.21.89-RXN`

## Notes

Peptides-with-Leader-Sequence + WATER -> Peptides-holder + Leader-Sequences; direction=PHYSIOL-LEFT-TO-RIGHT
