---
entity_id: "reaction.ecocyc.RXN0-6523"
entity_type: "reaction"
name: "RXN0-6523"
source_database: "EcoCyc"
source_id: "RXN0-6523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6523

`reaction.ecocyc.RXN0-6523`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6523`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNASE-G-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNASE-G-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by RNase G (complex.ecocyc.CPLX0-1621). Substrates: H2O (molecule.C00001).

## Annotation

RNASE-G-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1621|complex.ecocyc.CPLX0-1621]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6523`

## Notes

RNASE-G-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
