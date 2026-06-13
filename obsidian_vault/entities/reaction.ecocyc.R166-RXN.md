---
entity_id: "reaction.ecocyc.R166-RXN"
entity_type: "reaction"
name: "R166-RXN"
source_database: "EcoCyc"
source_id: "R166-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R166-RXN

`reaction.ecocyc.R166-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R166-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PD00237 + MALTOTRIOSE + ATP -> MONOMER0-158; direction=REVERSIBLE EcoCyc reaction equation: PD00237 + MALTOTRIOSE + ATP -> MONOMER0-158; direction=REVERSIBLE.

## Biological Role

Substrates: ATP (molecule.C00002), Maltotriose (molecule.C01835).

## Annotation

PD00237 + MALTOTRIOSE + ATP -> MONOMER0-158; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:R166-RXN`

## Notes

PD00237 + MALTOTRIOSE + ATP -> MONOMER0-158; direction=REVERSIBLE
