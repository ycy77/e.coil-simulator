---
entity_id: "protein.ecocyc.TAP-GLN"
entity_type: "complex"
name: "Tapgln"
source_database: "EcoCyc"
source_id: "TAP-GLN"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Tapgln

`protein.ecocyc.TAP-GLN`

## Static

- Type: `complex`
- Source: `EcoCyc:TAP-GLN`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P07018|protein.P07018]]

## Enriched Summary

Represents a signaling complex that contains unmodified Tap receptors Represents a signaling complex that contains unmodified Tap receptors

## Annotation

Represents a signaling complex that contains unmodified Tap receptors

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P07018|protein.P07018]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAP-GLN`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P07018
