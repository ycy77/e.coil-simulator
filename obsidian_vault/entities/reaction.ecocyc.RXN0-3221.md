---
entity_id: "reaction.ecocyc.RXN0-3221"
entity_type: "reaction"
name: "RXN0-3221"
source_database: "EcoCyc"
source_id: "RXN0-3221"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3221

`reaction.ecocyc.RXN0-3221`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3221`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond. EcoCyc reaction equation: General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond.

## Biological Role

Catalyzed by loiP (protein.P25894). Substrates: H2O (molecule.C00001).

## Annotation

This reaction is the hydrolysis of a peptide bond.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P25894|protein.P25894]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3221`

## Notes

General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
