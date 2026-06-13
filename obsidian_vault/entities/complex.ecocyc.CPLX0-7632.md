---
entity_id: "complex.ecocyc.CPLX0-7632"
entity_type: "complex"
name: "NAD(P)H:quinone oxidoreductase"
source_database: "EcoCyc"
source_id: "CPLX0-7632"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NAD(P)H:quinone oxidoreductase

`complex.ecocyc.CPLX0-7632`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7632`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8G6|protein.P0A8G6]]

## Enriched Summary

EcoCyc complex CPLX0-7632

## Biological Role

Catalyzes NQOR-RXN (reaction.ecocyc.NQOR-RXN). Bound by FMN (molecule.C00061).

## Annotation

EcoCyc complex CPLX0-7632

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NQOR-RXN|reaction.ecocyc.NQOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8G6|protein.P0A8G6]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7632`
- `QSPROTEOME:QS00183239`

## Notes

4*protein.P0A8G6
