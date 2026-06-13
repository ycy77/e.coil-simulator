---
entity_id: "complex.ecocyc.CITTRANS-CPLX"
entity_type: "complex"
name: "citrate lyase, citrate-acyl carrier protein transferase component"
source_database: "EcoCyc"
source_id: "CITTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "citrate lyase, citrate-ACP transferase component"
---

# citrate lyase, citrate-acyl carrier protein transferase component

`complex.ecocyc.CITTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CITTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75726|protein.P75726]]

## Enriched Summary

EcoCyc complex CITTRANS-CPLX

## Biological Role

Component of citrate lyase, inactive (complex.ecocyc.CITLY-CPLX).

## Annotation

EcoCyc complex CITTRANS-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P75726|protein.P75726]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CITTRANS-CPLX`
- `QSPROTEOME:QS00183257`

## Notes

6*protein.P75726
