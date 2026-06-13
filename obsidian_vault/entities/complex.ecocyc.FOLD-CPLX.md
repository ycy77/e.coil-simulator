---
entity_id: "complex.ecocyc.FOLD-CPLX"
entity_type: "complex"
name: "bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase"
source_database: "EcoCyc"
source_id: "FOLD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase

`complex.ecocyc.FOLD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FOLD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P24186|protein.P24186]]

## Enriched Summary

EcoCyc complex FOLD-CPLX

## Biological Role

Catalyzes METHENYLTHFCYCLOHYDRO-RXN (reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN), METHYLENETHFDEHYDROG-NADP-RXN (reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN).

## Annotation

EcoCyc complex FOLD-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN|reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P24186|protein.P24186]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FOLD-CPLX`
- `QSPROTEOME:QS00199157`

## Notes

2*protein.P24186
