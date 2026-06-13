---
entity_id: "complex.ecocyc.CPLX0-7683"
entity_type: "complex"
name: "sulfoquinovose isomerase"
source_database: "EcoCyc"
source_id: "CPLX0-7683"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sulfoquinovose isomerase

`complex.ecocyc.CPLX0-7683`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7683`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32140|protein.P32140]]

## Enriched Summary

EcoCyc complex CPLX0-7683

## Biological Role

Catalyzes MANNOSE-ISOMERASE-RXN (reaction.ecocyc.MANNOSE-ISOMERASE-RXN), RXN-15296 (reaction.ecocyc.RXN-15296).

## Annotation

EcoCyc complex CPLX0-7683

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MANNOSE-ISOMERASE-RXN|reaction.ecocyc.MANNOSE-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-15296|reaction.ecocyc.RXN-15296]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P32140|protein.P32140]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7683`
- `QSPROTEOME:QS00188833`

## Notes

6*protein.P32140
