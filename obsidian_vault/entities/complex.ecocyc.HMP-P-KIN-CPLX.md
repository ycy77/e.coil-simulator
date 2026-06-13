---
entity_id: "complex.ecocyc.HMP-P-KIN-CPLX"
entity_type: "complex"
name: "hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase"
source_database: "EcoCyc"
source_id: "HMP-P-KIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "hydroxymethylpyrimidine kinase 2"
---

# hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase

`complex.ecocyc.HMP-P-KIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HMP-P-KIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76422|protein.P76422]]

## Enriched Summary

EcoCyc complex HMP-P-KIN-CPLX

## Biological Role

Catalyzes OHMETPYRKIN-RXN (reaction.ecocyc.OHMETPYRKIN-RXN), PYRIMSYN3-RXN (reaction.ecocyc.PYRIMSYN3-RXN).

## Annotation

EcoCyc complex HMP-P-KIN-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.OHMETPYRKIN-RXN|reaction.ecocyc.OHMETPYRKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRIMSYN3-RXN|reaction.ecocyc.PYRIMSYN3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76422|protein.P76422]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HMP-P-KIN-CPLX`
- `QSPROTEOME:QS00181925`

## Notes

2*protein.P76422
