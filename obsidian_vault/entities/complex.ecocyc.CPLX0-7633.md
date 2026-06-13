---
entity_id: "complex.ecocyc.CPLX0-7633"
entity_type: "complex"
name: "L-fuculose-phosphate aldolase"
source_database: "EcoCyc"
source_id: "CPLX0-7633"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-fuculose-phosphate aldolase

`complex.ecocyc.CPLX0-7633`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7633`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB87|protein.P0AB87]]

## Enriched Summary

EcoCyc complex CPLX0-7633

## Biological Role

Catalyzes DARABALDOL-RXN (reaction.ecocyc.DARABALDOL-RXN), FUCPALDOL-RXN (reaction.ecocyc.FUCPALDOL-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex CPLX0-7633

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DARABALDOL-RXN|reaction.ecocyc.DARABALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FUCPALDOL-RXN|reaction.ecocyc.FUCPALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AB87|protein.P0AB87]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7633`
- `QSPROTEOME:QS00181725`

## Notes

4*protein.P0AB87
