---
entity_id: "reaction.ecocyc.RXN0-6480"
entity_type: "reaction"
name: "RXN0-6480"
source_database: "EcoCyc"
source_id: "RXN0-6480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6480

`reaction.ecocyc.RXN0-6480`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6480`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2354 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2354 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382), ribonuclease T (complex.ecocyc.CPLX0-3602). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY-8468` monocistronic tRNA processing I (EcoCyc)

## Annotation

CPD0-2354 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8468` monocistronic tRNA processing I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3602|complex.ecocyc.CPLX0-3602]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6480`

## Notes

CPD0-2354 + WATER -> tRNAs + tRNA-fragment; direction=PHYSIOL-LEFT-TO-RIGHT
