---
entity_id: "complex.ecocyc.GLUTAMATESYN-DIMER"
entity_type: "complex"
name: "glutamate synthase"
source_database: "EcoCyc"
source_id: "GLUTAMATESYN-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate synthase

`complex.ecocyc.GLUTAMATESYN-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTAMATESYN-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09832|protein.P09832]], [[protein.P09831|protein.P09831]]

## Enriched Summary

EcoCyc complex GLUTAMATESYN-DIMER

## Biological Role

Component of glutamate synthase (complex.ecocyc.GLUTAMATESYN-CPLX).

## Annotation

EcoCyc complex GLUTAMATESYN-DIMER

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLUTAMATESYN-CPLX|complex.ecocyc.GLUTAMATESYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P09831|protein.P09831]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P09832|protein.P09832]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:GLUTAMATESYN-DIMER`
- `QSPROTEOME:QS00049380`

## Notes

1*protein.P09832|1*protein.P09831
