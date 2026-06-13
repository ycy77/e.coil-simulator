---
entity_id: "reaction.ecocyc.CPXA-RXN"
entity_type: "reaction"
name: "CPXA-RXN"
source_database: "EcoCyc"
source_id: "CPXA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CPXA-RXN

`reaction.ecocyc.CPXA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CPXA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPLX0-8270 -> PHOSPHO-CPXA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-8270 -> PHOSPHO-CPXA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1485` CpxAR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CPLX0-8270 -> PHOSPHO-CPXA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1485` CpxAR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CPXA-RXN`

## Notes

ATP + CPLX0-8270 -> PHOSPHO-CPXA + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
