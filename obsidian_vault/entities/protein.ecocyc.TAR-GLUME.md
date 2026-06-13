---
entity_id: "protein.ecocyc.TAR-GLUME"
entity_type: "complex"
name: "Targlu-Me"
source_database: "EcoCyc"
source_id: "TAR-GLUME"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Targlu-Me

`protein.ecocyc.TAR-GLUME`

## Static

- Type: `complex`
- Source: `EcoCyc:TAR-GLUME`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]], [[protein.P0A964|protein.P0A964]], [[protein.P07017|protein.P07017]]

## Enriched Summary

Represents a signaling complex in which one or more specific Tar glutamate residues (E295, E302, E309, E491, E500) have been methylated. Represents a signaling complex in which one or more specific Tar glutamate residues (E295, E302, E309, E491, E500) have been methylated.

## Annotation

Represents a signaling complex in which one or more specific Tar glutamate residues (E295, E302, E309, E491, E500) have been methylated.

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.CHERTARM-RXN|reaction.ecocyc.CHERTARM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P07017|protein.P07017]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A964|protein.P0A964]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TAR-GLUME`

## Notes

2*protein.P07363|2*protein.P0A964|12*protein.P07017
