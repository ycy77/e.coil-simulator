---
entity_id: "complex.ecocyc.CPLX0-3927"
entity_type: "complex"
name: "regulatory ATPase RavA"
source_database: "EcoCyc"
source_id: "CPLX0-3927"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# regulatory ATPase RavA

`complex.ecocyc.CPLX0-3927`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3927`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P31473|protein.P31473]]

## Enriched Summary

EcoCyc complex CPLX0-3927

## Biological Role

Catalyzes RXN0-1061 (reaction.ecocyc.RXN0-1061).

## Annotation

EcoCyc complex CPLX0-3927

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1061|reaction.ecocyc.RXN0-1061]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31473|protein.P31473]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-3927`
- `QSPROTEOME:QS00182775`

## Notes

6*protein.P31473
