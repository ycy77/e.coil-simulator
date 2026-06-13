---
entity_id: "reaction.ecocyc.RXN-13519"
entity_type: "reaction"
name: "vectoral H+ export"
source_database: "EcoCyc"
source_id: "RXN-13519"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# vectoral H+ export

`reaction.ecocyc.RXN-13519`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13519`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a special transport reaction, which does not occur on its own. Instead, it can be used as a component for composing composite electron transport reactions, when there is a vectoral proton transport component. EcoCyc reaction equation: PROTON -> PROTON; direction=LEFT-TO-RIGHT. This is a special transport reaction, which does not occur on its own. Instead, it can be used as a component for composing composite electron transport reactions, when there is a vectoral proton transport component.

## Biological Role

Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

This is a special transport reaction, which does not occur on its own. Instead, it can be used as a component for composing composite electron transport reactions, when there is a vectoral proton transport component.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13519`

## Notes

PROTON -> PROTON; direction=LEFT-TO-RIGHT
