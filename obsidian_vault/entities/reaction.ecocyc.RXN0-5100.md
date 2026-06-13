---
entity_id: "reaction.ecocyc.RXN0-5100"
entity_type: "reaction"
name: "RXN0-5100"
source_database: "EcoCyc"
source_id: "RXN0-5100"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5100

`reaction.ecocyc.RXN0-5100`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5100`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-Segment-Placeholder -> DNA-Segment-in-Reverse-Orientations; direction=REVERSIBLE EcoCyc reaction equation: DNA-Segment-Placeholder -> DNA-Segment-in-Reverse-Orientations; direction=REVERSIBLE.

## Biological Role

Catalyzed by pinE (protein.P03014). Substrates: a DNA segment (molecule.ecocyc.DNA-Segment-Placeholder).

## Annotation

DNA-Segment-Placeholder -> DNA-Segment-in-Reverse-Orientations; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P03014|protein.P03014]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Segment-Placeholder|molecule.ecocyc.DNA-Segment-Placeholder]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5100`

## Notes

DNA-Segment-Placeholder -> DNA-Segment-in-Reverse-Orientations; direction=REVERSIBLE
