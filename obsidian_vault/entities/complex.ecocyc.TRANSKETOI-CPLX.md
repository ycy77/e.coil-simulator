---
entity_id: "complex.ecocyc.TRANSKETOI-CPLX"
entity_type: "complex"
name: "transketolase 1"
source_database: "EcoCyc"
source_id: "TRANSKETOI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# transketolase 1

`complex.ecocyc.TRANSKETOI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANSKETOI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27302|protein.P27302]]

## Enriched Summary

EcoCyc complex TRANSKETOI-CPLX

## Biological Role

Catalyzes 1TRANSKETO-RXN (reaction.ecocyc.1TRANSKETO-RXN), 2TRANSKETO-RXN (reaction.ecocyc.2TRANSKETO-RXN). Bound by Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex TRANSKETOI-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.2TRANSKETO-RXN|reaction.ecocyc.2TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27302|protein.P27302]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRANSKETOI-CPLX`
- `QSPROTEOME:QS00198911`

## Notes

2*protein.P27302
