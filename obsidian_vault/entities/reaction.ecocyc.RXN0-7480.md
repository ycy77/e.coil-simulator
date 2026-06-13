---
entity_id: "reaction.ecocyc.RXN0-7480"
entity_type: "reaction"
name: "RXN0-7480"
source_database: "EcoCyc"
source_id: "RXN0-7480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7480

`reaction.ecocyc.RXN0-7480`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7480`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the nucleolytic cleavage of a tRNA from a polycistronic transcription containing tRNA and mRNA regions in a step of a tRNA precursor processing pathway. EcoCyc reaction equation: a-polycistronic-containing-mRNA-amp-tRNA-with-a-short-3-exte + WATER -> CPD0-2353 + Pre-mRNA; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the nucleolytic cleavage of a tRNA from a polycistronic transcription containing tRNA and mRNA regions in a step of a tRNA precursor processing pathway.

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)

## Annotation

This reaction represents the nucleolytic cleavage of a tRNA from a polycistronic transcription containing tRNA and mRNA regions in a step of a tRNA precursor processing pathway.

## Pathways

- `ecocyc.PWY0-1626` polycistronic tRNA processing III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7480`

## Notes

a-polycistronic-containing-mRNA-amp-tRNA-with-a-short-3-exte + WATER -> CPD0-2353 + Pre-mRNA; direction=PHYSIOL-LEFT-TO-RIGHT
