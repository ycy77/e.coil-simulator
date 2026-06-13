---
entity_id: "reaction.ecocyc.RXN0-363"
entity_type: "reaction"
name: "RXN0-363"
source_database: "EcoCyc"
source_id: "RXN0-363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-363

`reaction.ecocyc.RXN0-363`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-363`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XANTHOSINE + WATER -> XANTHINE + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: XANTHOSINE + WATER -> XANTHINE + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rihC (protein.P22564). Substrates: H2O (molecule.C00001), Xanthosine (molecule.C01762). Products: Xanthine (molecule.C00385), D-ribofuranose (molecule.ecocyc.D-Ribofuranose).

## Annotation

XANTHOSINE + WATER -> XANTHINE + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P22564|protein.P22564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Ribofuranose|molecule.ecocyc.D-Ribofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01762|molecule.C01762]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-363`

## Notes

XANTHOSINE + WATER -> XANTHINE + D-Ribofuranose; direction=PHYSIOL-LEFT-TO-RIGHT
