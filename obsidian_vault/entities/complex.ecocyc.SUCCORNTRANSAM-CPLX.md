---
entity_id: "complex.ecocyc.SUCCORNTRANSAM-CPLX"
entity_type: "complex"
name: "succinylornithine transaminase"
source_database: "EcoCyc"
source_id: "SUCCORNTRANSAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# succinylornithine transaminase

`complex.ecocyc.SUCCORNTRANSAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SUCCORNTRANSAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77581|protein.P77581]]

## Enriched Summary

EcoCyc complex SUCCORNTRANSAM-CPLX

## Biological Role

Catalyzes ACETYLORNTRANSAM-RXN (reaction.ecocyc.ACETYLORNTRANSAM-RXN), SUCCORNTRANSAM-RXN (reaction.ecocyc.SUCCORNTRANSAM-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex SUCCORNTRANSAM-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCORNTRANSAM-RXN|reaction.ecocyc.SUCCORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77581|protein.P77581]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SUCCORNTRANSAM-CPLX`
- `QSPROTEOME:QS00198969`

## Notes

2*protein.P77581
