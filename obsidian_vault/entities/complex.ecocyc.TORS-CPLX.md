---
entity_id: "complex.ecocyc.TORS-CPLX"
entity_type: "complex"
name: "sensor histidine kinase TorS"
source_database: "EcoCyc"
source_id: "TORS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase TorS

`complex.ecocyc.TORS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TORS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39453|protein.P39453]]

## Enriched Summary

EcoCyc complex TORS-CPLX

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN). Component of TorTS signaling complex (complex.ecocyc.CPLX0-11302).

## Annotation

EcoCyc complex TORS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-11302|complex.ecocyc.CPLX0-11302]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P39453|protein.P39453]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TORS-CPLX`
- `QSPROTEOME:QS00049558`

## Notes

2*protein.P39453
