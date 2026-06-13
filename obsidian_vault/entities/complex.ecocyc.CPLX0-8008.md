---
entity_id: "complex.ecocyc.CPLX0-8008"
entity_type: "complex"
name: "UDP-N-acetylglucosamine 2-epimerase"
source_database: "EcoCyc"
source_id: "CPLX0-8008"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-N-acetylglucosamine 2-epimerase

`complex.ecocyc.CPLX0-8008`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8008`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27828|protein.P27828]]

## Enriched Summary

EcoCyc complex CPLX0-8008

## Biological Role

Catalyzes UDPGLCNACEPIM-RXN (reaction.ecocyc.UDPGLCNACEPIM-RXN).

## Annotation

EcoCyc complex CPLX0-8008

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPGLCNACEPIM-RXN|reaction.ecocyc.UDPGLCNACEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P27828|protein.P27828]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8008`
- `QSPROTEOME:QS00181525`

## Notes

2*protein.P27828
