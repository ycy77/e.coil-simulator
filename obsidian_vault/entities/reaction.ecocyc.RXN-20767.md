---
entity_id: "reaction.ecocyc.RXN-20767"
entity_type: "reaction"
name: "RXN-20767"
source_database: "EcoCyc"
source_id: "RXN-20767"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20767

`reaction.ecocyc.RXN-20767`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20767`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Fe2-siderophores + NADP + PROTON -> Fe3-siderophores + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Fe2-siderophores + NADP + PROTON -> Fe3-siderophores + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006), H+ (molecule.C00080), a siderophore-bound Fe(II) (molecule.ecocyc.Fe2-siderophores). Products: NADPH (molecule.C00005), a siderophore-bound Fe(III) (molecule.ecocyc.Fe3-siderophores).

## Annotation

Fe2-siderophores + NADP + PROTON -> Fe3-siderophores + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Fe3-siderophores|molecule.ecocyc.Fe3-siderophores]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Fe2-siderophores|molecule.ecocyc.Fe2-siderophores]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20767`

## Notes

Fe2-siderophores + NADP + PROTON -> Fe3-siderophores + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
