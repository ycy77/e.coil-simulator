---
entity_id: "reaction.ecocyc.RXN66-526"
entity_type: "reaction"
name: "RXN66-526"
source_database: "EcoCyc"
source_id: "RXN66-526"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN66-526

`reaction.ecocyc.RXN66-526`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN66-526`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

D-glucopyranose-6-phosphate + WATER -> Glucopyranose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-glucopyranose-6-phosphate + WATER -> Glucopyranose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), D-Glucose 6-phosphate (molecule.C00092). Products: D-Glucose (molecule.C00031), phosphate (molecule.ecocyc.Pi).

## Annotation

D-glucopyranose-6-phosphate + WATER -> Glucopyranose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN66-526`

## Notes

D-glucopyranose-6-phosphate + WATER -> Glucopyranose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
