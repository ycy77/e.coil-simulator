---
entity_id: "complex.ecocyc.CPLX0-7935"
entity_type: "complex"
name: "carbon-phosphorus lyase core complex"
source_database: "EcoCyc"
source_id: "CPLX0-7935"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "C-P lyase core complex"
---

# carbon-phosphorus lyase core complex

`complex.ecocyc.CPLX0-7935`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7935`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16688|protein.P16688]], [[protein.P16687|protein.P16687]], [[protein.P16686|protein.P16686]], [[protein.P16685|protein.P16685]]

## Enriched Summary

EcoCyc complex CPLX0-7935

## Biological Role

Component of carbon-phosphorus lyase core complex (complex.ecocyc.CPLX0-10309).

## Annotation

EcoCyc complex CPLX0-7935

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10309|complex.ecocyc.CPLX0-10309]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P16685|protein.P16685]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16686|protein.P16686]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16687|protein.P16687]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P16688|protein.P16688]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7935`
- `PDB:4XB6`
- `PDB:7Z19`
- `PDB:7Z18`
- `PDB:7Z17`
- `PDB:7Z15`
- `PDB:4XB6`
- `QSPROTEOME:QS00196167`

## Notes

1*protein.P16688|1*protein.P16687|1*protein.P16686|1*protein.P16685
