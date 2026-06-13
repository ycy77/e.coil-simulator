---
entity_id: "complex.ecocyc.CPLX0-7653"
entity_type: "complex"
name: "water channel AqpZ"
source_database: "EcoCyc"
source_id: "CPLX0-7653"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AqpZ water MIP channel"
  - "aquaporin Z"
---

# water channel AqpZ

`complex.ecocyc.CPLX0-7653`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7653`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60844|protein.P60844]]

## Enriched Summary

EcoCyc complex CPLX0-7653

## Biological Role

Catalyzes TRANS-RXN-145 (reaction.ecocyc.TRANS-RXN-145).

## Annotation

EcoCyc complex CPLX0-7653

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-145|reaction.ecocyc.TRANS-RXN-145]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60844|protein.P60844]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4 | EcoCyc transporter component coefficient=4

## External IDs

- `EcoCyc:CPLX0-7653`
- `QSPROTEOME:QS00181719`

## Notes

4*protein.P60844
