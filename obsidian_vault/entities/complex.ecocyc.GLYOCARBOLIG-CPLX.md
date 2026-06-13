---
entity_id: "complex.ecocyc.GLYOCARBOLIG-CPLX"
entity_type: "complex"
name: "glyoxylate carboligase"
source_database: "EcoCyc"
source_id: "GLYOCARBOLIG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glyoxylate carboligase

`complex.ecocyc.GLYOCARBOLIG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYOCARBOLIG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEP7|protein.P0AEP7]]

## Enriched Summary

EcoCyc complex GLYOCARBOLIG-CPLX

## Biological Role

Catalyzes GLYOCARBOLIG-RXN (reaction.ecocyc.GLYOCARBOLIG-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex GLYOCARBOLIG-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYOCARBOLIG-RXN|reaction.ecocyc.GLYOCARBOLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEP7|protein.P0AEP7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYOCARBOLIG-CPLX`
- `QSPROTEOME:QS00196899`

## Notes

2*protein.P0AEP7
