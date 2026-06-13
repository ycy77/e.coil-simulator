---
entity_id: "complex.ecocyc.ORNDECARBOXDEG-CPLX"
entity_type: "complex"
name: "inducible ornithine decarboxylase"
source_database: "EcoCyc"
source_id: "ORNDECARBOXDEG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# inducible ornithine decarboxylase

`complex.ecocyc.ORNDECARBOXDEG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ORNDECARBOXDEG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P24169|protein.P24169]]

## Enriched Summary

EcoCyc complex ORNDECARBOXDEG-CPLX

## Biological Role

Catalyzes ORNDECARBOX-RXN (reaction.ecocyc.ORNDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex ORNDECARBOXDEG-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ORNDECARBOX-RXN|reaction.ecocyc.ORNDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P24169|protein.P24169]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ORNDECARBOXDEG-CPLX`
- `QSPROTEOME:QS00049738`

## Notes

2*protein.P24169
