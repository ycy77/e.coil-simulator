---
entity_id: "complex.ecocyc.GCVP-CPLX"
entity_type: "complex"
name: "glycine decarboxylase"
source_database: "EcoCyc"
source_id: "GCVP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycine decarboxylase

`complex.ecocyc.GCVP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GCVP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33195|protein.P33195]]

## Enriched Summary

EcoCyc complex GCVP-CPLX

## Biological Role

Catalyzes GCVP-RXN (reaction.ecocyc.GCVP-RXN). Component of glycine cleavage system (complex.ecocyc.GCVMULTI-CPLX). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GCVP-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GCVP-RXN|reaction.ecocyc.GCVP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.GCVMULTI-CPLX|complex.ecocyc.GCVMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P33195|protein.P33195]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GCVP-CPLX`
- `QSPROTEOME:QS00196219`

## Notes

2*protein.P33195
