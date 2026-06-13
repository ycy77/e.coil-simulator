---
entity_id: "protein.ecocyc.TAR-GLN"
entity_type: "complex"
name: "Targln"
source_database: "EcoCyc"
source_id: "TAR-GLN"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Targln

`protein.ecocyc.TAR-GLN`

## Static

- Type: `complex`
- Source: `EcoCyc:TAR-GLN`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P07017|protein.P07017]]

## Enriched Summary

Represents a signaling complex that contains unmodified Tar receptors Represents a signaling complex that contains unmodified Tar receptors

## Annotation

Represents a signaling complex that contains unmodified Tar receptors

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P07017|protein.P07017]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAR-GLN`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P07017
