---
entity_id: "complex.ecocyc.ARCB-CPLX"
entity_type: "complex"
name: "sensor histidine kinase ArcB"
source_database: "EcoCyc"
source_id: "ARCB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ArcB"
---

# sensor histidine kinase ArcB

`complex.ecocyc.ARCB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ARCB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEC3|protein.P0AEC3]]

## Enriched Summary

EcoCyc complex ARCB-CPLX

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

EcoCyc complex ARCB-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEC3|protein.P0AEC3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ARCB-CPLX`
- `QSPROTEOME:QS00049567`

## Notes

2*protein.P0AEC3
