---
entity_id: "reaction.ecocyc.RXN0-7478"
entity_type: "reaction"
name: "RXN0-7478"
source_database: "EcoCyc"
source_id: "RXN0-7478"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7478

`reaction.ecocyc.RXN0-7478`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7478`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is for tRNA processing of tRNA genes in rRNA operons . EcoCyc reaction equation: tRNA-precursor-w-long-5-extension-amp-short-3-extension + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is for tRNA processing of tRNA genes in rRNA operons .

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

This reaction is for tRNA processing of tRNA genes in rRNA operons .

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7478`

## Notes

tRNA-precursor-w-long-5-extension-amp-short-3-extension + WATER -> CPD0-2353 + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
