---
entity_id: "complex.ecocyc.CPLX0-3941"
entity_type: "complex"
name: "phenylacetyl-CoA thioesterase"
source_database: "EcoCyc"
source_id: "CPLX0-3941"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phenylacetyl-CoA thioesterase

`complex.ecocyc.CPLX0-3941`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3941`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76084|protein.P76084]]

## Enriched Summary

EcoCyc complex CPLX0-3941

## Biological Role

Catalyzes RXN0-5065 (reaction.ecocyc.RXN0-5065), RXN0-7104 (reaction.ecocyc.RXN0-7104).

## Annotation

EcoCyc complex CPLX0-3941

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5065|reaction.ecocyc.RXN0-5065]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7104|reaction.ecocyc.RXN0-7104]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76084|protein.P76084]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3941`
- `QSPROTEOME:QS00181749`

## Notes

4*protein.P76084
