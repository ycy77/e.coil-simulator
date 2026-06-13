---
entity_id: "reaction.ecocyc.RXN0-5297"
entity_type: "reaction"
name: "RXN0-5297"
source_database: "EcoCyc"
source_id: "RXN0-5297"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5297

`reaction.ecocyc.RXN0-5297`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5297`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1181 + WATER -> GLC-6-P + CPD-173; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1181 + WATER -> GLC-6-P + CPD-173; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bglB (protein.P11988). Substrates: H2O (molecule.C00001), Salicin 6-phosphate (molecule.C06188). Products: beta-D-Glucose 6-phosphate (molecule.C01172), salicyl alcohol (molecule.ecocyc.CPD-173).

## Annotation

CPD-1181 + WATER -> GLC-6-P + CPD-173; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P11988|protein.P11988]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01172|molecule.C01172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-173|molecule.ecocyc.CPD-173]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06188|molecule.C06188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5297`

## Notes

CPD-1181 + WATER -> GLC-6-P + CPD-173; direction=PHYSIOL-LEFT-TO-RIGHT
