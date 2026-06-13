---
entity_id: "complex.ecocyc.ENVZ-CPLX"
entity_type: "complex"
name: "sensor histidine kinase EnvZ"
source_database: "EcoCyc"
source_id: "ENVZ-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase EnvZ

`complex.ecocyc.ENVZ-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENVZ-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AEJ4|protein.P0AEJ4]]

## Enriched Summary

EcoCyc complex ENVZ-CPLX

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

EcoCyc complex ENVZ-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEJ4|protein.P0AEJ4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ENVZ-CPLX`
- `QSPROTEOME:QS00049704`

## Notes

2*protein.P0AEJ4
