---
entity_id: "complex.ecocyc.DIHYDROPICRED-CPLX"
entity_type: "complex"
name: "4-hydroxy-tetrahydrodipicolinate reductase"
source_database: "EcoCyc"
source_id: "DIHYDROPICRED-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-hydroxy-tetrahydrodipicolinate reductase

`complex.ecocyc.DIHYDROPICRED-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIHYDROPICRED-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P04036|protein.P04036]]

## Enriched Summary

EcoCyc complex DIHYDROPICRED-CPLX

## Biological Role

Catalyzes RXN-14014 (reaction.ecocyc.RXN-14014).

## Annotation

EcoCyc complex DIHYDROPICRED-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14014|reaction.ecocyc.RXN-14014]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P04036|protein.P04036]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:DIHYDROPICRED-CPLX`
- `QSPROTEOME:QS00198895`

## Notes

4*protein.P04036
