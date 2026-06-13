---
entity_id: "complex.ecocyc.KDO-8PSYNTH-CPLX"
entity_type: "complex"
name: "3-deoxy-D-manno-octulosonate 8-phosphate synthase"
source_database: "EcoCyc"
source_id: "KDO-8PSYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-deoxy-D-manno-octulosonate 8-phosphate synthase

`complex.ecocyc.KDO-8PSYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:KDO-8PSYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A715|protein.P0A715]]

## Enriched Summary

EcoCyc complex KDO-8PSYNTH-CPLX

## Biological Role

Catalyzes KDO-8PSYNTH-RXN (reaction.ecocyc.KDO-8PSYNTH-RXN).

## Annotation

EcoCyc complex KDO-8PSYNTH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.KDO-8PSYNTH-RXN|reaction.ecocyc.KDO-8PSYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A715|protein.P0A715]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:KDO-8PSYNTH-CPLX`
- `QSPROTEOME:QS00181537`

## Notes

4*protein.P0A715
