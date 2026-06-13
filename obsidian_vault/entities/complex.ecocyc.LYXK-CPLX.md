---
entity_id: "complex.ecocyc.LYXK-CPLX"
entity_type: "complex"
name: "L-xylulose kinase"
source_database: "EcoCyc"
source_id: "LYXK-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-xylulose kinase

`complex.ecocyc.LYXK-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LYXK-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37677|protein.P37677]]

## Enriched Summary

EcoCyc complex LYXK-CPLX

## Biological Role

Catalyzes LYXK-RXN (reaction.ecocyc.LYXK-RXN), RXN0-704 (reaction.ecocyc.RXN0-704). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex LYXK-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.LYXK-RXN|reaction.ecocyc.LYXK-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-704|reaction.ecocyc.RXN0-704]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37677|protein.P37677]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:LYXK-CPLX`
- `QSPROTEOME:QS00049729`

## Notes

2*protein.P37677
