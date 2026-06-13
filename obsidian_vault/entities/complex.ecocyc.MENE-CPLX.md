---
entity_id: "complex.ecocyc.MENE-CPLX"
entity_type: "complex"
name: "o-succinylbenzoate—CoA ligase"
source_database: "EcoCyc"
source_id: "MENE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# o-succinylbenzoate—CoA ligase

`complex.ecocyc.MENE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MENE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37353|protein.P37353]]

## Enriched Summary

EcoCyc complex MENE-CPLX

## Biological Role

Catalyzes O-SUCCINYLBENZOATE-COA-LIG-RXN (reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex MENE-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN|reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37353|protein.P37353]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:MENE-CPLX`
- `QSPROTEOME:QS00049730`

## Notes

4*protein.P37353
