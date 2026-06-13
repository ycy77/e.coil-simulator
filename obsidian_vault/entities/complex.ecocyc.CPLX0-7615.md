---
entity_id: "complex.ecocyc.CPLX0-7615"
entity_type: "complex"
name: "α-dehydro-β-deoxy-D-glucarate aldolase"
source_database: "EcoCyc"
source_id: "CPLX0-7615"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# α-dehydro-β-deoxy-D-glucarate aldolase

`complex.ecocyc.CPLX0-7615`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7615`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23522|protein.P23522]]

## Enriched Summary

EcoCyc complex CPLX0-7615

## Biological Role

Catalyzes KDGALDOL-RXN (reaction.ecocyc.KDGALDOL-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7615

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23522|protein.P23522]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7615`
- `QSPROTEOME:QS00183229`

## Notes

6*protein.P23522
