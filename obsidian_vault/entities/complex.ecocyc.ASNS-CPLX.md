---
entity_id: "complex.ecocyc.ASNS-CPLX"
entity_type: "complex"
name: "asparagine—tRNA ligase"
source_database: "EcoCyc"
source_id: "ASNS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# asparagine—tRNA ligase

`complex.ecocyc.ASNS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASNS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8M0|protein.P0A8M0]]

## Enriched Summary

EcoCyc complex ASNS-CPLX

## Biological Role

Catalyzes ASPARAGINE--TRNA-LIGASE-RXN (reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN).

## Annotation

EcoCyc complex ASNS-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN|reaction.ecocyc.ASPARAGINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8M0|protein.P0A8M0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASNS-CPLX`
- `QSPROTEOME:QS00049571`

## Notes

2*protein.P0A8M0
