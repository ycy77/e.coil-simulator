---
entity_id: "reaction.ecocyc.RXN0-7461"
entity_type: "reaction"
name: "RXN0-7461"
source_database: "EcoCyc"
source_id: "RXN0-7461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7461

`reaction.ecocyc.RXN0-7461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7461`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is for tRNA processing of tRNA genes that are from rRNA operons . EcoCyc reaction equation: tRNA-precursor-w-long-5-amp-long-3-extensions + WATER -> tRNA-precursor-w-long-5-amp-medium-3-extensions + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is for tRNA processing of tRNA genes that are from rRNA operons .

## Biological Role

Catalyzed by RNase III (complex.ecocyc.CPLX0-3281). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Annotation

This reaction is for tRNA processing of tRNA genes that are from rRNA operons .

## Pathways

- `ecocyc.PWY0-1623` polycistronic tRNA processing II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3281|complex.ecocyc.CPLX0-3281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7461`

## Notes

tRNA-precursor-w-long-5-amp-long-3-extensions + WATER -> tRNA-precursor-w-long-5-amp-medium-3-extensions + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
