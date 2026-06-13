---
entity_id: "protein.ecocyc.TAR-GLU"
entity_type: "complex"
name: "Targlu"
source_database: "EcoCyc"
source_id: "TAR-GLU"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Targlu

`protein.ecocyc.TAR-GLU`

## Static

- Type: `complex`
- Source: `EcoCyc:TAR-GLU`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P07017|protein.P07017]]

## Enriched Summary

Represents a signaling complex in which one or more specific Tar glutamine residues (Q295, Q309) have been irreversibly deamidated to glutamate (E295, E309) Represents a signaling complex in which one or more specific Tar glutamine residues (Q295, Q309) have been irreversibly deamidated to glutamate (E295, E309)

## Annotation

Represents a signaling complex in which one or more specific Tar glutamine residues (Q295, Q309) have been irreversibly deamidated to glutamate (E295, E309)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P07017|protein.P07017]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAR-GLU`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P07017
