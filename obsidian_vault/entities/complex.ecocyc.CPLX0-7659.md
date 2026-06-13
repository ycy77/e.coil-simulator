---
entity_id: "complex.ecocyc.CPLX0-7659"
entity_type: "complex"
name: "fused diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase"
source_database: "EcoCyc"
source_id: "CPLX0-7659"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase

`complex.ecocyc.CPLX0-7659`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7659`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25539|protein.P25539]]

## Enriched Summary

EcoCyc complex CPLX0-7659

## Biological Role

Catalyzes RIBOFLAVINSYNDEAM-RXN (reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN), RIBOFLAVINSYNREDUC-RXN (reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN).

## Annotation

EcoCyc complex CPLX0-7659

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN|reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN|reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P25539|protein.P25539]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7659`
- `QSPROTEOME:QS00181951`

## Notes

2*protein.P25539
