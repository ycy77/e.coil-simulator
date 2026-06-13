---
entity_id: "complex.ecocyc.CPLX0-7990"
entity_type: "complex"
name: "dTDP-4-dehydro-6-deoxy-D-glucose transaminase"
source_database: "EcoCyc"
source_id: "CPLX0-7990"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dTDP-4-dehydro-6-deoxy-D-glucose transaminase

`complex.ecocyc.CPLX0-7990`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7990`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27833|protein.P27833]]

## Enriched Summary

EcoCyc complex CPLX0-7990

## Biological Role

Catalyzes RFFTRANS-RXN (reaction.ecocyc.RFFTRANS-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex CPLX0-7990

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RFFTRANS-RXN|reaction.ecocyc.RFFTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27833|protein.P27833]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7990`
- `QSPROTEOME:QS00196489`

## Notes

4*protein.P27833
