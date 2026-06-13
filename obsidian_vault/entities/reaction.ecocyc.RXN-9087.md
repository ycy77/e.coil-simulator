---
entity_id: "reaction.ecocyc.RXN-9087"
entity_type: "reaction"
name: "RXN-9087"
source_database: "EcoCyc"
source_id: "RXN-9087"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9087

`reaction.ecocyc.RXN-9087`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9087`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROPIONYL-COA + NADP -> ACRYLYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: PROPIONYL-COA + NADP -> ACRYLYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by acrylyl-CoA reductase (complex.ecocyc.CPLX0-8121). Substrates: NADP+ (molecule.C00006), Propanoyl-CoA (molecule.C00100). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Propenoyl-CoA (molecule.C00894).

## Annotation

PROPIONYL-COA + NADP -> ACRYLYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8121|complex.ecocyc.CPLX0-8121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00894|molecule.C00894]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9087`

## Notes

PROPIONYL-COA + NADP -> ACRYLYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
