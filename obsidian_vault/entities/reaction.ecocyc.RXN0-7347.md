---
entity_id: "reaction.ecocyc.RXN0-7347"
entity_type: "reaction"
name: "RXN0-7347"
source_database: "EcoCyc"
source_id: "RXN0-7347"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7347

`reaction.ecocyc.RXN0-7347`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7347`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOSE -> Glucopyranose + MALTOTRIOSE; direction= EcoCyc reaction equation: MALTOSE -> Glucopyranose + MALTOTRIOSE; direction=.

## Biological Role

Catalyzed by malQ (protein.P15977). Substrates: Maltose (molecule.C00208). Products: D-Glucose (molecule.C00031), Maltotriose (molecule.C01835).

## Annotation

MALTOSE -> Glucopyranose + MALTOTRIOSE; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15977|protein.P15977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06802|molecule.C06802]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7347`

## Notes

MALTOSE -> Glucopyranose + MALTOTRIOSE; direction=
