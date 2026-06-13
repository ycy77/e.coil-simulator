---
entity_id: "complex.ecocyc.CPLX0-3121"
entity_type: "complex"
name: "quinone reductase"
source_database: "EcoCyc"
source_id: "CPLX0-3121"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# quinone reductase

`complex.ecocyc.CPLX0-3121`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3121`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGE6|protein.P0AGE6]]

## Enriched Summary

EcoCyc complex CPLX0-3121

## Biological Role

Catalyzes NQOR-RXN (reaction.ecocyc.NQOR-RXN), RXN0-3381 (reaction.ecocyc.RXN0-3381). Bound by FMN (molecule.C00061).

## Annotation

EcoCyc complex CPLX0-3121

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.NQOR-RXN|reaction.ecocyc.NQOR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3381|reaction.ecocyc.RXN0-3381]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AGE6|protein.P0AGE6]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3121`
- `QSPROTEOME:QS00181991`

## Notes

4*protein.P0AGE6
