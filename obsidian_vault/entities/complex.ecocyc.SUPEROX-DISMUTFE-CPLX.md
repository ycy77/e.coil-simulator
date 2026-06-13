---
entity_id: "complex.ecocyc.SUPEROX-DISMUTFE-CPLX"
entity_type: "complex"
name: "superoxide dismutase (Fe)"
source_database: "EcoCyc"
source_id: "SUPEROX-DISMUTFE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# superoxide dismutase (Fe)

`complex.ecocyc.SUPEROX-DISMUTFE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SUPEROX-DISMUTFE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGD3|protein.P0AGD3]]

## Enriched Summary

EcoCyc complex SUPEROX-DISMUTFE-CPLX

## Biological Role

Catalyzes SUPEROX-DISMUT-RXN (reaction.ecocyc.SUPEROX-DISMUT-RXN). Bound by Fe3+ (molecule.C14819).

## Annotation

EcoCyc complex SUPEROX-DISMUTFE-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUPEROX-DISMUT-RXN|reaction.ecocyc.SUPEROX-DISMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AGD3|protein.P0AGD3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SUPEROX-DISMUTFE-CPLX`
- `QSPROTEOME:QS00200453`

## Notes

2*protein.P0AGD3
