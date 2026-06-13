---
entity_id: "complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX"
entity_type: "complex"
name: "glucosamine-6-phosphate deaminase"
source_database: "EcoCyc"
source_id: "GLUCOSAMINE-6-P-DEAMIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucosamine-6-phosphate deaminase

`complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUCOSAMINE-6-P-DEAMIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A759|protein.P0A759]]

## Enriched Summary

EcoCyc complex GLUCOSAMINE-6-P-DEAMIN-CPLX

## Biological Role

Catalyzes GLUCOSAMINE-6-P-DEAMIN-RXN (reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN).

## Annotation

EcoCyc complex GLUCOSAMINE-6-P-DEAMIN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A759|protein.P0A759]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:GLUCOSAMINE-6-P-DEAMIN-CPLX`
- `QSPROTEOME:QS00181895`

## Notes

6*protein.P0A759
