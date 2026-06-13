---
entity_id: "complex.ecocyc.QUINOPRIBOTRANS-CPLX"
entity_type: "complex"
name: "quinolinate phosphoribosyltransferase (decarboxylating)"
source_database: "EcoCyc"
source_id: "QUINOPRIBOTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# quinolinate phosphoribosyltransferase (decarboxylating)

`complex.ecocyc.QUINOPRIBOTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:QUINOPRIBOTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30011|protein.P30011]]

## Enriched Summary

EcoCyc complex QUINOPRIBOTRANS-CPLX

## Biological Role

Catalyzes QUINOPRIBOTRANS-RXN (reaction.ecocyc.QUINOPRIBOTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex QUINOPRIBOTRANS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.QUINOPRIBOTRANS-RXN|reaction.ecocyc.QUINOPRIBOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P30011|protein.P30011]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:QUINOPRIBOTRANS-CPLX`
- `QSPROTEOME:QS00049547`

## Notes

2*protein.P30011
