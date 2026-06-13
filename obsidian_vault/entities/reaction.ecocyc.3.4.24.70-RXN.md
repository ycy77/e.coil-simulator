---
entity_id: "reaction.ecocyc.3.4.24.70-RXN"
entity_type: "reaction"
name: "3.4.24.70-RXN"
source_database: "EcoCyc"
source_id: "3.4.24.70-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.24.70-RXN

`reaction.ecocyc.3.4.24.70-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.24.70-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction involves broad-specificity hydrolysis of peptide bonds. EcoCyc reaction equation: WATER + OLIGOPEPTIDES -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction involves broad-specificity hydrolysis of peptide bonds.

## Biological Role

Catalyzed by prlC (protein.P27298). Substrates: H2O (molecule.C00001), Oligopeptide (molecule.C00098).

## Annotation

This reaction involves broad-specificity hydrolysis of peptide bonds.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27298|protein.P27298]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00098|molecule.C00098]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.24.70-RXN`

## Notes

WATER + OLIGOPEPTIDES -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT
