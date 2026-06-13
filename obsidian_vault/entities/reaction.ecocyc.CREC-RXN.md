---
entity_id: "reaction.ecocyc.CREC-RXN"
entity_type: "reaction"
name: "CREC-RXN"
source_database: "EcoCyc"
source_id: "CREC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CREC-RXN

`reaction.ecocyc.CREC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CREC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + CREC-CPLX -> ADP + PHOSPHO-CREC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CREC-CPLX -> ADP + PHOSPHO-CREC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1487` CreCB Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CREC-CPLX -> ADP + PHOSPHO-CREC; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1487` CreCB Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CREC-RXN`

## Notes

ATP + CREC-CPLX -> ADP + PHOSPHO-CREC; direction=PHYSIOL-LEFT-TO-RIGHT
