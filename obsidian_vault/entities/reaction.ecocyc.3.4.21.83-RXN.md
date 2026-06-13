---
entity_id: "reaction.ecocyc.3.4.21.83-RXN"
entity_type: "reaction"
name: "3.4.21.83-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.83-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Protease II"
---

# 3.4.21.83-RXN

`reaction.ecocyc.3.4.21.83-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.83-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond following an arginine or lysine. EcoCyc reaction equation: OLIGOPEPTIDES + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond following an arginine or lysine.

## Biological Role

Catalyzed by ptrB (protein.P24555). Substrates: H2O (molecule.C00001), Oligopeptide (molecule.C00098).

## Annotation

This reaction is the hydrolysis of a peptide bond following an arginine or lysine.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P24555|protein.P24555]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.21.83-RXN`

## Notes

OLIGOPEPTIDES + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT
