---
entity_id: "reaction.ecocyc.RXN0-267"
entity_type: "reaction"
name: "RXN0-267"
source_database: "EcoCyc"
source_id: "RXN0-267"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-267

`reaction.ecocyc.RXN0-267`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-267`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Red-Thioredoxin + HYDROGEN-PEROXIDE -> Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Red-Thioredoxin + HYDROGEN-PEROXIDE -> Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by btuE (protein.P06610). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001).

## Annotation

Red-Thioredoxin + HYDROGEN-PEROXIDE -> Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P06610|protein.P06610]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-267`

## Notes

Red-Thioredoxin + HYDROGEN-PEROXIDE -> Ox-Thioredoxin + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
