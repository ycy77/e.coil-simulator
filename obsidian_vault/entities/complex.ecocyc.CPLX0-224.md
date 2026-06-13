---
entity_id: "complex.ecocyc.CPLX0-224"
entity_type: "complex"
name: "NADPH-dependent FMN reductase"
source_database: "EcoCyc"
source_id: "CPLX0-224"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADPH-dependent FMN reductase

`complex.ecocyc.CPLX0-224`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-224`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P80644|protein.P80644]]

## Enriched Summary

EcoCyc complex CPLX0-224

## Biological Role

Catalyzes RXN-12444 (reaction.ecocyc.RXN-12444).

## Annotation

EcoCyc complex CPLX0-224

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12444|reaction.ecocyc.RXN-12444]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P80644|protein.P80644]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-224`
- `QSPROTEOME:QS00185223`

## Notes

2*protein.P80644
