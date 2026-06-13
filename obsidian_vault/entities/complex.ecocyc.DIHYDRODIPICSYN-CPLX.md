---
entity_id: "complex.ecocyc.DIHYDRODIPICSYN-CPLX"
entity_type: "complex"
name: "4-hydroxy-tetrahydrodipicolinate synthase"
source_database: "EcoCyc"
source_id: "DIHYDRODIPICSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-hydroxy-tetrahydrodipicolinate synthase

`complex.ecocyc.DIHYDRODIPICSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIHYDRODIPICSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6L2|protein.P0A6L2]]

## Enriched Summary

EcoCyc complex DIHYDRODIPICSYN-CPLX

## Biological Role

Catalyzes DIHYDRODIPICSYN-RXN (reaction.ecocyc.DIHYDRODIPICSYN-RXN).

## Annotation

EcoCyc complex DIHYDRODIPICSYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIHYDRODIPICSYN-RXN|reaction.ecocyc.DIHYDRODIPICSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6L2|protein.P0A6L2]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:DIHYDRODIPICSYN-CPLX`
- `QSPROTEOME:QS00181535`

## Notes

4*protein.P0A6L2
