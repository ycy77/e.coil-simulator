---
entity_id: "complex.ecocyc.PC00003"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator AraC"
source_database: "EcoCyc"
source_id: "PC00003"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AraC"
---

# DNA-binding transcriptional dual regulator AraC

`complex.ecocyc.PC00003`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00003`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9E0|protein.P0A9E0]]

## Enriched Summary

EcoCyc complex PC00003

## Biological Role

Component of AraC-α-L-arabinopyranose DNA-binding transcriptional activator (complex.ecocyc.CPLX-172), AraC-D-fucose (complex.ecocyc.CPLX0-9162).

## Annotation

EcoCyc complex PC00003

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-172|complex.ecocyc.CPLX-172]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9162|complex.ecocyc.CPLX0-9162]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9E0|protein.P0A9E0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PC00003`
- `QSPROTEOME:QS00049739`

## Notes

2*protein.P0A9E0
