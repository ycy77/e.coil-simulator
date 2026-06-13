---
entity_id: "complex.ecocyc.CPLX0-901"
entity_type: "complex"
name: "tRNA adenosine34 deaminase"
source_database: "EcoCyc"
source_id: "CPLX0-901"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA adenosine34 deaminase

`complex.ecocyc.CPLX0-901`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-901`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P68398|protein.P68398]]

## Enriched Summary

EcoCyc complex CPLX0-901

## Biological Role

Catalyzes RXN0-1081 (reaction.ecocyc.RXN0-1081). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex CPLX0-901

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1081|reaction.ecocyc.RXN0-1081]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P68398|protein.P68398]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-901`
- `QSPROTEOME:QS00182051`

## Notes

2*protein.P68398
