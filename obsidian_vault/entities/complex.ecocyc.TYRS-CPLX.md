---
entity_id: "complex.ecocyc.TYRS-CPLX"
entity_type: "complex"
name: "tyrosine—tRNA ligase"
source_database: "EcoCyc"
source_id: "TYRS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tyrosine—tRNA ligase

`complex.ecocyc.TYRS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TYRS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGJ9|protein.P0AGJ9]]

## Enriched Summary

EcoCyc complex TYRS-CPLX

## Biological Role

Catalyzes RXN-23936 (reaction.ecocyc.RXN-23936), TYROSINE--TRNA-LIGASE-RXN (reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN).

## Annotation

EcoCyc complex TYRS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-23936|reaction.ecocyc.RXN-23936]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN|reaction.ecocyc.TYROSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGJ9|protein.P0AGJ9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TYRS-CPLX`
- `QSPROTEOME:QS00195923`

## Notes

2*protein.P0AGJ9
