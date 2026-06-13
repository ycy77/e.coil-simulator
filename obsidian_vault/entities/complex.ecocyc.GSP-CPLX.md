---
entity_id: "complex.ecocyc.GSP-CPLX"
entity_type: "complex"
name: "fused glutathionylspermidine amidase / glutathionylspermidine synthetase"
source_database: "EcoCyc"
source_id: "GSP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused glutathionylspermidine amidase / glutathionylspermidine synthetase

`complex.ecocyc.GSP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GSP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AES0|protein.P0AES0]]

## Enriched Summary

EcoCyc complex GSP-CPLX

## Biological Role

Catalyzes GSPAMID-RXN (reaction.ecocyc.GSPAMID-RXN), GSPSYN-RXN (reaction.ecocyc.GSPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex GSP-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GSPAMID-RXN|reaction.ecocyc.GSPAMID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GSPSYN-RXN|reaction.ecocyc.GSPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AES0|protein.P0AES0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GSP-CPLX`
- `QSPROTEOME:QS00181857`

## Notes

2*protein.P0AES0
