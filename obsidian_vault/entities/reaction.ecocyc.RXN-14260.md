---
entity_id: "reaction.ecocyc.RXN-14260"
entity_type: "reaction"
name: "RXN-14260"
source_database: "EcoCyc"
source_id: "RXN-14260"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14260

`reaction.ecocyc.RXN-14260`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14260`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOPENTAOSE + Glucopyranose -> MALTOTETRAOSE + MALTOSE; direction=REVERSIBLE EcoCyc reaction equation: MALTOPENTAOSE + Glucopyranose -> MALTOTETRAOSE + MALTOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by malQ (protein.P15977). Substrates: D-Glucose (molecule.C00031), maltopentaose (molecule.ecocyc.MALTOPENTAOSE). Products: Maltose (molecule.C00208), maltotetraose (molecule.ecocyc.MALTOTETRAOSE).

## Annotation

MALTOPENTAOSE + Glucopyranose -> MALTOTETRAOSE + MALTOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15977|protein.P15977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOPENTAOSE|molecule.ecocyc.MALTOPENTAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14260`

## Notes

MALTOPENTAOSE + Glucopyranose -> MALTOTETRAOSE + MALTOSE; direction=REVERSIBLE
