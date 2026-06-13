---
entity_id: "complex.ecocyc.SUPEROX-DISMUTMN-CPLX"
entity_type: "complex"
name: "superoxide dismutase (Mn)"
source_database: "EcoCyc"
source_id: "SUPEROX-DISMUTMN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# superoxide dismutase (Mn)

`complex.ecocyc.SUPEROX-DISMUTMN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SUPEROX-DISMUTMN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00448|protein.P00448]]

## Enriched Summary

EcoCyc complex SUPEROX-DISMUTMN-CPLX

## Biological Role

Catalyzes SUPEROX-DISMUT-RXN (reaction.ecocyc.SUPEROX-DISMUT-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex SUPEROX-DISMUTMN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUPEROX-DISMUT-RXN|reaction.ecocyc.SUPEROX-DISMUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00448|protein.P00448]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SUPEROX-DISMUTMN-CPLX`
- `QSPROTEOME:QS00188907`

## Notes

2*protein.P00448
