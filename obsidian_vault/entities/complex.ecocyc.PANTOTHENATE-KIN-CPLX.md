---
entity_id: "complex.ecocyc.PANTOTHENATE-KIN-CPLX"
entity_type: "complex"
name: "pantothenate kinase / pantetheine kinase"
source_database: "EcoCyc"
source_id: "PANTOTHENATE-KIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pantothenate kinase / pantetheine kinase

`complex.ecocyc.PANTOTHENATE-KIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PANTOTHENATE-KIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6I3|protein.P0A6I3]]

## Enriched Summary

EcoCyc complex PANTOTHENATE-KIN-CPLX

## Biological Role

Catalyzes PANTETHEINE-KINASE-RXN (reaction.ecocyc.PANTETHEINE-KINASE-RXN), PANTOTHENATE-KIN-RXN (reaction.ecocyc.PANTOTHENATE-KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PANTOTHENATE-KIN-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PANTETHEINE-KINASE-RXN|reaction.ecocyc.PANTETHEINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PANTOTHENATE-KIN-RXN|reaction.ecocyc.PANTOTHENATE-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6I3|protein.P0A6I3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PANTOTHENATE-KIN-CPLX`
- `QSPROTEOME:QS00166025`

## Notes

2*protein.P0A6I3
