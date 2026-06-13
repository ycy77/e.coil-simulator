---
entity_id: "reaction.ecocyc.RXN0-7482"
entity_type: "reaction"
name: "RXN0-7482"
source_database: "EcoCyc"
source_id: "RXN0-7482"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7482

`reaction.ecocyc.RXN0-7482`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7482`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is specific for exonucleolytic removal of 3' Rho-independent transcription terminator . EcoCyc reaction equation: a-polycistronic-tRNA-precursor-with-long-3-extension + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is specific for exonucleolytic removal of 3' Rho-independent transcription terminator .

## Biological Role

Catalyzed by polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521), rnb (protein.P30850). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Annotation

This reaction is specific for exonucleolytic removal of 3' Rho-independent transcription terminator .

## Pathways

- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30850|protein.P30850]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7482`

## Notes

a-polycistronic-tRNA-precursor-with-long-3-extension + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
