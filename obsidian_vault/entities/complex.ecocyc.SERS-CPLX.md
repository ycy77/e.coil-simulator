---
entity_id: "complex.ecocyc.SERS-CPLX"
entity_type: "complex"
name: "serine—tRNA ligase"
source_database: "EcoCyc"
source_id: "SERS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# serine—tRNA ligase

`complex.ecocyc.SERS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SERS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8L1|protein.P0A8L1]]

## Enriched Summary

EcoCyc complex SERS-CPLX

## Biological Role

Catalyzes RXN0-2161 (reaction.ecocyc.RXN0-2161), SERINE--TRNA-LIGASE-RXN (reaction.ecocyc.SERINE--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex SERS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2161|reaction.ecocyc.RXN0-2161]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SERINE--TRNA-LIGASE-RXN|reaction.ecocyc.SERINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8L1|protein.P0A8L1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SERS-CPLX`
- `QSPROTEOME:QS00195693`

## Notes

2*protein.P0A8L1
