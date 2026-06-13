---
entity_id: "reaction.ecocyc.RXN0-5265"
entity_type: "reaction"
name: "RXN0-5265"
source_database: "EcoCyc"
source_id: "RXN0-5265"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5265

`reaction.ecocyc.RXN0-5265`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5265`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXYGEN-MOLECULE + PROTON + E- -> WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: OXYGEN-MOLECULE + PROTON + E- -> WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080). Products: H2O (molecule.C00001).

## Annotation

OXYGEN-MOLECULE + PROTON + E- -> WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5265`

## Notes

OXYGEN-MOLECULE + PROTON + E- -> WATER; direction=PHYSIOL-LEFT-TO-RIGHT
