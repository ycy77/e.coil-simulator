---
entity_id: "protein.ecocyc.TSR-GLU"
entity_type: "complex"
name: "Tsrglu"
source_database: "EcoCyc"
source_id: "TSR-GLU"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Tsrglu

`protein.ecocyc.TSR-GLU`

## Static

- Type: `complex`
- Source: `EcoCyc:TSR-GLU`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A964|protein.P0A964]], [[protein.P07363|protein.P07363]], [[protein.P02942|protein.P02942]]

## Enriched Summary

Represents a signaling complex in which one or more specific Tsr glutamine residues (Q297, Q311) have been irreversibly deamidated to glutamate (E297, E311) Represents a signaling complex in which one or more specific Tsr glutamine residues (Q297, Q311) have been irreversibly deamidated to glutamate (E297, E311)

## Annotation

Represents a signaling complex in which one or more specific Tsr glutamine residues (Q297, Q311) have been irreversibly deamidated to glutamate (E297, E311)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P02942|protein.P02942]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TSR-GLU`

## Notes

2*protein.P0A964|2*protein.P07363|12*protein.P02942
