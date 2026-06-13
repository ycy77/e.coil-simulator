---
entity_id: "complex.ecocyc.1-PFK"
entity_type: "complex"
name: "1-phosphofructokinase"
source_database: "EcoCyc"
source_id: "1-PFK"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 1-phosphofructokinase

`complex.ecocyc.1-PFK`

## Static

- Type: `complex`
- Source: `EcoCyc:1-PFK`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEW9|protein.P0AEW9]]

## Enriched Summary

EcoCyc complex 1-PFK

## Biological Role

Catalyzes 1PFRUCTPHOSN-RXN (reaction.ecocyc.1PFRUCTPHOSN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex 1-PFK

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1PFRUCTPHOSN-RXN|reaction.ecocyc.1PFRUCTPHOSN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEW9|protein.P0AEW9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:1-PFK`
- `QSPROTEOME:QS00049537`

## Notes

2*protein.P0AEW9
