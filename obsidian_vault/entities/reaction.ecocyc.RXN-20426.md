---
entity_id: "reaction.ecocyc.RXN-20426"
entity_type: "reaction"
name: "RXN-20426"
source_database: "EcoCyc"
source_id: "RXN-20426"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20426

`reaction.ecocyc.RXN-20426`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20426`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Prime-Phosphate-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-Prime-Phosphate-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xthA (protein.P09030), nfo (protein.P0A6C1). Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

3-Prime-Phosphate-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P09030|protein.P09030]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6C1|protein.P0A6C1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20426`

## Notes

3-Prime-Phosphate-Terminated-DNAs + WATER -> 3-Hydroxy-Terminated-DNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
