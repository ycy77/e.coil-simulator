---
entity_id: "complex.ecocyc.PPX-CPLX"
entity_type: "complex"
name: "exopolyphosphatase"
source_database: "EcoCyc"
source_id: "PPX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# exopolyphosphatase

`complex.ecocyc.PPX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PPX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFL6|protein.P0AFL6]]

## Enriched Summary

EcoCyc complex PPX-CPLX

## Biological Role

Catalyzes EXOPOLYPHOSPHATASE-RXN (reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PPX-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN|reaction.ecocyc.EXOPOLYPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AFL6|protein.P0AFL6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PPX-CPLX`
- `QSPROTEOME:QS00166879`

## Notes

2*protein.P0AFL6
