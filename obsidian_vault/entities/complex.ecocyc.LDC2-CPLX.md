---
entity_id: "complex.ecocyc.LDC2-CPLX"
entity_type: "complex"
name: "lysine decarboxylase 2"
source_database: "EcoCyc"
source_id: "LDC2-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LDC2"
---

# lysine decarboxylase 2

`complex.ecocyc.LDC2-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LDC2-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P52095|protein.P52095]]

## Enriched Summary

EcoCyc complex LDC2-CPLX

## Biological Role

Catalyzes LYSDECARBOX-RXN (reaction.ecocyc.LYSDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex LDC2-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LYSDECARBOX-RXN|reaction.ecocyc.LYSDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P52095|protein.P52095]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:LDC2-CPLX`

## Notes

10*protein.P52095
