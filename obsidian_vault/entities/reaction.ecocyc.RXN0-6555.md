---
entity_id: "reaction.ecocyc.RXN0-6555"
entity_type: "reaction"
name: "RXN0-6555"
source_database: "EcoCyc"
source_id: "RXN0-6555"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6555

`reaction.ecocyc.RXN0-6555`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6555`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FE+2 + Siderophore + NADP -> Fe3-siderophores + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: FE+2 + Siderophore + NADP -> Fe3-siderophores + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by yqjH (protein.Q46871). Substrates: NADP+ (molecule.C00006), Fe2+ (molecule.C14818), a siderophore (molecule.ecocyc.Siderophore). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a siderophore-bound Fe(III) (molecule.ecocyc.Fe3-siderophores).

## Annotation

FE+2 + Siderophore + NADP -> Fe3-siderophores + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.Q46871|protein.Q46871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Fe3-siderophores|molecule.ecocyc.Fe3-siderophores]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Siderophore|molecule.ecocyc.Siderophore]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6555`

## Notes

FE+2 + Siderophore + NADP -> Fe3-siderophores + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
