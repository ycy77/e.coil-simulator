---
entity_id: "reaction.ecocyc.PHOR-RXN"
entity_type: "reaction"
name: "PHOR-RXN"
source_database: "EcoCyc"
source_id: "PHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOR-RXN

`reaction.ecocyc.PHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + PHOR-CPLX -> ADP + PHOSPHO-PHOR; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + PHOR-CPLX -> ADP + PHOSPHO-PHOR; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1483` PhoRB Two-Component Signal Transduction System, phosphate-dependent (EcoCyc)

## Annotation

ATP + PHOR-CPLX -> ADP + PHOSPHO-PHOR; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1483` PhoRB Two-Component Signal Transduction System, phosphate-dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOR-RXN`

## Notes

ATP + PHOR-CPLX -> ADP + PHOSPHO-PHOR; direction=LEFT-TO-RIGHT
