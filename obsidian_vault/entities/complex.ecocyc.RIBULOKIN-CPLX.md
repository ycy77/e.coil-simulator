---
entity_id: "complex.ecocyc.RIBULOKIN-CPLX"
entity_type: "complex"
name: "ribulokinase"
source_database: "EcoCyc"
source_id: "RIBULOKIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribulokinase

`complex.ecocyc.RIBULOKIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIBULOKIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08204|protein.P08204]]

## Enriched Summary

EcoCyc complex RIBULOKIN-CPLX

## Biological Role

Catalyzes RXN0-5116 (reaction.ecocyc.RXN0-5116).

## Annotation

EcoCyc complex RIBULOKIN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5116|reaction.ecocyc.RXN0-5116]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08204|protein.P08204]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIBULOKIN-CPLX`
- `QSPROTEOME:QS00049549`

## Notes

2*protein.P08204
