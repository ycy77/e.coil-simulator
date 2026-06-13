---
entity_id: "complex.ecocyc.CPLX0-225"
entity_type: "complex"
name: "FMNH2-dependent alkanesulfonate monooxygenase"
source_database: "EcoCyc"
source_id: "CPLX0-225"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# FMNH2-dependent alkanesulfonate monooxygenase

`complex.ecocyc.CPLX0-225`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-225`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P80645|protein.P80645]]

## Enriched Summary

EcoCyc complex CPLX0-225

## Biological Role

Catalyzes RXN-13418 (reaction.ecocyc.RXN-13418), RXN0-280 (reaction.ecocyc.RXN0-280).

## Annotation

EcoCyc complex CPLX0-225

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-13418|reaction.ecocyc.RXN-13418]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-280|reaction.ecocyc.RXN0-280]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P80645|protein.P80645]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-225`
- `QSPROTEOME:QS00193621`

## Notes

4*protein.P80645
