---
entity_id: "complex.ecocyc.NAD-SYNTH-CPLX"
entity_type: "complex"
name: "NH3-dependent NAD+ synthetase"
source_database: "EcoCyc"
source_id: "NAD-SYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NH3-dependent NAD+ synthetase

`complex.ecocyc.NAD-SYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NAD-SYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P18843|protein.P18843]]

## Enriched Summary

EcoCyc complex NAD-SYNTH-CPLX

## Biological Role

Catalyzes NAD-SYNTH-NH3-RXN (reaction.ecocyc.NAD-SYNTH-NH3-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex NAD-SYNTH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NAD-SYNTH-NH3-RXN|reaction.ecocyc.NAD-SYNTH-NH3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P18843|protein.P18843]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:NAD-SYNTH-CPLX`
- `QSPROTEOME:QS00181739`

## Notes

2*protein.P18843
