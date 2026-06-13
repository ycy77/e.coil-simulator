---
entity_id: "protein.ecocyc.TRG-GLUME"
entity_type: "complex"
name: "Trgglu-Me"
source_database: "EcoCyc"
source_id: "TRG-GLUME"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Trgglu-Me

`protein.ecocyc.TRG-GLUME`

## Static

- Type: `complex`
- Source: `EcoCyc:TRG-GLUME`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P05704|protein.P05704]]

## Enriched Summary

Represents a signaling complex in which one or more specific Trg glutamate residues (E305, E312, E319, E501, E510) have been methylated. Represents a signaling complex in which one or more specific Trg glutamate residues (E305, E312, E319, E501, E510) have been methylated.

## Annotation

Represents a signaling complex in which one or more specific Trg glutamate residues (E305, E312, E319, E501, E510) have been methylated.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P05704|protein.P05704]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRG-GLUME`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P05704
