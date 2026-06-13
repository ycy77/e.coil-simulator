---
entity_id: "reaction.ecocyc.RXN-24138"
entity_type: "reaction"
name: "endoribonuclease"
source_database: "EcoCyc"
source_id: "RXN-24138"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# endoribonuclease

`reaction.ecocyc.RXN-24138`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24138`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction represents the exonucleolytic cleavage of 3' nucleotides in tRNA processing pathway . EcoCyc reaction equation: a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> a-tRNA-precursor-w-5-extension-and-medium-3-trailer + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents the exonucleolytic cleavage of 3' nucleotides in tRNA processing pathway .

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Annotation

This reaction represents the exonucleolytic cleavage of 3' nucleotides in tRNA processing pathway .

## Pathways

- `ecocyc.PWY0-1614` monocistronic leuX tRNA processing (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24138`

## Notes

a-monocistronic-tRNA-transcript-with-long-3-extension + WATER -> a-tRNA-precursor-w-5-extension-and-medium-3-trailer + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
