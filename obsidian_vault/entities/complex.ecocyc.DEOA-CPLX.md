---
entity_id: "complex.ecocyc.DEOA-CPLX"
entity_type: "complex"
name: "thymidine phosphorylase / uracil phosphorylase"
source_database: "EcoCyc"
source_id: "DEOA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thymidine phosphorylase / uracil phosphorylase

`complex.ecocyc.DEOA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DEOA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07650|protein.P07650]]

## Enriched Summary

EcoCyc complex DEOA-CPLX

## Biological Role

Catalyzes THYM-PHOSPH-RXN (reaction.ecocyc.THYM-PHOSPH-RXN), URA-PHOSPH-RXN (reaction.ecocyc.URA-PHOSPH-RXN).

## Annotation

EcoCyc complex DEOA-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.THYM-PHOSPH-RXN|reaction.ecocyc.THYM-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URA-PHOSPH-RXN|reaction.ecocyc.URA-PHOSPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07650|protein.P07650]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DEOA-CPLX`
- `QSPROTEOME:QS00196569`

## Notes

2*protein.P07650
