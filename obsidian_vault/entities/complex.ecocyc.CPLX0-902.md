---
entity_id: "complex.ecocyc.CPLX0-902"
entity_type: "complex"
name: "tautomerase PptA"
source_database: "EcoCyc"
source_id: "CPLX0-902"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tautomerase PptA

`complex.ecocyc.CPLX0-902`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-902`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31992|protein.P31992]]

## Enriched Summary

EcoCyc complex CPLX0-902

## Biological Role

Catalyzes RXN-19492 (reaction.ecocyc.RXN-19492).

## Annotation

EcoCyc complex CPLX0-902

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19492|reaction.ecocyc.RXN-19492]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31992|protein.P31992]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-902`
- `QSPROTEOME:QS00195537`

## Notes

2*protein.P31992
