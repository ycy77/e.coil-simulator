---
entity_id: "complex.ecocyc.GSAAMINOTRANS-CPLX"
entity_type: "complex"
name: "glutamate-1-semialdehyde 2,1-aminomutase"
source_database: "EcoCyc"
source_id: "GSAAMINOTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate-1-semialdehyde 2,1-aminomutase

`complex.ecocyc.GSAAMINOTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GSAAMINOTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23893|protein.P23893]]

## Enriched Summary

EcoCyc complex GSAAMINOTRANS-CPLX

## Biological Role

Catalyzes GSAAMINOTRANS-RXN (reaction.ecocyc.GSAAMINOTRANS-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GSAAMINOTRANS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GSAAMINOTRANS-RXN|reaction.ecocyc.GSAAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23893|protein.P23893]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GSAAMINOTRANS-CPLX`
- `QSPROTEOME:QS00049723`

## Notes

2*protein.P23893
