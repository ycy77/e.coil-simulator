---
entity_id: "complex.ecocyc.AROH-CPLX"
entity_type: "complex"
name: "3-deoxy-7-phosphoheptulonate synthase"
source_database: "EcoCyc"
source_id: "AROH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-deoxy-7-phosphoheptulonate synthase

`complex.ecocyc.AROH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AROH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00887|protein.P00887]]

## Enriched Summary

EcoCyc complex AROH-CPLX

## Biological Role

Catalyzes DAHPSYN-RXN (reaction.ecocyc.DAHPSYN-RXN).

## Annotation

EcoCyc complex AROH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00887|protein.P00887]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AROH-CPLX`
- `QSPROTEOME:QS00049570`

## Notes

2*protein.P00887
