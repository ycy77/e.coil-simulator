---
entity_id: "complex.ecocyc.UPPSYN-CPLX"
entity_type: "complex"
name: "ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific]"
source_database: "EcoCyc"
source_id: "UPPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ditrans,polycis-undecaprenyl-diphosphate synthase [(2E,6E)-farnesyl-diphosphate specific]

`complex.ecocyc.UPPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UPPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60472|protein.P60472]]

## Enriched Summary

EcoCyc complex UPPSYN-CPLX

## Biological Role

Catalyzes RXN-8999 (reaction.ecocyc.RXN-8999). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex UPPSYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8999|reaction.ecocyc.RXN-8999]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60472|protein.P60472]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:UPPSYN-CPLX`
- `QSPROTEOME:QS00196449`

## Notes

2*protein.P60472
