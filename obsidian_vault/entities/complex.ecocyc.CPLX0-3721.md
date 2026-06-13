---
entity_id: "complex.ecocyc.CPLX0-3721"
entity_type: "complex"
name: "ADP-sugar pyrophosphatase"
source_database: "EcoCyc"
source_id: "CPLX0-3721"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ADP-sugar pyrophosphatase

`complex.ecocyc.CPLX0-3721`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3721`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q93K97|protein.Q93K97]]

## Enriched Summary

EcoCyc complex CPLX0-3721

## Biological Role

Catalyzes ADPSUGPPHOSPHAT-RXN (reaction.ecocyc.ADPSUGPPHOSPHAT-RXN), RXN0-7309 (reaction.ecocyc.RXN0-7309). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-3721

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ADPSUGPPHOSPHAT-RXN|reaction.ecocyc.ADPSUGPPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7309|reaction.ecocyc.RXN0-7309]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q93K97|protein.Q93K97]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3721`
- `QSPROTEOME:QS00157409`

## Notes

2*protein.Q93K97
