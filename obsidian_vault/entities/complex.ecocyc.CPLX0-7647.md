---
entity_id: "complex.ecocyc.CPLX0-7647"
entity_type: "complex"
name: "ribokinase"
source_database: "EcoCyc"
source_id: "CPLX0-7647"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribokinase

`complex.ecocyc.CPLX0-7647`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7647`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9J6|protein.P0A9J6]]

## Enriched Summary

EcoCyc complex CPLX0-7647

## Biological Role

Catalyzes RIBOKIN-RXN (reaction.ecocyc.RIBOKIN-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7647

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RIBOKIN-RXN|reaction.ecocyc.RIBOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9J6|protein.P0A9J6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7647`
- `QSPROTEOME:QS00157687`

## Notes

2*protein.P0A9J6
