---
entity_id: "complex.ecocyc.DIOHBUTANONEPSYN-CPLX"
entity_type: "complex"
name: "3,4-dihydroxy-2-butanone-4-phosphate synthase"
source_database: "EcoCyc"
source_id: "DIOHBUTANONEPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3,4-dihydroxy-2-butanone-4-phosphate synthase

`complex.ecocyc.DIOHBUTANONEPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIOHBUTANONEPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7J0|protein.P0A7J0]]

## Enriched Summary

EcoCyc complex DIOHBUTANONEPSYN-CPLX

## Biological Role

Catalyzes DIOHBUTANONEPSYN-RXN (reaction.ecocyc.DIOHBUTANONEPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex DIOHBUTANONEPSYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIOHBUTANONEPSYN-RXN|reaction.ecocyc.DIOHBUTANONEPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7J0|protein.P0A7J0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DIOHBUTANONEPSYN-CPLX`
- `QSPROTEOME:QS00196475`

## Notes

2*protein.P0A7J0
