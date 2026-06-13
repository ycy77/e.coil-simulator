---
entity_id: "complex.ecocyc.TRPS-CPLX"
entity_type: "complex"
name: "tryptophan—tRNA ligase"
source_database: "EcoCyc"
source_id: "TRPS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tryptophan—tRNA ligase

`complex.ecocyc.TRPS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRPS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00954|protein.P00954]]

## Enriched Summary

EcoCyc complex TRPS-CPLX

## Biological Role

Catalyzes RXN-23933 (reaction.ecocyc.RXN-23933), TRYPTOPHAN--TRNA-LIGASE-RXN (reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex TRPS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-23933|reaction.ecocyc.RXN-23933]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN|reaction.ecocyc.TRYPTOPHAN--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00954|protein.P00954]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRPS-CPLX`
- `QSPROTEOME:QS00049560`

## Notes

2*protein.P00954
