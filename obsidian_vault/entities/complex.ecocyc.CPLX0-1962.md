---
entity_id: "complex.ecocyc.CPLX0-1962"
entity_type: "complex"
name: "3-hydroxy acid dehydrogenase YdfG"
source_database: "EcoCyc"
source_id: "CPLX0-1962"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Serine dehydrogenase"
  - "SerDH"
  - "L-allo-threonine dehydrogenase"
---

# 3-hydroxy acid dehydrogenase YdfG

`complex.ecocyc.CPLX0-1962`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1962`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39831|protein.P39831]]

## Enriched Summary

EcoCyc complex CPLX0-1962

## Biological Role

Catalyzes RXN-16000 (reaction.ecocyc.RXN-16000), RXN-8974 (reaction.ecocyc.RXN-8974), RXN0-2201 (reaction.ecocyc.RXN0-2201).

## Annotation

EcoCyc complex CPLX0-1962

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16000|reaction.ecocyc.RXN-16000]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8974|reaction.ecocyc.RXN-8974]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2201|reaction.ecocyc.RXN0-2201]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P39831|protein.P39831]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-1962`
- `QSPROTEOME:QS00183133`

## Notes

4*protein.P39831
