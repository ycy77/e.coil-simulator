---
entity_id: "reaction.ecocyc.3.4.21.87-RXN"
entity_type: "reaction"
name: "3.4.21.87-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.87-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Protease VII"
  - "Protease A"
  - "Outer membrane protein 3B"
---

# 3.4.21.87-RXN

`reaction.ecocyc.3.4.21.87-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.87-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ompT (protein.P09169). Substrates: H2O (molecule.C00001).

## Annotation

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P09169|protein.P09169]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.21.87-RXN`

## Notes

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
