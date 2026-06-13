---
entity_id: "reaction.ecocyc.3.4.21.107-RXN"
entity_type: "reaction"
name: "3.4.21.107-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.107-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.21.107-RXN

`reaction.ecocyc.3.4.21.107-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.107-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by periplasmic serine endoprotease DegP (complex.ecocyc.CPLX0-2921), bepA (protein.P66948). Substrates: H2O (molecule.C00001).

## Annotation

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2921|complex.ecocyc.CPLX0-2921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P66948|protein.P66948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.21.107-RXN`

## Notes

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
