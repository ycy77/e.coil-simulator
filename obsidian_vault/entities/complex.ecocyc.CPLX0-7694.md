---
entity_id: "complex.ecocyc.CPLX0-7694"
entity_type: "complex"
name: "glutaminase 1"
source_database: "EcoCyc"
source_id: "CPLX0-7694"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutaminase 1

`complex.ecocyc.CPLX0-7694`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7694`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77454|protein.P77454]]

## Enriched Summary

EcoCyc complex CPLX0-7694

## Biological Role

Catalyzes GLUTAMIN-RXN (reaction.ecocyc.GLUTAMIN-RXN).

## Annotation

EcoCyc complex CPLX0-7694

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMIN-RXN|reaction.ecocyc.GLUTAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77454|protein.P77454]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7694`
- `QSPROTEOME:QS00192175`

## Notes

4*protein.P77454
