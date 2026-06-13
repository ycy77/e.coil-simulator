---
entity_id: "reaction.ecocyc.3.4.11.2-RXN"
entity_type: "reaction"
name: "3.4.11.2-RXN"
source_database: "EcoCyc"
source_id: "3.4.11.2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Microsomal aminopeptidase"
  - "Aminopeptidase M"
  - "Aminopeptidase N"
  - "Particle-bound aminopeptidase"
  - "Amino-oligopeptidase"
  - "Membrane aminopeptidase I"
  - "Peptidase E"
---

# 3.4.11.2-RXN

`reaction.ecocyc.3.4.11.2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.11.2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the removal of the amino-terminal amino acid of a protein or other polypeptide. EcoCyc reaction equation: Peptide-with-N-terminal-Alanine + WATER -> L-ALPHA-ALANINE + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the removal of the amino-terminal amino acid of a protein or other polypeptide.

## Biological Role

Catalyzed by pepN (protein.P04825). Substrates: H2O (molecule.C00001). Products: L-Alanine (molecule.C00041).

## Annotation

This reaction is the removal of the amino-terminal amino acid of a protein or other polypeptide.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P04825|protein.P04825]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.11.2-RXN`

## Notes

Peptide-with-N-terminal-Alanine + WATER -> L-ALPHA-ALANINE + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
