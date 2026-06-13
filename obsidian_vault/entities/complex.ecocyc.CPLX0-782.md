---
entity_id: "complex.ecocyc.CPLX0-782"
entity_type: "complex"
name: "lipoyl synthase"
source_database: "EcoCyc"
source_id: "CPLX0-782"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lipoyl synthase

`complex.ecocyc.CPLX0-782`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-782`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60716|protein.P60716]]

## Enriched Summary

EcoCyc complex CPLX0-782

## Biological Role

Catalyzes RXN0-949 (reaction.ecocyc.RXN0-949). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-782

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-949|reaction.ecocyc.RXN0-949]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60716|protein.P60716]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-782`
- `QSPROTEOME:QS00049407`

## Notes

2*protein.P60716
