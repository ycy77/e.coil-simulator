---
entity_id: "complex.ecocyc.FUMARASE-C"
entity_type: "complex"
name: "fumarase C"
source_database: "EcoCyc"
source_id: "FUMARASE-C"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fumarase C

`complex.ecocyc.FUMARASE-C`

## Static

- Type: `complex`
- Source: `EcoCyc:FUMARASE-C`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05042|protein.P05042]]

## Enriched Summary

EcoCyc complex FUMARASE-C

## Biological Role

Catalyzes FUMHYDR-RXN (reaction.ecocyc.FUMHYDR-RXN).

## Annotation

EcoCyc complex FUMARASE-C

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P05042|protein.P05042]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:FUMARASE-C`
- `QSPROTEOME:QS00183123`

## Notes

4*protein.P05042
