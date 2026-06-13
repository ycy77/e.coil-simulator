---
entity_id: "complex.ecocyc.CPLX0-8238"
entity_type: "complex"
name: "putative menaquinol-cytochrome c reductase NrfCD"
source_database: "EcoCyc"
source_id: "CPLX0-8238"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative menaquinol-cytochrome c reductase NrfCD

`complex.ecocyc.CPLX0-8238`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8238`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32709|protein.P32709]], [[protein.P0AAK7|protein.P0AAK7]]

## Enriched Summary

EcoCyc complex CPLX0-8238

## Biological Role

Catalyzes RXN-18604 (reaction.ecocyc.RXN-18604). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-8238

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-18604|reaction.ecocyc.RXN-18604]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AAK7|protein.P0AAK7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P32709|protein.P32709]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8238`
- `QSPROTEOME:QS00049465`

## Notes

1*protein.P32709|1*protein.P0AAK7
