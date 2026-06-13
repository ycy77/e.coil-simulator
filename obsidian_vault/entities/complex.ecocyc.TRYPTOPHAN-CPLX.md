---
entity_id: "complex.ecocyc.TRYPTOPHAN-CPLX"
entity_type: "complex"
name: "tryptophanase / L-cysteine desulfhydrase"
source_database: "EcoCyc"
source_id: "TRYPTOPHAN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tryptophanase / L-cysteine desulfhydrase

`complex.ecocyc.TRYPTOPHAN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRYPTOPHAN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A853|protein.P0A853]]

## Enriched Summary

EcoCyc complex TRYPTOPHAN-CPLX

## Biological Role

Catalyzes LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN), TRYPTOPHAN-RXN (reaction.ecocyc.TRYPTOPHAN-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex TRYPTOPHAN-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRYPTOPHAN-RXN|reaction.ecocyc.TRYPTOPHAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A853|protein.P0A853]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:TRYPTOPHAN-CPLX`
- `QSPROTEOME:QS00183061`

## Notes

4*protein.P0A853
