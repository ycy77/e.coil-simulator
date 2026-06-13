---
entity_id: "complex.ecocyc.PROS-CPLX"
entity_type: "complex"
name: "proline—tRNA ligase"
source_database: "EcoCyc"
source_id: "PROS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# proline—tRNA ligase

`complex.ecocyc.PROS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PROS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16659|protein.P16659]]

## Enriched Summary

EcoCyc complex PROS-CPLX

## Biological Role

Catalyzes PROLINE--TRNA-LIGASE-RXN (reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN), RXN-21072 (reaction.ecocyc.RXN-21072), RXN-23940 (reaction.ecocyc.RXN-23940), RXN-23942 (reaction.ecocyc.RXN-23942).

## Annotation

EcoCyc complex PROS-CPLX

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN|reaction.ecocyc.PROLINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21072|reaction.ecocyc.RXN-21072]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23940|reaction.ecocyc.RXN-23940]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23942|reaction.ecocyc.RXN-23942]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P16659|protein.P16659]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PROS-CPLX`
- `QSPROTEOME:QS00049517`

## Notes

2*protein.P16659
