---
entity_id: "reaction.ecocyc.RXN-24141"
entity_type: "reaction"
name: "RXN-24141"
source_database: "EcoCyc"
source_id: "RXN-24141"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24141

`reaction.ecocyc.RXN-24141`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24141`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8122 + CPD-3 -> CPD-26686 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8122 + CPD-3 -> CPD-26686 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Molybdate (molecule.C06232), Adenylated molybdopterin (molecule.C19848). Products: H2O (molecule.C00001), adenylyl MoO3-molybdopterin cofactor (molecule.ecocyc.CPD-26686).

## Annotation

CPD-8122 + CPD-3 -> CPD-26686 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26686|molecule.ecocyc.CPD-26686]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19848|molecule.C19848]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24141`

## Notes

CPD-8122 + CPD-3 -> CPD-26686 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
