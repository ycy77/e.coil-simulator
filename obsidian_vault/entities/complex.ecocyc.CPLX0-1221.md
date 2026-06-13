---
entity_id: "complex.ecocyc.CPLX0-1221"
entity_type: "complex"
name: "ADP-sugar diphosphatase NudE"
source_database: "EcoCyc"
source_id: "CPLX0-1221"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ADP-sugar diphosphatase NudE

`complex.ecocyc.CPLX0-1221`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1221`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P45799|protein.P45799]]

## Enriched Summary

EcoCyc complex CPLX0-1221

## Biological Role

Catalyzes ADPSUGPPHOSPHAT-RXN (reaction.ecocyc.ADPSUGPPHOSPHAT-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-1221

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ADPSUGPPHOSPHAT-RXN|reaction.ecocyc.ADPSUGPPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P45799|protein.P45799]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1221`
- `QSPROTEOME:QS00183243`

## Notes

2*protein.P45799
