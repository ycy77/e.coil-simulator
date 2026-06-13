---
entity_id: "complex.ecocyc.LYSS-CPLX"
entity_type: "complex"
name: "lysine—tRNA ligase, constitutive"
source_database: "EcoCyc"
source_id: "LYSS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lysine—tRNA ligase, constitutive

`complex.ecocyc.LYSS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LYSS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8N3|protein.P0A8N3]]

## Enriched Summary

EcoCyc complex LYSS-CPLX

## Biological Role

Catalyzes LYSINE--TRNA-LIGASE-RXN (reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN).

## Annotation

EcoCyc complex LYSS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN|reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8N3|protein.P0A8N3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:LYSS-CPLX`
- `QSPROTEOME:QS00190123`

## Notes

2*protein.P0A8N3
