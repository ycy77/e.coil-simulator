---
entity_id: "complex.ecocyc.CARBODEHYDRAT-CPLX"
entity_type: "complex"
name: "carbonic anhydrase 1"
source_database: "EcoCyc"
source_id: "CARBODEHYDRAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbonic anhydrase 1

`complex.ecocyc.CARBODEHYDRAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CARBODEHYDRAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P0ABE9|protein.P0ABE9]]

## Enriched Summary

EcoCyc complex CARBODEHYDRAT-CPLX

## Biological Role

Catalyzes RXN0-5224 (reaction.ecocyc.RXN0-5224). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex CARBODEHYDRAT-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5224|reaction.ecocyc.RXN0-5224]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABE9|protein.P0ABE9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CARBODEHYDRAT-CPLX`
- `QSPROTEOME:QS00049578`

## Notes

2*protein.P0ABE9
