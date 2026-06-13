---
entity_id: "complex.ecocyc.CPLX0-7728"
entity_type: "complex"
name: "tRNA pseudouridine38-40 synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7728"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "tRNA pseudouridine synthase I"
---

# tRNA pseudouridine38-40 synthase

`complex.ecocyc.CPLX0-7728`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7728`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07649|protein.P07649]]

## Enriched Summary

EcoCyc complex CPLX0-7728

## Biological Role

Catalyzes TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN (reaction.ecocyc.TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN).

## Annotation

EcoCyc complex CPLX0-7728

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN|reaction.ecocyc.TRNA-PSEUDOURIDINE-SYNTHASE-I-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07649|protein.P07649]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7728`
- `QSPROTEOME:QS00182015`

## Notes

2*protein.P07649
