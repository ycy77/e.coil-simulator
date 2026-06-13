---
entity_id: "complex.ecocyc.KDO-8PPHOSPHAT-CPLX"
entity_type: "complex"
name: "3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC"
source_database: "EcoCyc"
source_id: "KDO-8PPHOSPHAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC

`complex.ecocyc.KDO-8PPHOSPHAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:KDO-8PPHOSPHAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABZ4|protein.P0ABZ4]]

## Enriched Summary

EcoCyc complex KDO-8PPHOSPHAT-CPLX

## Biological Role

Catalyzes KDO-8PPHOSPHAT-RXN (reaction.ecocyc.KDO-8PPHOSPHAT-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex KDO-8PPHOSPHAT-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.KDO-8PPHOSPHAT-RXN|reaction.ecocyc.KDO-8PPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABZ4|protein.P0ABZ4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:KDO-8PPHOSPHAT-CPLX`
- `QSPROTEOME:QS00195939`

## Notes

4*protein.P0ABZ4
