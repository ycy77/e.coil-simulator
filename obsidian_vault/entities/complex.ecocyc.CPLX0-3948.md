---
entity_id: "complex.ecocyc.CPLX0-3948"
entity_type: "complex"
name: "inosine/xanthosine triphosphatase"
source_database: "EcoCyc"
source_id: "CPLX0-3948"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# inosine/xanthosine triphosphatase

`complex.ecocyc.CPLX0-3948`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3948`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39411|protein.P39411]]

## Enriched Summary

EcoCyc complex CPLX0-3948

## Biological Role

Catalyzes RXN0-5073 (reaction.ecocyc.RXN0-5073), RXN0-5074 (reaction.ecocyc.RXN0-5074). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-3948

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5073|reaction.ecocyc.RXN0-5073]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5074|reaction.ecocyc.RXN0-5074]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39411|protein.P39411]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3948`
- `QSPROTEOME:QS00181775`

## Notes

2*protein.P39411
