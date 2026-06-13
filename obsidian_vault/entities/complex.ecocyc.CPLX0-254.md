---
entity_id: "complex.ecocyc.CPLX0-254"
entity_type: "complex"
name: "methylmalonyl-CoA decarboxylase"
source_database: "EcoCyc"
source_id: "CPLX0-254"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methylmalonyl-CoA decarboxylase

`complex.ecocyc.CPLX0-254`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-254`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P52045|protein.P52045]]

## Enriched Summary

EcoCyc complex CPLX0-254

## Biological Role

Catalyzes RXN0-310 (reaction.ecocyc.RXN0-310).

## Annotation

EcoCyc complex CPLX0-254

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-310|reaction.ecocyc.RXN0-310]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P52045|protein.P52045]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-254`
- `QSPROTEOME:QS00195257`

## Notes

6*protein.P52045
