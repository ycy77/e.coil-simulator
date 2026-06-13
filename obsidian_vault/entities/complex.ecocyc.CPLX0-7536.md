---
entity_id: "complex.ecocyc.CPLX0-7536"
entity_type: "complex"
name: "FKBP-type peptidyl-prolyl cis-trans isomerase SlyD"
source_database: "EcoCyc"
source_id: "CPLX0-7536"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# FKBP-type peptidyl-prolyl cis-trans isomerase SlyD

`complex.ecocyc.CPLX0-7536`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7536`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9K9|protein.P0A9K9]]

## Enriched Summary

EcoCyc complex CPLX0-7536

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN), RXN-22956 (reaction.ecocyc.RXN-22956).

## Annotation

EcoCyc complex CPLX0-7536

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22956|reaction.ecocyc.RXN-22956]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9K9|protein.P0A9K9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7536`
- `QSPROTEOME:QS00049624`

## Notes

2*protein.P0A9K9
