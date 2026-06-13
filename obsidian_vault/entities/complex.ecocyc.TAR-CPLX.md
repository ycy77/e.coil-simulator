---
entity_id: "complex.ecocyc.TAR-CPLX"
entity_type: "complex"
name: "chemotaxis signaling complex core unit - aspartate sensing"
source_database: "EcoCyc"
source_id: "TAR-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MCP-II signaling complex"
---

# chemotaxis signaling complex core unit - aspartate sensing

`complex.ecocyc.TAR-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TAR-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]], [[protein.P0A964|protein.P0A964]], [[complex.ecocyc.CPLX0-8102|complex.ecocyc.CPLX0-8102]]

## Enriched Summary

EcoCyc complex TAR-CPLX

## Annotation

EcoCyc complex TAR-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-8102|complex.ecocyc.CPLX0-8102]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P07017|protein.P07017]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAR-CPLX`
- `PDB:6S1K`

## Notes

1*complex.ecocyc.CHEA-CPLX|2*protein.P0A964|6*complex.ecocyc.CPLX0-8102
