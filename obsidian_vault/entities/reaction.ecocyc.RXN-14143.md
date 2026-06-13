---
entity_id: "reaction.ecocyc.RXN-14143"
entity_type: "reaction"
name: "RXN-14143"
source_database: "EcoCyc"
source_id: "RXN-14143"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14143

`reaction.ecocyc.RXN-14143`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14143`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DUMP + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DUMP + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dCMP phosphohydrolase (complex.ecocyc.CPLX0-7625). Substrates: H2O (molecule.C00001), dUMP (molecule.C00365). Products: Deoxyuridine (molecule.C00526), phosphate (molecule.ecocyc.Pi).

## Annotation

DUMP + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7625|complex.ecocyc.CPLX0-7625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00365|molecule.C00365]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14143`

## Notes

DUMP + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
