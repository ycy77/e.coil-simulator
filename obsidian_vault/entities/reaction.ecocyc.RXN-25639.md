---
entity_id: "reaction.ecocyc.RXN-25639"
entity_type: "reaction"
name: "RXN-25639"
source_database: "EcoCyc"
source_id: "RXN-25639"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25639

`reaction.ecocyc.RXN-25639`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25639`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SUPER-OXIDE + MN+3 -> MN+2 + OXYGEN-MOLECULE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SUPER-OXIDE + MN+3 -> MN+2 + OXYGEN-MOLECULE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Mn3+ (molecule.ecocyc.MN_3), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: Oxygen (molecule.C00007), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

SUPER-OXIDE + MN+3 -> MN+2 + OXYGEN-MOLECULE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MN_3|molecule.ecocyc.MN_3]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25639`

## Notes

SUPER-OXIDE + MN+3 -> MN+2 + OXYGEN-MOLECULE; direction=PHYSIOL-LEFT-TO-RIGHT
