---
entity_id: "reaction.ecocyc.RXN0-384"
entity_type: "reaction"
name: "RXN0-384"
source_database: "EcoCyc"
source_id: "RXN0-384"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-384

`reaction.ecocyc.RXN0-384`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-384`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DATP + WATER -> PROTON + DAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DATP + WATER -> PROTON + DAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudB (protein.P0AFC0). Substrates: H2O (molecule.C00001), dATP (molecule.C00131). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), dAMP (molecule.C00360).

## Annotation

DATP + WATER -> PROTON + DAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AFC0|protein.P0AFC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00360|molecule.C00360]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00360|molecule.C00360]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-384`

## Notes

DATP + WATER -> PROTON + DAMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
