---
entity_id: "complex.ecocyc.QOR-CPLX"
entity_type: "complex"
name: "putative quinone oxidoreductase 1"
source_database: "EcoCyc"
source_id: "QOR-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative quinone oxidoreductase 1

`complex.ecocyc.QOR-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:QOR-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28304|protein.P28304]]

## Enriched Summary

EcoCyc complex QOR-CPLX

## Biological Role

Catalyzes QOR-RXN (reaction.ecocyc.QOR-RXN).

## Annotation

EcoCyc complex QOR-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.QOR-RXN|reaction.ecocyc.QOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P28304|protein.P28304]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:QOR-CPLX`
- `QSPROTEOME:QS00183293`

## Notes

2*protein.P28304
