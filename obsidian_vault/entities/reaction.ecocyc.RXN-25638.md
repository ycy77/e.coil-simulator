---
entity_id: "reaction.ecocyc.RXN-25638"
entity_type: "reaction"
name: "RXN-25638"
source_database: "EcoCyc"
source_id: "RXN-25638"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25638

`reaction.ecocyc.RXN-25638`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25638`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MN+2 + SUPER-OXIDE + PROTON -> MN+3 + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MN+2 + SUPER-OXIDE + PROTON -> MN+3 + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Mn2+ (molecule.ecocyc.MN_2), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: Hydrogen peroxide (molecule.C00027), Mn3+ (molecule.ecocyc.MN_3).

## Annotation

MN+2 + SUPER-OXIDE + PROTON -> MN+3 + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MN_3|molecule.ecocyc.MN_3]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25638`

## Notes

MN+2 + SUPER-OXIDE + PROTON -> MN+3 + HYDROGEN-PEROXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
