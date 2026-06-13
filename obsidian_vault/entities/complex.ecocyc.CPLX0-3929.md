---
entity_id: "complex.ecocyc.CPLX0-3929"
entity_type: "complex"
name: "D-arabinose 5-phosphate isomerase GutQ"
source_database: "EcoCyc"
source_id: "CPLX0-3929"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-arabinose 5-phosphate isomerase GutQ

`complex.ecocyc.CPLX0-3929`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3929`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17115|protein.P17115]]

## Enriched Summary

EcoCyc complex CPLX0-3929

## Biological Role

Catalyzes DARAB5PISOM-RXN (reaction.ecocyc.DARAB5PISOM-RXN).

## Annotation

EcoCyc complex CPLX0-3929

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DARAB5PISOM-RXN|reaction.ecocyc.DARAB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P17115|protein.P17115]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3929`
- `QSPROTEOME:QS00049616`

## Notes

4*protein.P17115
