---
entity_id: "complex.ecocyc.HOLO-ACP-SYNTH-CPLX"
entity_type: "complex"
name: "holo-[acyl-carrier-protein] synthase"
source_database: "EcoCyc"
source_id: "HOLO-ACP-SYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# holo-[acyl-carrier-protein] synthase

`complex.ecocyc.HOLO-ACP-SYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HOLO-ACP-SYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P24224|protein.P24224]]

## Enriched Summary

EcoCyc complex HOLO-ACP-SYNTH-CPLX

## Biological Role

Catalyzes HOLO-ACP-SYNTH-RXN (reaction.ecocyc.HOLO-ACP-SYNTH-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex HOLO-ACP-SYNTH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HOLO-ACP-SYNTH-RXN|reaction.ecocyc.HOLO-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P24224|protein.P24224]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HOLO-ACP-SYNTH-CPLX`
- `QSPROTEOME:QS00049724`

## Notes

2*protein.P24224
