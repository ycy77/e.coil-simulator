---
entity_id: "complex.ecocyc.CPLX0-7698"
entity_type: "complex"
name: "MukF dimer"
source_database: "EcoCyc"
source_id: "CPLX0-7698"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# MukF dimer

`complex.ecocyc.CPLX0-7698`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7698`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60293|protein.P60293]]

## Enriched Summary

EcoCyc complex CPLX0-7698

## Biological Role

Component of MukEF complex (complex.ecocyc.CPLX0-7697).

## Annotation

EcoCyc complex CPLX0-7698

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7697|complex.ecocyc.CPLX0-7697]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60293|protein.P60293]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7698`
- `QSPROTEOME:QS00049642`

## Notes

2*protein.P60293
