---
entity_id: "reaction.ecocyc.RXN-2043"
entity_type: "reaction"
name: "RXN-2043"
source_database: "EcoCyc"
source_id: "RXN-2043"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-2043

`reaction.ecocyc.RXN-2043`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-2043`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR

## Enriched Summary

CELLULOSE + WATER -> Cellodextrins; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CELLULOSE + WATER -> Cellodextrins; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bcsZ (protein.P37651). Substrates: H2O (molecule.C00001), Cellulose (molecule.C00760). Products: Cellodextrin (molecule.C01898).

## Annotation

CELLULOSE + WATER -> Cellodextrins; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P37651|protein.P37651]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01898|molecule.C01898]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00760|molecule.C00760]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-2043`

## Notes

CELLULOSE + WATER -> Cellodextrins; direction=PHYSIOL-LEFT-TO-RIGHT
