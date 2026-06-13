---
entity_id: "complex.ecocyc.CPLX0-1421"
entity_type: "complex"
name: "bacterioferritin"
source_database: "EcoCyc"
source_id: "CPLX0-1421"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# bacterioferritin

`complex.ecocyc.CPLX0-1421`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1421`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABD3|protein.P0ABD3]]

## Enriched Summary

EcoCyc complex CPLX0-1421

## Biological Role

Catalyzes RXN0-1483 (reaction.ecocyc.RXN0-1483).

## Annotation

EcoCyc complex CPLX0-1421

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1483|reaction.ecocyc.RXN0-1483]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABD3|protein.P0ABD3]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## External IDs

- `EcoCyc:CPLX0-1421`
- `QSPROTEOME:QS00183189`

## Notes

24*protein.P0ABD3
