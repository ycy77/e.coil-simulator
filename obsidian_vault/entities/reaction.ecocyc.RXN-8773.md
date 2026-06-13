---
entity_id: "reaction.ecocyc.RXN-8773"
entity_type: "reaction"
name: "RXN-8773"
source_database: "EcoCyc"
source_id: "RXN-8773"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8773

`reaction.ecocyc.RXN-8773`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8773`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XYLITOL + NADP -> D-Xylose + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: XYLITOL + NADP -> D-Xylose + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006), Xylitol (molecule.C00379). Products: NADPH (molecule.C00005), H+ (molecule.C00080), D-Xylose (molecule.C00181).

## Enriched Pathways

- `ecocyc.PWY-5516` D-xylose degradation II (EcoCyc)

## Annotation

XYLITOL + NADP -> D-Xylose + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5516` D-xylose degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00181|molecule.C00181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00379|molecule.C00379]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8773`

## Notes

XYLITOL + NADP -> D-Xylose + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
