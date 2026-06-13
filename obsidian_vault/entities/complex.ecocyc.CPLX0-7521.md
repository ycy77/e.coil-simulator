---
entity_id: "complex.ecocyc.CPLX0-7521"
entity_type: "complex"
name: "carbonic anhydrase 2"
source_database: "EcoCyc"
source_id: "CPLX0-7521"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbonic anhydrase 2

`complex.ecocyc.CPLX0-7521`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7521`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P61517|protein.P61517]]

## Enriched Summary

EcoCyc complex CPLX0-7521

## Biological Role

Catalyzes RXN0-5224 (reaction.ecocyc.RXN0-5224). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex CPLX0-7521

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5224|reaction.ecocyc.RXN0-5224]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P61517|protein.P61517]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7521`
- `QSPROTEOME:QS00181533`

## Notes

4*protein.P61517
