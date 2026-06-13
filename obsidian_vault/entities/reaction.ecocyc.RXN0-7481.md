---
entity_id: "reaction.ecocyc.RXN0-7481"
entity_type: "reaction"
name: "RXN0-7481"
source_database: "EcoCyc"
source_id: "RXN0-7481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7481

`reaction.ecocyc.RXN0-7481`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7481`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2350 + WATER -> CPD0-2353 + a-polycistronic-tRNA-precursor-with-long-3-extension; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2350 + WATER -> CPD0-2353 + a-polycistronic-tRNA-precursor-with-long-3-extension; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNase P (complex.ecocyc.CPLX0-1382). Substrates: H2O (molecule.C00001).

## Enriched Pathways

- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Annotation

CPD0-2350 + WATER -> CPD0-2353 + a-polycistronic-tRNA-precursor-with-long-3-extension; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1627` polycistronic tRNA processing IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1382|complex.ecocyc.CPLX0-1382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7481`

## Notes

CPD0-2350 + WATER -> CPD0-2353 + a-polycistronic-tRNA-precursor-with-long-3-extension; direction=PHYSIOL-LEFT-TO-RIGHT
