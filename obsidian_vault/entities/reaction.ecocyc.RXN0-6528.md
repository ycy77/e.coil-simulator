---
entity_id: "reaction.ecocyc.RXN0-6528"
entity_type: "reaction"
name: "RXN0-6528"
source_database: "EcoCyc"
source_id: "RXN0-6528"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6528

`reaction.ecocyc.RXN0-6528`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6528`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

YHAV-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: YHAV-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yhaV (protein.P64594). Substrates: H2O (molecule.C00001).

## Annotation

YHAV-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P64594|protein.P64594]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6528`

## Notes

YHAV-DEGRADATION-SUBSTRATE-MRNA + WATER -> mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
