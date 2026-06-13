---
entity_id: "protein.ecocyc.TSR-GLUME"
entity_type: "complex"
name: "Tsrglu-Me"
source_database: "EcoCyc"
source_id: "TSR-GLUME"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Tsrglu-Me

`protein.ecocyc.TSR-GLUME`

## Static

- Type: `complex`
- Source: `EcoCyc:TSR-GLUME`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A964|protein.P0A964]], [[protein.P07363|protein.P07363]], [[protein.P02942|protein.P02942]]

## Enriched Summary

Represents a signaling complex in which one or more specific Tsr glutamate residues (E297, E304, E311, E493, E502) have been methylated. Represents a signaling complex in which one or more specific Tsr glutamate residues (E297, E304, E311, E493, E502) have been methylated.

## Annotation

Represents a signaling complex in which one or more specific Tsr glutamate residues (E297, E304, E311, E493, E502) have been methylated.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02942|protein.P02942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TSR-GLUME`

## Notes

2*protein.P0A964|2*protein.P07363|12*protein.P02942
