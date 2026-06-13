---
entity_id: "complex.ecocyc.CPLX0-7741"
entity_type: "complex"
name: "methylmalonyl-CoA mutase"
source_database: "EcoCyc"
source_id: "CPLX0-7741"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methylmalonyl-CoA mutase

`complex.ecocyc.CPLX0-7741`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7741`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27253|protein.P27253]]

## Enriched Summary

EcoCyc complex CPLX0-7741

## Biological Role

Catalyzes METHYLMALONYL-COA-MUT-RXN (reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN). Bound by Cobamide coenzyme (molecule.C00194).

## Annotation

EcoCyc complex CPLX0-7741

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN|reaction.ecocyc.METHYLMALONYL-COA-MUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27253|protein.P27253]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7741`
- `QSPROTEOME:QS00049653`

## Notes

2*protein.P27253
