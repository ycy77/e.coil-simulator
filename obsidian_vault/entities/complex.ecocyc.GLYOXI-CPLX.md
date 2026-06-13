---
entity_id: "complex.ecocyc.GLYOXI-CPLX"
entity_type: "complex"
name: "lactoylglutathione lyase"
source_database: "EcoCyc"
source_id: "GLYOXI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GLX I"
---

# lactoylglutathione lyase

`complex.ecocyc.GLYOXI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYOXI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC81|protein.P0AC81]]

## Enriched Summary

EcoCyc complex GLYOXI-CPLX

## Biological Role

Catalyzes GLYOXI-RXN (reaction.ecocyc.GLYOXI-RXN). Bound by Nickel(2+) (molecule.C19609).

## Annotation

EcoCyc complex GLYOXI-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYOXI-RXN|reaction.ecocyc.GLYOXI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC81|protein.P0AC81]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYOXI-CPLX`
- `QSPROTEOME:QS00164871`

## Notes

2*protein.P0AC81
