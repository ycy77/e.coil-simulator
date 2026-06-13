---
entity_id: "complex.ecocyc.CPLX0-7722"
entity_type: "complex"
name: "L-rhamnonate dehydratase"
source_database: "EcoCyc"
source_id: "CPLX0-7722"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-rhamnonate dehydratase

`complex.ecocyc.CPLX0-7722`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7722`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77215|protein.P77215]]

## Enriched Summary

EcoCyc complex CPLX0-7722

## Biological Role

Catalyzes L-RHAMNONATE-DEHYDRATASE-RXN (reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7722

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN|reaction.ecocyc.L-RHAMNONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77215|protein.P77215]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:CPLX0-7722`
- `QSPROTEOME:QS00197313`

## Notes

8*protein.P77215
