---
entity_id: "reaction.ecocyc.RXN-20061"
entity_type: "reaction"
name: "RXN-20061"
source_database: "EcoCyc"
source_id: "RXN-20061"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20061

`reaction.ecocyc.RXN-20061`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20061`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21685 -> CPD-21686; direction=REVERSIBLE EcoCyc reaction equation: CPD-21685 -> CPD-21686; direction=REVERSIBLE.

## Biological Role

Substrates: 6-sulfo-α-D-quinovose (molecule.ecocyc.CPD-21685). Products: 6-sulfo-β-D-quinovose (molecule.ecocyc.CPD-21686).

## Enriched Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Annotation

CPD-21685 -> CPD-21686; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7446` sulfoquinovose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-21686|molecule.ecocyc.CPD-21686]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21685|molecule.ecocyc.CPD-21685]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20061`

## Notes

CPD-21685 -> CPD-21686; direction=REVERSIBLE
