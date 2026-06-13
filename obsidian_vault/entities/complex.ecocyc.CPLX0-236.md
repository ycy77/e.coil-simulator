---
entity_id: "complex.ecocyc.CPLX0-236"
entity_type: "complex"
name: "arylamine N-acetyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-236"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# arylamine N-acetyltransferase

`complex.ecocyc.CPLX0-236`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-236`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77567|protein.P77567]]

## Enriched Summary

EcoCyc complex CPLX0-236

## Biological Role

Catalyzes 2.3.1.118-RXN (reaction.ecocyc.2.3.1.118-RXN), ARYLAMINE-N-ACETYLTRANSFERASE-RXN (reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN).

## Annotation

EcoCyc complex CPLX0-236

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.118-RXN|reaction.ecocyc.2.3.1.118-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN|reaction.ecocyc.ARYLAMINE-N-ACETYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77567|protein.P77567]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-236`
- `QSPROTEOME:QS00049585`

## Notes

2*protein.P77567
