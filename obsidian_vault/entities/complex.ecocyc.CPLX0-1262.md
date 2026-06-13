---
entity_id: "complex.ecocyc.CPLX0-1262"
entity_type: "complex"
name: "D-arabinose 5-phosphate isomerase KdsD"
source_database: "EcoCyc"
source_id: "CPLX0-1262"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-arabinose 5-phosphate isomerase KdsD

`complex.ecocyc.CPLX0-1262`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1262`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P45395|protein.P45395]]

## Enriched Summary

EcoCyc complex CPLX0-1262

## Biological Role

Catalyzes DARAB5PISOM-RXN (reaction.ecocyc.DARAB5PISOM-RXN).

## Annotation

EcoCyc complex CPLX0-1262

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DARAB5PISOM-RXN|reaction.ecocyc.DARAB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P45395|protein.P45395]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-1262`
- `QSPROTEOME:QS00049594`

## Notes

4*protein.P45395
