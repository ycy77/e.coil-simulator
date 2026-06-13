---
entity_id: "complex.ecocyc.DALADALALIGB-CPLX"
entity_type: "complex"
name: "D-alanine—D-alanine ligase B"
source_database: "EcoCyc"
source_id: "DALADALALIGB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# D-alanine—D-alanine ligase B

`complex.ecocyc.DALADALALIGB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DALADALALIGB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07862|protein.P07862]]

## Enriched Summary

EcoCyc complex DALADALALIGB-CPLX

## Biological Role

Catalyzes DALADALALIG-RXN (reaction.ecocyc.DALADALALIG-RXN).

## Annotation

EcoCyc complex DALADALALIGB-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DALADALALIG-RXN|reaction.ecocyc.DALADALALIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07862|protein.P07862]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DALADALALIGB-CPLX`
- `QSPROTEOME:QS00181821`

## Notes

2*protein.P07862
