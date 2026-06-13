---
entity_id: "complex.ecocyc.CPLX0-3001"
entity_type: "complex"
name: "peptidase D"
source_database: "EcoCyc"
source_id: "CPLX0-3001"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "carnosinase"
---

# peptidase D

`complex.ecocyc.CPLX0-3001`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3001`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15288|protein.P15288]]

## Enriched Summary

EcoCyc complex CPLX0-3001

## Biological Role

Catalyzes 3.4.13.18-RXN (reaction.ecocyc.3.4.13.18-RXN), RXN-6622 (reaction.ecocyc.RXN-6622), RXN0-6981 (reaction.ecocyc.RXN0-6981).

## Annotation

EcoCyc complex CPLX0-3001

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.3.4.13.18-RXN|reaction.ecocyc.3.4.13.18-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-6622|reaction.ecocyc.RXN-6622]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6981|reaction.ecocyc.RXN0-6981]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P15288|protein.P15288]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3001`
- `QSPROTEOME:QS00049604`

## Notes

2*protein.P15288
