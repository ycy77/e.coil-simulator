---
entity_id: "complex.ecocyc.ATPE-CPLX"
entity_type: "complex"
name: "ATP synthase Fo complex - subunit c"
source_database: "EcoCyc"
source_id: "ATPE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP synthase Fo complex - subunit c

`complex.ecocyc.ATPE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P68699|protein.P68699]]

## Enriched Summary

EcoCyc complex ATPE-CPLX

## Biological Role

Component of ATP synthase Fo complex (complex.ecocyc.F-O-CPLX).

## Annotation

EcoCyc complex ATPE-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P68699|protein.P68699]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:ATPE-CPLX`
- `QSPROTEOME:QS00049575`

## Notes

10*protein.P68699
