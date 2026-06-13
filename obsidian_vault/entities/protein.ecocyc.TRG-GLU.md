---
entity_id: "protein.ecocyc.TRG-GLU"
entity_type: "complex"
name: "Trgglu"
source_database: "EcoCyc"
source_id: "TRG-GLU"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Trgglu

`protein.ecocyc.TRG-GLU`

## Static

- Type: `complex`
- Source: `EcoCyc:TRG-GLU`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P05704|protein.P05704]]

## Enriched Summary

Represents a signaling complex in which one or more specific Trg glutamine residues (Q312, Q319) have been irreversibly deamidated to glutamate (E312, E319) Represents a signaling complex in which one or more specific Trg glutamine residues (Q312, Q319) have been irreversibly deamidated to glutamate (E312, E319)

## Annotation

Represents a signaling complex in which one or more specific Trg glutamine residues (Q312, Q319) have been irreversibly deamidated to glutamate (E312, E319)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P05704|protein.P05704]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TRG-GLU`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P05704
