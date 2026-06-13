---
entity_id: "complex.ecocyc.CPLX0-682"
entity_type: "complex"
name: "NAD kinase"
source_database: "EcoCyc"
source_id: "CPLX0-682"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NAD kinase

`complex.ecocyc.CPLX0-682`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-682`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7B3|protein.P0A7B3]]

## Enriched Summary

EcoCyc complex CPLX0-682

## Biological Role

Catalyzes NAD-KIN-RXN (reaction.ecocyc.NAD-KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-682

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NAD-KIN-RXN|reaction.ecocyc.NAD-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7B3|protein.P0A7B3]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-682`
- `QSPROTEOME:QS00049587`

## Notes

6*protein.P0A7B3
