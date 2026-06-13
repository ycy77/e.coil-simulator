---
entity_id: "complex.ecocyc.CPLX0-321"
entity_type: "complex"
name: "pyridoxine 5'-phosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-321"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyridoxine 5'-phosphate synthase

`complex.ecocyc.CPLX0-321`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-321`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A794|protein.P0A794]]

## Enriched Summary

EcoCyc complex CPLX0-321

## Biological Role

Catalyzes PDXJ-RXN (reaction.ecocyc.PDXJ-RXN).

## Annotation

EcoCyc complex CPLX0-321

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PDXJ-RXN|reaction.ecocyc.PDXJ-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A794|protein.P0A794]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:CPLX0-321`
- `QSPROTEOME:QS00181779`

## Notes

8*protein.P0A794
