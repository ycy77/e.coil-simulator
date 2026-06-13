---
entity_id: "reaction.ecocyc.3.4.24.55-RXN"
entity_type: "reaction"
name: "3.4.24.55-RXN"
source_database: "EcoCyc"
source_id: "3.4.24.55-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Protease III"
  - "Protease Pi"
---

# 3.4.24.55-RXN

`reaction.ecocyc.3.4.24.55-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.24.55-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is hydrolysis of a peptide bond within a small protein or peptide substrate, less than 7 kDa. EcoCyc reaction equation: General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is hydrolysis of a peptide bond within a small protein or peptide substrate, less than 7 kDa.

## Biological Role

Catalyzed by ptrA (protein.P05458). Substrates: H2O (molecule.C00001).

## Annotation

This reaction is hydrolysis of a peptide bond within a small protein or peptide substrate, less than 7 kDa.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P05458|protein.P05458]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.24.55-RXN`

## Notes

General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
