---
entity_id: "complex.ecocyc.CPLX0-1021"
entity_type: "complex"
name: "2-methylisocitrate lyase"
source_database: "EcoCyc"
source_id: "CPLX0-1021"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-methylisocitrate lyase

`complex.ecocyc.CPLX0-1021`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1021`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77541|protein.P77541]]

## Enriched Summary

EcoCyc complex CPLX0-1021

## Biological Role

Catalyzes METHYLISOCITRATE-LYASE-RXN (reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-1021

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN|reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77541|protein.P77541]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-1021`
- `QSPROTEOME:QS00183151`

## Notes

4*protein.P77541
