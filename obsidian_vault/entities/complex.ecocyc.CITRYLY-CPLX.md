---
entity_id: "complex.ecocyc.CITRYLY-CPLX"
entity_type: "complex"
name: "citrate lyase, citryl-acyl carrrier protein lyase component"
source_database: "EcoCyc"
source_id: "CITRYLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "citrate lyase, citryl-ACP lyase component"
---

# citrate lyase, citryl-acyl carrrier protein lyase component

`complex.ecocyc.CITRYLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CITRYLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9I1|protein.P0A9I1]]

## Enriched Summary

EcoCyc complex CITRYLY-CPLX

## Biological Role

Component of citrate lyase, inactive (complex.ecocyc.CITLY-CPLX).

## Annotation

EcoCyc complex CITRYLY-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9I1|protein.P0A9I1]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CITRYLY-CPLX`
- `QSPROTEOME:QS00049357`

## Notes

6*protein.P0A9I1
