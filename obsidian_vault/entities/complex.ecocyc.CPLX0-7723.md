---
entity_id: "complex.ecocyc.CPLX0-7723"
entity_type: "complex"
name: "2-keto-3-deoxy-L-rhamnonate aldolase"
source_database: "EcoCyc"
source_id: "CPLX0-7723"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-keto-3-deoxy-L-rhamnonate aldolase

`complex.ecocyc.CPLX0-7723`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7723`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76469|protein.P76469]]

## Enriched Summary

EcoCyc complex CPLX0-7723

## Biological Role

Catalyzes RXN0-5433 (reaction.ecocyc.RXN0-5433). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7723

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5433|reaction.ecocyc.RXN0-5433]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76469|protein.P76469]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7723`
- `QSPROTEOME:QS00192349`

## Notes

6*protein.P76469
