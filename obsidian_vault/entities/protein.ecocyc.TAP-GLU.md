---
entity_id: "protein.ecocyc.TAP-GLU"
entity_type: "complex"
name: "Tapglu"
source_database: "EcoCyc"
source_id: "TAP-GLU"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Tapglu

`protein.ecocyc.TAP-GLU`

## Static

- Type: `complex`
- Source: `EcoCyc:TAP-GLU`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P07018|protein.P07018]]

## Enriched Summary

Represents a signaling complex in which one or more specific Tap glutamine residues (Q293, Q300, Q307) have been irreversibly deamidated to glutamate (E293, E300, E307) Represents a signaling complex in which one or more specific Tap glutamine residues (Q293, Q300, Q307) have been irreversibly deamidated to glutamate (E293, E300, E307)

## Annotation

Represents a signaling complex in which one or more specific Tap glutamine residues (Q293, Q300, Q307) have been irreversibly deamidated to glutamate (E293, E300, E307)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P07018|protein.P07018]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAP-GLU`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P07018
