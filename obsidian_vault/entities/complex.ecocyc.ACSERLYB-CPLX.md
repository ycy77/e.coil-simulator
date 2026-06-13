---
entity_id: "complex.ecocyc.ACSERLYB-CPLX"
entity_type: "complex"
name: "cysteine synthase B"
source_database: "EcoCyc"
source_id: "ACSERLYB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cysteine synthase B

`complex.ecocyc.ACSERLYB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACSERLYB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16703|protein.P16703]]

## Enriched Summary

EcoCyc complex ACSERLYB-CPLX

## Biological Role

Catalyzes ACSERLY-RXN (reaction.ecocyc.ACSERLY-RXN), LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN), SULFOCYS-RXN (reaction.ecocyc.SULFOCYS-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex ACSERLYB-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SULFOCYS-RXN|reaction.ecocyc.SULFOCYS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P16703|protein.P16703]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACSERLYB-CPLX`
- `QSPROTEOME:QS00181717`

## Notes

2*protein.P16703
