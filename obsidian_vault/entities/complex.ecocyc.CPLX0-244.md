---
entity_id: "complex.ecocyc.CPLX0-244"
entity_type: "complex"
name: "NADPH-dependent nitroreductase / NADPH-dependent quinone reductase"
source_database: "EcoCyc"
source_id: "CPLX0-244"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADPH-dependent nitroreductase / NADPH-dependent quinone reductase

`complex.ecocyc.CPLX0-244`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-244`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17117|protein.P17117]]

## Enriched Summary

EcoCyc complex CPLX0-244

## Biological Role

Catalyzes R303-RXN (reaction.ecocyc.R303-RXN), RXN0-7385 (reaction.ecocyc.RXN0-7385). Bound by FMN (molecule.C00061).

## Annotation

EcoCyc complex CPLX0-244

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.R303-RXN|reaction.ecocyc.R303-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7385|reaction.ecocyc.RXN0-7385]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P17117|protein.P17117]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-244`
- `QSPROTEOME:QS00183181`

## Notes

2*protein.P17117
