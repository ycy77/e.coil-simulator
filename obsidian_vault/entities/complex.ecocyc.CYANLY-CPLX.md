---
entity_id: "complex.ecocyc.CYANLY-CPLX"
entity_type: "complex"
name: "cyanase"
source_database: "EcoCyc"
source_id: "CYANLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cyanase

`complex.ecocyc.CYANLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CYANLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00816|protein.P00816]]

## Enriched Summary

EcoCyc complex CYANLY-CPLX

## Biological Role

Catalyzes R524-RXN (reaction.ecocyc.R524-RXN).

## Annotation

EcoCyc complex CYANLY-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00816|protein.P00816]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:CYANLY-CPLX`
- `QSPROTEOME:QS00182771`

## Notes

10*protein.P00816
