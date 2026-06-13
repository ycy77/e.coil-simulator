---
entity_id: "complex.ecocyc.GLYCEROL-KIN-CPLX"
entity_type: "complex"
name: "glycerol kinase"
source_database: "EcoCyc"
source_id: "GLYCEROL-KIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycerol kinase

`complex.ecocyc.GLYCEROL-KIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYCEROL-KIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6F3|protein.P0A6F3]]

## Enriched Summary

EcoCyc complex GLYCEROL-KIN-CPLX

## Biological Role

Catalyzes GLYCEROL-KIN-RXN (reaction.ecocyc.GLYCEROL-KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex GLYCEROL-KIN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYCEROL-KIN-RXN|reaction.ecocyc.GLYCEROL-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6F3|protein.P0A6F3]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLYCEROL-KIN-CPLX`
- `QSPROTEOME:QS00181789`

## Notes

4*protein.P0A6F3
