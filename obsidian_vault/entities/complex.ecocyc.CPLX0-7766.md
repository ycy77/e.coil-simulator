---
entity_id: "complex.ecocyc.CPLX0-7766"
entity_type: "complex"
name: "proofreading thioesterase in enterobactin biosynthesis"
source_database: "EcoCyc"
source_id: "CPLX0-7766"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# proofreading thioesterase in enterobactin biosynthesis

`complex.ecocyc.CPLX0-7766`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7766`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8Y8|protein.P0A8Y8]]

## Enriched Summary

EcoCyc complex CPLX0-7766

## Biological Role

Catalyzes RXN0-7046 (reaction.ecocyc.RXN0-7046), RXN0-7105 (reaction.ecocyc.RXN0-7105).

## Annotation

EcoCyc complex CPLX0-7766

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7046|reaction.ecocyc.RXN0-7046]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7105|reaction.ecocyc.RXN0-7105]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8Y8|protein.P0A8Y8]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7766`
- `QSPROTEOME:QS00049663`

## Notes

4*protein.P0A8Y8
