---
entity_id: "complex.ecocyc.CPLX0-3936"
entity_type: "complex"
name: "dihydroneopterin aldolase"
source_database: "EcoCyc"
source_id: "CPLX0-3936"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dihydroneopterin aldolase

`complex.ecocyc.CPLX0-3936`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3936`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC16|protein.P0AC16]]

## Enriched Summary

EcoCyc complex CPLX0-3936

## Biological Role

Catalyzes H2NEOPTERINALDOL-RXN (reaction.ecocyc.H2NEOPTERINALDOL-RXN), RXN-10856 (reaction.ecocyc.RXN-10856).

## Annotation

EcoCyc complex CPLX0-3936

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.H2NEOPTERINALDOL-RXN|reaction.ecocyc.H2NEOPTERINALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10856|reaction.ecocyc.RXN-10856]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AC16|protein.P0AC16]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:CPLX0-3936`
- `QSPROTEOME:QS00183187`

## Notes

8*protein.P0AC16
