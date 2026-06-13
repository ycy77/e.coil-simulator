---
entity_id: "complex.ecocyc.TSR-CPLX"
entity_type: "complex"
name: "chemotaxis signaling complex core unit - serine sensing"
source_database: "EcoCyc"
source_id: "TSR-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MCP-I signaling complex"
---

# chemotaxis signaling complex core unit - serine sensing

`complex.ecocyc.TSR-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TSR-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A964|protein.P0A964]], [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]], [[complex.ecocyc.CPLX0-8103|complex.ecocyc.CPLX0-8103]]

## Enriched Summary

EcoCyc complex TSR-CPLX

## Annotation

EcoCyc complex TSR-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-8103|complex.ecocyc.CPLX0-8103]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P02942|protein.P02942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TSR-CPLX`
- `PDB:6S1K`
- `PDB:8C5V`

## Notes

2*protein.P0A964|1*complex.ecocyc.CHEA-CPLX|6*complex.ecocyc.CPLX0-8103
