---
entity_id: "complex.ecocyc.CPLX0-1261"
entity_type: "complex"
name: "transketolase 2"
source_database: "EcoCyc"
source_id: "CPLX0-1261"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "TK II"
---

# transketolase 2

`complex.ecocyc.CPLX0-1261`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1261`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33570|protein.P33570]]

## Enriched Summary

EcoCyc complex CPLX0-1261

## Biological Role

Catalyzes 1TRANSKETO-RXN (reaction.ecocyc.1TRANSKETO-RXN), 2TRANSKETO-RXN (reaction.ecocyc.2TRANSKETO-RXN).

## Annotation

EcoCyc complex CPLX0-1261

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.2TRANSKETO-RXN|reaction.ecocyc.2TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P33570|protein.P33570]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1261`

## Notes

protein.P33570
