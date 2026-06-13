---
entity_id: "complex.ecocyc.DGTPTRIPHYDRO-CPLX"
entity_type: "complex"
name: "dGTP triphosphohydrolase"
source_database: "EcoCyc"
source_id: "DGTPTRIPHYDRO-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dGTP triphosphohydrolase

`complex.ecocyc.DGTPTRIPHYDRO-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DGTPTRIPHYDRO-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15723|protein.P15723]]

## Enriched Summary

EcoCyc complex DGTPTRIPHYDRO-CPLX

## Biological Role

Catalyzes DGTPTRIPHYDRO-RXN (reaction.ecocyc.DGTPTRIPHYDRO-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex DGTPTRIPHYDRO-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DGTPTRIPHYDRO-RXN|reaction.ecocyc.DGTPTRIPHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P15723|protein.P15723]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:DGTPTRIPHYDRO-CPLX`
- `QSPROTEOME:QS00181867`

## Notes

6*protein.P15723
