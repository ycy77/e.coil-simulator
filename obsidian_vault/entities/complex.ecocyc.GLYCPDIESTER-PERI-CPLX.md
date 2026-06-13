---
entity_id: "complex.ecocyc.GLYCPDIESTER-PERI-CPLX"
entity_type: "complex"
name: "glycerophosphoryl diester phosphodiesterase, periplasmic"
source_database: "EcoCyc"
source_id: "GLYCPDIESTER-PERI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycerophosphoryl diester phosphodiesterase, periplasmic

`complex.ecocyc.GLYCPDIESTER-PERI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYCPDIESTER-PERI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09394|protein.P09394]]

## Enriched Summary

EcoCyc complex GLYCPDIESTER-PERI-CPLX

## Biological Role

Catalyzes GLYCPDIESTER-RXN (reaction.ecocyc.GLYCPDIESTER-RXN). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Annotation

EcoCyc complex GLYCPDIESTER-PERI-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYCPDIESTER-RXN|reaction.ecocyc.GLYCPDIESTER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09394|protein.P09394]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYCPDIESTER-PERI-CPLX`
- `QSPROTEOME:QS00181687`

## Notes

2*protein.P09394
