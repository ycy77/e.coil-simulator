---
entity_id: "complex.ecocyc.CPLX0-7760"
entity_type: "complex"
name: "aconitate hydratase A"
source_database: "EcoCyc"
source_id: "CPLX0-7760"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aconitase"
  - "isocitrate hydro-lyase"
  - "aconitate hydratase 1"
---

# aconitate hydratase A

`complex.ecocyc.CPLX0-7760`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7760`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25516|protein.P25516]]

## Enriched Summary

EcoCyc complex CPLX0-7760

## Biological Role

Catalyzes ACONITATEDEHYDR-RXN (reaction.ecocyc.ACONITATEDEHYDR-RXN), cis-aconitate hydratase (reaction.ecocyc.ACONITATEHYDR-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-7760

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACONITATEDEHYDR-RXN|reaction.ecocyc.ACONITATEDEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACONITATEHYDR-RXN|reaction.ecocyc.ACONITATEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P25516|protein.P25516]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7760`
- `QSPROTEOME:QS00049661`

## Notes

2*protein.P25516
