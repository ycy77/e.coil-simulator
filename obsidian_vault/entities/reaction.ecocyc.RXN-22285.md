---
entity_id: "reaction.ecocyc.RXN-22285"
entity_type: "reaction"
name: "RXN-22285"
source_database: "EcoCyc"
source_id: "RXN-22285"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22285

`reaction.ecocyc.RXN-22285`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22285`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-678 -> SE-2 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-678 -> SE-2 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: Hydrogen selenide (molecule.C01528). Products: H+ (molecule.C00080), selenide (molecule.ecocyc.SE-2).

## Annotation

CPD-678 -> SE-2 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SE-2|molecule.ecocyc.SE-2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01528|molecule.C01528]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22285`

## Notes

CPD-678 -> SE-2 + PROTON; direction=REVERSIBLE
