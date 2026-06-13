---
entity_id: "complex.ecocyc.CPLX0-1141"
entity_type: "complex"
name: "selenocysteine synthase"
source_database: "EcoCyc"
source_id: "CPLX0-1141"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# selenocysteine synthase

`complex.ecocyc.CPLX0-1141`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1141`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A821|protein.P0A821]]

## Enriched Summary

EcoCyc complex CPLX0-1141

## Biological Role

Catalyzes 2.9.1.1-RXN (reaction.ecocyc.2.9.1.1-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex CPLX0-1141

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.9.1.1-RXN|reaction.ecocyc.2.9.1.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A821|protein.P0A821]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:CPLX0-1141`
- `QSPROTEOME:QS00182005`

## Notes

10*protein.P0A821
