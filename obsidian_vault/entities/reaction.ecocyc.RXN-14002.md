---
entity_id: "reaction.ecocyc.RXN-14002"
entity_type: "reaction"
name: "RXN-14002"
source_database: "EcoCyc"
source_id: "RXN-14002"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14002

`reaction.ecocyc.RXN-14002`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14002`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14101 + WATER -> CPD-12367 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14101 + WATER -> CPD-12367 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutT (protein.P08337). Substrates: H2O (molecule.C00001), 8-oxo-GDP (molecule.ecocyc.CPD-14101). Products: H+ (molecule.C00080), 8-oxo-GMP (molecule.ecocyc.CPD-12367), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-14101 + WATER -> CPD-12367 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08337|protein.P08337]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12367|molecule.ecocyc.CPD-12367]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14101|molecule.ecocyc.CPD-14101]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14002`

## Notes

CPD-14101 + WATER -> CPD-12367 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
