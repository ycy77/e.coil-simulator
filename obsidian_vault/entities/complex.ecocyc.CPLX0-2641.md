---
entity_id: "complex.ecocyc.CPLX0-2641"
entity_type: "complex"
name: "chaperone protein HtpG"
source_database: "EcoCyc"
source_id: "CPLX0-2641"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# chaperone protein HtpG

`complex.ecocyc.CPLX0-2641`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2641`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6Z3|protein.P0A6Z3]]

## Enriched Summary

EcoCyc complex CPLX0-2641

## Biological Role

Catalyzes RXN0-1061 (reaction.ecocyc.RXN0-1061).

## Annotation

EcoCyc complex CPLX0-2641

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1061|reaction.ecocyc.RXN0-1061]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6Z3|protein.P0A6Z3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2641`
- `QSPROTEOME:QS00196929`

## Notes

2*protein.P0A6Z3
