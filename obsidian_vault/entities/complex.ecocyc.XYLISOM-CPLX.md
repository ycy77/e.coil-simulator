---
entity_id: "complex.ecocyc.XYLISOM-CPLX"
entity_type: "complex"
name: "xylose isomerase"
source_database: "EcoCyc"
source_id: "XYLISOM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# xylose isomerase

`complex.ecocyc.XYLISOM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:XYLISOM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00944|protein.P00944]]

## Enriched Summary

EcoCyc complex XYLISOM-CPLX

## Biological Role

Catalyzes XYLISOM-RXN (reaction.ecocyc.XYLISOM-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex XYLISOM-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.XYLISOM-RXN|reaction.ecocyc.XYLISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00944|protein.P00944]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:XYLISOM-CPLX`
- `QSPROTEOME:QS00197019`

## Notes

2*protein.P00944
