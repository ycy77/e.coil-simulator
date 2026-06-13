---
entity_id: "reaction.ecocyc.RXN0-6388"
entity_type: "reaction"
name: "RXN0-6388"
source_database: "EcoCyc"
source_id: "RXN0-6388"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6388

`reaction.ecocyc.RXN0-6388`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6388`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPLX0-8275 -> MONOMER0-4141 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPLX0-8275 -> MONOMER0-4141 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1503` GlrKR Two-Component Signal Transduction System (EcoCyc)

## Annotation

ATP + CPLX0-8275 -> MONOMER0-4141 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1503` GlrKR Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6388`

## Notes

ATP + CPLX0-8275 -> MONOMER0-4141 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
