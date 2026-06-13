---
entity_id: "complex.ecocyc.CPLX0-7709"
entity_type: "complex"
name: "glutamate-putrescine ligase"
source_database: "EcoCyc"
source_id: "CPLX0-7709"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate-putrescine ligase

`complex.ecocyc.CPLX0-7709`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7709`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P78061|protein.P78061]]

## Enriched Summary

EcoCyc complex CPLX0-7709

## Biological Role

Catalyzes RXN0-3901 (reaction.ecocyc.RXN0-3901). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7709

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3901|reaction.ecocyc.RXN0-3901]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P78061|protein.P78061]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-7709`

## Notes

12*protein.P78061
