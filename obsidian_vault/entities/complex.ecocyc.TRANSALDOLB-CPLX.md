---
entity_id: "complex.ecocyc.TRANSALDOLB-CPLX"
entity_type: "complex"
name: "transaldolase B"
source_database: "EcoCyc"
source_id: "TRANSALDOLB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# transaldolase B

`complex.ecocyc.TRANSALDOLB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANSALDOLB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A870|protein.P0A870]]

## Enriched Summary

EcoCyc complex TRANSALDOLB-CPLX

## Biological Role

Catalyzes TRANSALDOL-RXN (reaction.ecocyc.TRANSALDOL-RXN).

## Annotation

EcoCyc complex TRANSALDOLB-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A870|protein.P0A870]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRANSALDOLB-CPLX`
- `QSPROTEOME:QS00196885`

## Notes

2*protein.P0A870
