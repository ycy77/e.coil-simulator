---
entity_id: "reaction.ecocyc.NARX-RXN"
entity_type: "reaction"
name: "NARX-RXN"
source_database: "EcoCyc"
source_id: "NARX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NARX-RXN

`reaction.ecocyc.NARX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NARX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + NARX-CPLX -> ADP + PHOSPHO-NARX; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + NARX-CPLX -> ADP + PHOSPHO-NARX; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1515` NarX Two-Component Signal Transduction System, nitrate dependent (EcoCyc)

## Annotation

ATP + NARX-CPLX -> ADP + PHOSPHO-NARX; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1515` NarX Two-Component Signal Transduction System, nitrate dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NARX-RXN`

## Notes

ATP + NARX-CPLX -> ADP + PHOSPHO-NARX; direction=LEFT-TO-RIGHT
