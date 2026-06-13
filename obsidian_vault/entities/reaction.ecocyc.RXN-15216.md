---
entity_id: "reaction.ecocyc.RXN-15216"
entity_type: "reaction"
name: "RXN-15216"
source_database: "EcoCyc"
source_id: "RXN-15216"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15216

`reaction.ecocyc.RXN-15216`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15216`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10551 -> CPD0-2467; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10551 -> CPD0-2467; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lsrG (protein.P64461). Substrates: (4S)-4-Hydroxy-5-phosphooxypentane-2,3-dione (molecule.C20959). Products: 3-hydroxy-2,4-dioxopentyl phosphate (molecule.ecocyc.CPD0-2467).

## Enriched Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Annotation

CPD-10551 -> CPD0-2467; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P64461|protein.P64461]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2467|molecule.ecocyc.CPD0-2467]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20959|molecule.C20959]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15216`

## Notes

CPD-10551 -> CPD0-2467; direction=LEFT-TO-RIGHT
