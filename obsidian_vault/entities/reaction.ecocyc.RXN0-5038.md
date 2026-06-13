---
entity_id: "reaction.ecocyc.RXN0-5038"
entity_type: "reaction"
name: "RXN0-5038"
source_database: "EcoCyc"
source_id: "RXN0-5038"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5038

`reaction.ecocyc.RXN0-5038`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5038`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CAMP + WATER -> PROTON + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CAMP + WATER -> PROTON + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cpdA (protein.P0AEW4). Substrates: H2O (molecule.C00001), 3',5'-Cyclic AMP (molecule.C00575). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CAMP + WATER -> PROTON + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEW4|protein.P0AEW4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00575|molecule.C00575]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5038`

## Notes

CAMP + WATER -> PROTON + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
