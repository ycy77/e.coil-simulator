---
entity_id: "complex.ecocyc.CPLX0-3954"
entity_type: "complex"
name: "S-formylglutathione hydrolase / S-lactoylglutathione hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-3954"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# S-formylglutathione hydrolase / S-lactoylglutathione hydrolase

`complex.ecocyc.CPLX0-3954`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3954`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33018|protein.P33018]]

## Enriched Summary

EcoCyc complex CPLX0-3954

## Biological Role

Catalyzes GLYOXII-RXN (reaction.ecocyc.GLYOXII-RXN), S-FORMYLGLUTATHIONE-HYDROLASE-RXN (reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN).

## Annotation

EcoCyc complex CPLX0-3954

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN|reaction.ecocyc.S-FORMYLGLUTATHIONE-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P33018|protein.P33018]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3954`
- `QSPROTEOME:QS00049619`

## Notes

4*protein.P33018
