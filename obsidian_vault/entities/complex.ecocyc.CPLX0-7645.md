---
entity_id: "complex.ecocyc.CPLX0-7645"
entity_type: "complex"
name: "L-fucose mutarotase"
source_database: "EcoCyc"
source_id: "CPLX0-7645"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-fucose mutarotase

`complex.ecocyc.CPLX0-7645`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7645`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEN8|protein.P0AEN8]]

## Enriched Summary

EcoCyc complex CPLX0-7645

## Biological Role

Catalyzes RXN0-5298 (reaction.ecocyc.RXN0-5298), RXN0-5304 (reaction.ecocyc.RXN0-5304).

## Annotation

EcoCyc complex CPLX0-7645

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5298|reaction.ecocyc.RXN0-5298]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5304|reaction.ecocyc.RXN0-5304]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEN8|protein.P0AEN8]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:CPLX0-7645`
- `QSPROTEOME:QS00183249`

## Notes

10*protein.P0AEN8
