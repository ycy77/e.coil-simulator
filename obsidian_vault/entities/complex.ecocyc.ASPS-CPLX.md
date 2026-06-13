---
entity_id: "complex.ecocyc.ASPS-CPLX"
entity_type: "complex"
name: "aspartate—tRNA ligase"
source_database: "EcoCyc"
source_id: "ASPS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aspartyl tRNA Synthetase"
---

# aspartate—tRNA ligase

`complex.ecocyc.ASPS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P21889|protein.P21889]]

## Enriched Summary

EcoCyc complex ASPS-CPLX

## Biological Role

Catalyzes ASPARTATE--TRNA-LIGASE-RXN (reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN), RXN-23928 (reaction.ecocyc.RXN-23928).

## Annotation

EcoCyc complex ASPS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN|reaction.ecocyc.ASPARTATE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23928|reaction.ecocyc.RXN-23928]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P21889|protein.P21889]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASPS-CPLX`
- `QSPROTEOME:QS00049573`

## Notes

2*protein.P21889
