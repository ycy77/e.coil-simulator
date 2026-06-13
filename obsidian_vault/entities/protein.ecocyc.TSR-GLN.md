---
entity_id: "protein.ecocyc.TSR-GLN"
entity_type: "complex"
name: "Tsrgln"
source_database: "EcoCyc"
source_id: "TSR-GLN"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Tsrgln

`protein.ecocyc.TSR-GLN`

## Static

- Type: `complex`
- Source: `EcoCyc:TSR-GLN`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A964|protein.P0A964]], [[protein.P07363|protein.P07363]], [[protein.P02942|protein.P02942]]

## Enriched Summary

Represents a signaling complex which contains unmodified Tsr receptors. Represents a signaling complex which contains unmodified Tsr receptors.

## Annotation

Represents a signaling complex which contains unmodified Tsr receptors.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02942|protein.P02942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TSR-GLN`

## Notes

2*protein.P0A964|2*protein.P07363|12*protein.P02942
