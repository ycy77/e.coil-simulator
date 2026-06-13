---
entity_id: "reaction.ecocyc.RXN0-7483"
entity_type: "reaction"
name: "RXN0-7483"
source_database: "EcoCyc"
source_id: "RXN0-7483"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7483

`reaction.ecocyc.RXN0-7483`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7483`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is one of the first reactions of the branched PWY0-1614 . EcoCyc reaction equation: a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> CPD0-2352 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is one of the first reactions of the branched PWY0-1614 .

## Biological Role

Catalyzed by polynucleotide phosphorylase (complex.ecocyc.CPLX0-3521). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Annotation

This reaction is one of the first reactions of the branched PWY0-1614 .

## Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3521|complex.ecocyc.CPLX0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7483`

## Notes

a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> CPD0-2352 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
