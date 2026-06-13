---
entity_id: "reaction.ecocyc.RXN-22316"
entity_type: "reaction"
name: "RXN-22316"
source_database: "EcoCyc"
source_id: "RXN-22316"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22316

`reaction.ecocyc.RXN-22316`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22316`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-763 -> CPD-24319 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-763 -> CPD-24319 + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: arsenite (molecule.ecocyc.CPD-763). Products: H+ (molecule.C00080), arsenite2- (molecule.ecocyc.CPD-24319).

## Annotation

CPD-763 -> CPD-24319 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24319|molecule.ecocyc.CPD-24319]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-763|molecule.ecocyc.CPD-763]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22316`

## Notes

CPD-763 -> CPD-24319 + PROTON; direction=REVERSIBLE
