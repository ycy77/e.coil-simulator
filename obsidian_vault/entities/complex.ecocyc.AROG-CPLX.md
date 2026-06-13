---
entity_id: "complex.ecocyc.AROG-CPLX"
entity_type: "complex"
name: "3-deoxy-7-phosphoheptulonate synthase"
source_database: "EcoCyc"
source_id: "AROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-deoxy-7-phosphoheptulonate synthase

`complex.ecocyc.AROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB91|protein.P0AB91]]

## Enriched Summary

EcoCyc complex AROG-CPLX

## Biological Role

Catalyzes DAHPSYN-RXN (reaction.ecocyc.DAHPSYN-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

EcoCyc complex AROG-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AB91|protein.P0AB91]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:AROG-CPLX`
- `QSPROTEOME:QS00182673`

## Notes

4*protein.P0AB91
