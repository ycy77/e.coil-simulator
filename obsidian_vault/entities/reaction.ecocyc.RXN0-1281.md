---
entity_id: "reaction.ecocyc.RXN0-1281"
entity_type: "reaction"
name: "dihydrouridine synthase"
source_database: "EcoCyc"
source_id: "RXN0-1281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dihydrouridine synthase

`reaction.ecocyc.RXN0-1281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tRNA-Dihydrouridines + NADP -> tRNA-uridines + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: tRNA-Dihydrouridines + NADP -> tRNA-uridines + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dusB (protein.P0ABT5), dusA (protein.P32695), dusC (protein.P33371). Substrates: NADP+ (molecule.C00006), a 5,6-dihydrouridine in tRNA (molecule.ecocyc.tRNA-Dihydrouridines). Products: NADPH (molecule.C00005), H+ (molecule.C00080), tRNA uridine (molecule.C00868).

## Annotation

tRNA-Dihydrouridines + NADP -> tRNA-uridines + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0ABT5|protein.P0ABT5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P32695|protein.P32695]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33371|protein.P33371]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00868|molecule.C00868]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-Dihydrouridines|molecule.ecocyc.tRNA-Dihydrouridines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1281`

## Notes

tRNA-Dihydrouridines + NADP -> tRNA-uridines + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
