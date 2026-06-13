---
entity_id: "reaction.ecocyc.RXN0-5103"
entity_type: "reaction"
name: "RXN0-5103"
source_database: "EcoCyc"
source_id: "RXN0-5103"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5103

`reaction.ecocyc.RXN0-5103`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5103`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by HslVU protease (complex.ecocyc.CPLX0-1163). Substrates: H2O (molecule.C00001).

## Annotation

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1163|complex.ecocyc.CPLX0-1163]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5103`

## Notes

WATER + General-Protein-Substrates -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
