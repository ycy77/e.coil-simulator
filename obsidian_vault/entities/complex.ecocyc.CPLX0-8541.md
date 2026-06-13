---
entity_id: "complex.ecocyc.CPLX0-8541"
entity_type: "complex"
name: "ferric catecholate outer membrane transport complex I"
source_database: "EcoCyc"
source_id: "CPLX0-8541"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "iron-catecholate outer membrane transport complex I"
---

# ferric catecholate outer membrane transport complex I

`complex.ecocyc.CPLX0-8541`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8541`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75780|protein.P75780]], [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]]

## Enriched Summary

EcoCyc complex CPLX0-8541

## Biological Role

Catalyzes TRANS-RXN-1598 (reaction.ecocyc.TRANS-RXN-1598). Transports hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-8541

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1598|reaction.ecocyc.TRANS-RXN-1598]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P75780|protein.P75780]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-8541`
- `QSPROTEOME:QS00203833`

## Notes

protein.P75780|complex.ecocyc.CPLX0-1923
