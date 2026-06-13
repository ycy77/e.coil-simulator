---
entity_id: "complex.ecocyc.CPLX0-7810"
entity_type: "complex"
name: "heme-containing peroxidase/deferrochelatase"
source_database: "EcoCyc"
source_id: "CPLX0-7810"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "B1019"
  - "YcdB"
---

# heme-containing peroxidase/deferrochelatase

`complex.ecocyc.CPLX0-7810`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7810`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31545|protein.P31545]]

## Enriched Summary

EcoCyc complex CPLX0-7810

## Biological Role

Catalyzes PROTOHEMEFERROCHELAT-RXN (reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN).

## Annotation

EcoCyc complex CPLX0-7810

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN|reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31545|protein.P31545]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7810`
- `QSPROTEOME:QS00206985`

## Notes

2*protein.P31545
