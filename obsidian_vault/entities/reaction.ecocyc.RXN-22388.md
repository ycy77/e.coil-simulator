---
entity_id: "reaction.ecocyc.RXN-22388"
entity_type: "reaction"
name: "RXN-22388"
source_database: "EcoCyc"
source_id: "RXN-22388"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22388

`reaction.ecocyc.RXN-22388`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22388`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16459 -> Pi + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-16459 -> Pi + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: dihydrogen phosphate (molecule.ecocyc.CPD-16459). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-16459 -> Pi + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16459|molecule.ecocyc.CPD-16459]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22388`

## Notes

CPD-16459 -> Pi + PROTON; direction=REVERSIBLE
