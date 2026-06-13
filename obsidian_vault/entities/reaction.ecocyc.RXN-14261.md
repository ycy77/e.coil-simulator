---
entity_id: "reaction.ecocyc.RXN-14261"
entity_type: "reaction"
name: "RXN-14261"
source_database: "EcoCyc"
source_id: "RXN-14261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14261

`reaction.ecocyc.RXN-14261`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14261`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOHEXAOSE + Glucopyranose -> MALTOPENTAOSE + MALTOSE; direction=REVERSIBLE EcoCyc reaction equation: MALTOHEXAOSE + Glucopyranose -> MALTOPENTAOSE + MALTOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by malQ (protein.P15977). Substrates: D-Glucose (molecule.C00031), maltohexaose (molecule.ecocyc.MALTOHEXAOSE). Products: Maltose (molecule.C00208), maltopentaose (molecule.ecocyc.MALTOPENTAOSE).

## Annotation

MALTOHEXAOSE + Glucopyranose -> MALTOPENTAOSE + MALTOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15977|protein.P15977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOPENTAOSE|molecule.ecocyc.MALTOPENTAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14261`

## Notes

MALTOHEXAOSE + Glucopyranose -> MALTOPENTAOSE + MALTOSE; direction=REVERSIBLE
