---
entity_id: "complex.ecocyc.CPLX0-7693"
entity_type: "complex"
name: "FMN dependent NADH:quinone oxidoreductase"
source_database: "EcoCyc"
source_id: "CPLX0-7693"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# FMN dependent NADH:quinone oxidoreductase

`complex.ecocyc.CPLX0-7693`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7693`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P41407|protein.P41407]]

## Enriched Summary

EcoCyc complex CPLX0-7693

## Biological Role

Catalyzes RXN0-5375 (reaction.ecocyc.RXN0-5375), RXN0-6722 (reaction.ecocyc.RXN0-6722). Bound by FMN (molecule.C00061).

## Annotation

EcoCyc complex CPLX0-7693

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5375|reaction.ecocyc.RXN0-5375]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6722|reaction.ecocyc.RXN0-6722]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P41407|protein.P41407]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7693`
- `QSPROTEOME:QS00183201`

## Notes

2*protein.P41407
