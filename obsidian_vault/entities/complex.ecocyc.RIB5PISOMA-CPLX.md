---
entity_id: "complex.ecocyc.RIB5PISOMA-CPLX"
entity_type: "complex"
name: "ribose-5-phosphate isomerase A"
source_database: "EcoCyc"
source_id: "RIB5PISOMA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribose-5-phosphate isomerase A

`complex.ecocyc.RIB5PISOMA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIB5PISOMA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7Z0|protein.P0A7Z0]]

## Enriched Summary

EcoCyc complex RIB5PISOMA-CPLX

## Biological Role

Catalyzes RIB5PISOM-RXN (reaction.ecocyc.RIB5PISOM-RXN).

## Annotation

EcoCyc complex RIB5PISOMA-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RIB5PISOM-RXN|reaction.ecocyc.RIB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A7Z0|protein.P0A7Z0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIB5PISOMA-CPLX`
- `QSPROTEOME:QS00158521`

## Notes

2*protein.P0A7Z0
