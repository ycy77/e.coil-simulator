---
entity_id: "complex.ecocyc.DCTP-DEAM-CPLX"
entity_type: "complex"
name: "dCTP deaminase"
source_database: "EcoCyc"
source_id: "DCTP-DEAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dCTP deaminase

`complex.ecocyc.DCTP-DEAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DCTP-DEAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28248|protein.P28248]]

## Enriched Summary

EcoCyc complex DCTP-DEAM-CPLX

## Biological Role

Catalyzes DCTP-DEAM-RXN (reaction.ecocyc.DCTP-DEAM-RXN).

## Annotation

EcoCyc complex DCTP-DEAM-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DCTP-DEAM-RXN|reaction.ecocyc.DCTP-DEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P28248|protein.P28248]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:DCTP-DEAM-CPLX`
- `QSPROTEOME:QS00188827`

## Notes

3*protein.P28248
