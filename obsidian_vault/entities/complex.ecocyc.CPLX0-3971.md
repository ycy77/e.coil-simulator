---
entity_id: "complex.ecocyc.CPLX0-3971"
entity_type: "complex"
name: "GDP-mannose hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-3971"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GDP-mannose hydrolase

`complex.ecocyc.CPLX0-3971`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3971`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37128|protein.P37128]]

## Enriched Summary

EcoCyc complex CPLX0-3971

## Biological Role

Catalyzes RXN0-5108 (reaction.ecocyc.RXN0-5108). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-3971

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5108|reaction.ecocyc.RXN0-5108]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37128|protein.P37128]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3971`
- `QSPROTEOME:QS00049426`

## Notes

2*protein.P37128
