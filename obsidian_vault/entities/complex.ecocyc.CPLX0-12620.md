---
entity_id: "complex.ecocyc.CPLX0-12620"
entity_type: "complex"
name: "[Fe-S] cluster biosynthesis chaperone/co-chaperone system"
source_database: "EcoCyc"
source_id: "CPLX0-12620"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# [Fe-S] cluster biosynthesis chaperone/co-chaperone system

`complex.ecocyc.CPLX0-12620`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12620`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6L9|protein.P0A6L9]], [[protein.P0A6Z1|protein.P0A6Z1]]

## Enriched Summary

EcoCyc complex CPLX0-12620

## Biological Role

Catalyzes RXN-25091 (reaction.ecocyc.RXN-25091).

## Annotation

EcoCyc complex CPLX0-12620

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-25091|reaction.ecocyc.RXN-25091]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0A6L9|protein.P0A6L9]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A6Z1|protein.P0A6Z1]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-12620`
- `QSPROTEOME:QS00049488`

## Notes

protein.P0A6L9|protein.P0A6Z1
