---
entity_id: "complex.ecocyc.CPLX0-7466"
entity_type: "complex"
name: "xylulokinase"
source_database: "EcoCyc"
source_id: "CPLX0-7466"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# xylulokinase

`complex.ecocyc.CPLX0-7466`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7466`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09099|protein.P09099]]

## Enriched Summary

EcoCyc complex CPLX0-7466

## Biological Role

Catalyzes RXN0-382 (reaction.ecocyc.RXN0-382), XYLULOKIN-RXN (reaction.ecocyc.XYLULOKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7466

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-382|reaction.ecocyc.RXN0-382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.XYLULOKIN-RXN|reaction.ecocyc.XYLULOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09099|protein.P09099]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7466`
- `QSPROTEOME:QS00181575`

## Notes

2*protein.P09099
