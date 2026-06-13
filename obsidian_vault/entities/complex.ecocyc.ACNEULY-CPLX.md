---
entity_id: "complex.ecocyc.ACNEULY-CPLX"
entity_type: "complex"
name: "N-acetylneuraminate lyase"
source_database: "EcoCyc"
source_id: "ACNEULY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N-acetylneuraminate lyase

`complex.ecocyc.ACNEULY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACNEULY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6L4|protein.P0A6L4]]

## Enriched Summary

EcoCyc complex ACNEULY-CPLX

## Biological Role

Catalyzes RXN0-7390 (reaction.ecocyc.RXN0-7390).

## Annotation

EcoCyc complex ACNEULY-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7390|reaction.ecocyc.RXN0-7390]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6L4|protein.P0A6L4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ACNEULY-CPLX`
- `QSPROTEOME:QS00183207`

## Notes

4*protein.P0A6L4
