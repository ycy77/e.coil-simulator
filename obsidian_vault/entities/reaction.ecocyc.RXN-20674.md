---
entity_id: "reaction.ecocyc.RXN-20674"
entity_type: "reaction"
name: "RXN-20674"
source_database: "EcoCyc"
source_id: "RXN-20674"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20674

`reaction.ecocyc.RXN-20674`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20674`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22307 -> DEHYDROQUINATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-22307 -> DEHYDROQUINATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 3-deoxy-D-arabino-heptulopyranuronate 7-phosphate (molecule.ecocyc.CPD-22307). Products: 3-Dehydroquinate (molecule.C00944), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-22307 -> DEHYDROQUINATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00944|molecule.C00944]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22307|molecule.ecocyc.CPD-22307]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20674`

## Notes

CPD-22307 -> DEHYDROQUINATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
