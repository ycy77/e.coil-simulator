---
entity_id: "complex.ecocyc.CPLX0-3661"
entity_type: "complex"
name: "fused heptose 7-phosphate kinase/heptose 1-phosphate adenyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-3661"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused heptose 7-phosphate kinase/heptose 1-phosphate adenyltransferase

`complex.ecocyc.CPLX0-3661`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3661`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76658|protein.P76658]]

## Enriched Summary

EcoCyc complex CPLX0-3661

## Biological Role

Catalyzes RXN0-4341 (reaction.ecocyc.RXN0-4341), RXN0-4342 (reaction.ecocyc.RXN0-4342). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-3661

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4341|reaction.ecocyc.RXN0-4341]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4342|reaction.ecocyc.RXN0-4342]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76658|protein.P76658]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3661`
- `QSPROTEOME:QS00049611`

## Notes

2*protein.P76658
