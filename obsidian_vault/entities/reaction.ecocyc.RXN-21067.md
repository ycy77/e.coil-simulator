---
entity_id: "reaction.ecocyc.RXN-21067"
entity_type: "reaction"
name: "RXN-21067"
source_database: "EcoCyc"
source_id: "RXN-21067"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21067

`reaction.ecocyc.RXN-21067`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21067`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22690 + WATER -> CPD0-2367 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-22690 + WATER -> CPD0-2367 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yjjG (protein.P0A8Y1). Substrates: H2O (molecule.C00001), 5-fluorouridine 5'-monophosphate (molecule.ecocyc.CPD-22690). Products: 5-fluorouridine (molecule.ecocyc.CPD0-2367), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-22690 + WATER -> CPD0-2367 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A8Y1|protein.P0A8Y1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2367|molecule.ecocyc.CPD0-2367]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22690|molecule.ecocyc.CPD-22690]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21067`

## Notes

CPD-22690 + WATER -> CPD0-2367 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
