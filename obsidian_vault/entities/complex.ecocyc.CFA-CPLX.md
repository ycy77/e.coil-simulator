---
entity_id: "complex.ecocyc.CFA-CPLX"
entity_type: "complex"
name: "cyclopropane fatty acyl phospholipid synthase"
source_database: "EcoCyc"
source_id: "CFA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cyclopropane fatty acyl phospholipid synthase

`complex.ecocyc.CFA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CFA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9H7|protein.P0A9H7]]

## Enriched Summary

EcoCyc complex CFA-CPLX

## Biological Role

Catalyzes 2.1.1.79-RXN (reaction.ecocyc.2.1.1.79-RXN). Bound by HCO3- (molecule.C00288).

## Annotation

EcoCyc complex CFA-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.79-RXN|reaction.ecocyc.2.1.1.79-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9H7|protein.P0A9H7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CFA-CPLX`
- `QSPROTEOME:QS00183149`

## Notes

2*protein.P0A9H7
