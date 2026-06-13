---
entity_id: "reaction.ecocyc.RXN-17330"
entity_type: "reaction"
name: "RXN-17330"
source_database: "EcoCyc"
source_id: "RXN-17330"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17330

`reaction.ecocyc.RXN-17330`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17330`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

D-glucose-1-phosphates + WATER -> Glucopyranose + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-glucose-1-phosphates + WATER -> Glucopyranose + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), D-Glucose 1-phosphate (molecule.C00103). Products: D-Glucose (molecule.C00031), phosphate (molecule.ecocyc.Pi).

## Annotation

D-glucose-1-phosphates + WATER -> Glucopyranose + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00103|molecule.C00103]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17330`

## Notes

D-glucose-1-phosphates + WATER -> Glucopyranose + Pi; direction=LEFT-TO-RIGHT
