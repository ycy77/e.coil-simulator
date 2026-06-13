---
entity_id: "reaction.ecocyc.RXN0-7476"
entity_type: "reaction"
name: "RXN0-7476"
source_database: "EcoCyc"
source_id: "RXN0-7476"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7476

`reaction.ecocyc.RXN0-7476`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7476`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction describes the endonucleolytic cleavage of tRNA transcripts found in the spacer regions between the 16S and 23S rRNAs in each rRNA operon in TAX-562. It is catalyzed by CPLX0-3281 . EcoCyc reaction equation: polycistronic-tRNA-amp-rRNA-transcript + WATER -> tRNA-precursor-w-long-5-amp-long-3-extensions + partially-processed-rRNA-transcript; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction describes the endonucleolytic cleavage of tRNA transcripts found in the spacer regions between the 16S and 23S rRNAs in each rRNA operon in TAX-562. It is catalyzed by CPLX0-3281 .

## Biological Role

Catalyzed by RNase III (complex.ecocyc.CPLX0-3281). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

This reaction describes the endonucleolytic cleavage of tRNA transcripts found in the spacer regions between the 16S and 23S rRNAs in each rRNA operon in TAX-562. It is catalyzed by CPLX0-3281 .

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3281|complex.ecocyc.CPLX0-3281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7476`

## Notes

polycistronic-tRNA-amp-rRNA-transcript + WATER -> tRNA-precursor-w-long-5-amp-long-3-extensions + partially-processed-rRNA-transcript; direction=PHYSIOL-LEFT-TO-RIGHT
