---
entity_id: "complex.ecocyc.CPLX-171"
entity_type: "complex"
name: "hydroxypyruvate isomerase"
source_database: "EcoCyc"
source_id: "CPLX-171"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# hydroxypyruvate isomerase

`complex.ecocyc.CPLX-171`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-171`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30147|protein.P30147]]

## Enriched Summary

EcoCyc complex CPLX-171

## Biological Role

Catalyzes RXN0-305 (reaction.ecocyc.RXN0-305).

## Annotation

EcoCyc complex CPLX-171

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-305|reaction.ecocyc.RXN0-305]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P30147|protein.P30147]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX-171`
- `QSPROTEOME:QS00049693`

## Notes

2*protein.P30147
