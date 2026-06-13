---
entity_id: "reaction.ecocyc.RXN0-6446"
entity_type: "reaction"
name: "RXN0-6446"
source_database: "EcoCyc"
source_id: "RXN0-6446"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6446

`reaction.ecocyc.RXN0-6446`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6446`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

EG12658-MONOMER + ATP -> MONOMER0-4171 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: EG12658-MONOMER + ATP -> MONOMER0-4171 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1470` QseBC Two-Component Signal Transduction System, quorum sensing related (EcoCyc)

## Annotation

EG12658-MONOMER + ATP -> MONOMER0-4171 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1470` QseBC Two-Component Signal Transduction System, quorum sensing related (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6446`

## Notes

EG12658-MONOMER + ATP -> MONOMER0-4171 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
