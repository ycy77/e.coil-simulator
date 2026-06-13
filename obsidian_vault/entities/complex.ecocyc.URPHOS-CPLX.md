---
entity_id: "complex.ecocyc.URPHOS-CPLX"
entity_type: "complex"
name: "uridine phosphorylase"
source_database: "EcoCyc"
source_id: "URPHOS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# uridine phosphorylase

`complex.ecocyc.URPHOS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:URPHOS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12758|protein.P12758]]

## Enriched Summary

EcoCyc complex URPHOS-CPLX

## Biological Role

Catalyzes URPHOS-RXN (reaction.ecocyc.URPHOS-RXN). Bound by Potassium cation (molecule.C00238).

## Annotation

EcoCyc complex URPHOS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P12758|protein.P12758]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:URPHOS-CPLX`
- `QSPROTEOME:QS00183385`

## Notes

6*protein.P12758
