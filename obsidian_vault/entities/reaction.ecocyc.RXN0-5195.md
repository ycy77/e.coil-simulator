---
entity_id: "reaction.ecocyc.RXN0-5195"
entity_type: "reaction"
name: "RXN0-5195"
source_database: "EcoCyc"
source_id: "RXN0-5195"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5195

`reaction.ecocyc.RXN0-5195`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5195`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the cleavage of an internal amine bond within a polypeptide. EcoCyc reaction equation: General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the cleavage of an internal amine bond within a polypeptide.

## Biological Role

Catalyzed by pepN (protein.P04825). Substrates: H2O (molecule.C00001).

## Annotation

This reaction is the cleavage of an internal amine bond within a polypeptide.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P04825|protein.P04825]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5195`

## Notes

General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
