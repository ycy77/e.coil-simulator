---
entity_id: "reaction.ecocyc.RXN0-5410"
entity_type: "reaction"
name: "RXN0-5410"
source_database: "EcoCyc"
source_id: "RXN0-5410"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5410

`reaction.ecocyc.RXN0-5410`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5410`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCEROL-3P + NADP -> PROTON + L-GLYCERALDEHYDE-3-PHOSPHATE + NADPH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: GLYCEROL-3P + NADP -> PROTON + L-GLYCERALDEHYDE-3-PHOSPHATE + NADPH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by gpr (protein.Q46851). Substrates: NADP+ (molecule.C00006), sn-Glycerol 3-phosphate (molecule.C00093). Products: NADPH (molecule.C00005), H+ (molecule.C00080), L-glyceraldehyde 3-phosphate (molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE).

## Annotation

GLYCEROL-3P + NADP -> PROTON + L-GLYCERALDEHYDE-3-PHOSPHATE + NADPH; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.Q46851|protein.Q46851]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5410`

## Notes

GLYCEROL-3P + NADP -> PROTON + L-GLYCERALDEHYDE-3-PHOSPHATE + NADPH; direction=RIGHT-TO-LEFT
