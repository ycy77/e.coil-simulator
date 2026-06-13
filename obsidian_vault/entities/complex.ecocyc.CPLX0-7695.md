---
entity_id: "complex.ecocyc.CPLX0-7695"
entity_type: "complex"
name: "glutaminase 2"
source_database: "EcoCyc"
source_id: "CPLX0-7695"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutaminase 2

`complex.ecocyc.CPLX0-7695`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7695`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6W0|protein.P0A6W0]]

## Enriched Summary

EcoCyc complex CPLX0-7695

## Biological Role

Catalyzes GLUTAMIN-RXN (reaction.ecocyc.GLUTAMIN-RXN).

## Annotation

EcoCyc complex CPLX0-7695

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMIN-RXN|reaction.ecocyc.GLUTAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6W0|protein.P0A6W0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7695`
- `QSPROTEOME:QS00049641`

## Notes

2*protein.P0A6W0
