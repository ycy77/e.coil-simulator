---
entity_id: "complex.ecocyc.AROF-CPLX"
entity_type: "complex"
name: "3-deoxy-7-phosphoheptulonate synthase"
source_database: "EcoCyc"
source_id: "AROF-CPLX"
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

`complex.ecocyc.AROF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AROF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00888|protein.P00888]]

## Enriched Summary

EcoCyc complex AROF-CPLX

## Biological Role

Catalyzes DAHPSYN-RXN (reaction.ecocyc.DAHPSYN-RXN).

## Annotation

EcoCyc complex AROF-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00888|protein.P00888]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AROF-CPLX`
- `QSPROTEOME:QS00182669`

## Notes

2*protein.P00888
