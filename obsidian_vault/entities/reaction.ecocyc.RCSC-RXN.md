---
entity_id: "reaction.ecocyc.RCSC-RXN"
entity_type: "reaction"
name: "RCSC-RXN"
source_database: "EcoCyc"
source_id: "RCSC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RCSC-RXN

`reaction.ecocyc.RCSC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RCSC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + RCSC-MONOMER -> ADP + PHOSPHO-RCSC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + RCSC-MONOMER -> ADP + PHOSPHO-RCSC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1493` Rcs Signal Transduction System (EcoCyc)

## Annotation

ATP + RCSC-MONOMER -> ADP + PHOSPHO-RCSC; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1493` Rcs Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RCSC-RXN`

## Notes

ATP + RCSC-MONOMER -> ADP + PHOSPHO-RCSC; direction=PHYSIOL-LEFT-TO-RIGHT
