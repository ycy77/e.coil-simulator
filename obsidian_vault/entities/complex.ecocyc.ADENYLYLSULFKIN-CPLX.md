---
entity_id: "complex.ecocyc.ADENYLYLSULFKIN-CPLX"
entity_type: "complex"
name: "adenylyl-sulfate kinase"
source_database: "EcoCyc"
source_id: "ADENYLYLSULFKIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# adenylyl-sulfate kinase

`complex.ecocyc.ADENYLYLSULFKIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ADENYLYLSULFKIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6J1|protein.P0A6J1]]

## Enriched Summary

EcoCyc complex ADENYLYLSULFKIN-CPLX

## Biological Role

Catalyzes ADENYLYLSULFKIN-RXN (reaction.ecocyc.ADENYLYLSULFKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex ADENYLYLSULFKIN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ADENYLYLSULFKIN-RXN|reaction.ecocyc.ADENYLYLSULFKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6J1|protein.P0A6J1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ADENYLYLSULFKIN-CPLX`
- `QSPROTEOME:QS00049540`

## Notes

2*protein.P0A6J1
