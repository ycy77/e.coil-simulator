---
entity_id: "complex.ecocyc.TAP-CPLX"
entity_type: "complex"
name: "chemotaxis signaling complex core unit - dipeptide sensing"
source_database: "EcoCyc"
source_id: "TAP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MCP-IV chemotaxis signaling complex"
---

# chemotaxis signaling complex core unit - dipeptide sensing

`complex.ecocyc.TAP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TAP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]], [[protein.P0A964|protein.P0A964]], [[complex.ecocyc.CPLX0-8104|complex.ecocyc.CPLX0-8104]]

## Enriched Summary

EcoCyc complex TAP-CPLX

## Annotation

EcoCyc complex TAP-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CHEA-CPLX|complex.ecocyc.CHEA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CPLX0-8104|complex.ecocyc.CPLX0-8104]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P07018|protein.P07018]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAP-CPLX`
- `PDB:6S1K`

## Notes

1*complex.ecocyc.CHEA-CPLX|2*protein.P0A964|6*complex.ecocyc.CPLX0-8104
