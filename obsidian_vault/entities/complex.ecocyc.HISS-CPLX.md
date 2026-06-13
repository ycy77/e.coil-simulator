---
entity_id: "complex.ecocyc.HISS-CPLX"
entity_type: "complex"
name: "histidine—tRNA ligase"
source_database: "EcoCyc"
source_id: "HISS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# histidine—tRNA ligase

`complex.ecocyc.HISS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HISS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60906|protein.P60906]]

## Enriched Summary

EcoCyc complex HISS-CPLX

## Biological Role

Catalyzes HISTIDINE--TRNA-LIGASE-RXN (reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex HISS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN|reaction.ecocyc.HISTIDINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60906|protein.P60906]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HISS-CPLX`
- `QSPROTEOME:QS00233924`

## Notes

2*protein.P60906
