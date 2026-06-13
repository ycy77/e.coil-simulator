---
entity_id: "complex.ecocyc.CPLX0-7719"
entity_type: "complex"
name: "quinolinate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7719"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# quinolinate synthase

`complex.ecocyc.CPLX0-7719`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7719`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P11458|protein.P11458]]

## Enriched Summary

EcoCyc complex CPLX0-7719

## Biological Role

Catalyzes QUINOLINATE-SYNTHA-RXN (reaction.ecocyc.QUINOLINATE-SYNTHA-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-7719

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.QUINOLINATE-SYNTHA-RXN|reaction.ecocyc.QUINOLINATE-SYNTHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P11458|protein.P11458]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7719`
- `QSPROTEOME:QS00049645`

## Notes

2*protein.P11458
