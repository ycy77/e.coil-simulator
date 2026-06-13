---
entity_id: "reaction.ecocyc.RXN-14521"
entity_type: "reaction"
name: "RXN-14521"
source_database: "EcoCyc"
source_id: "RXN-14521"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14521

`reaction.ecocyc.RXN-14521`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14521`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3732 + WATER -> THYMIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3732 + WATER -> THYMIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), thymidine 3'-monophosphate (molecule.ecocyc.CPD-3732). Products: Thymidine (molecule.C00214), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3732 + WATER -> THYMIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3732|molecule.ecocyc.CPD-3732]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14521`

## Notes

CPD-3732 + WATER -> THYMIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
