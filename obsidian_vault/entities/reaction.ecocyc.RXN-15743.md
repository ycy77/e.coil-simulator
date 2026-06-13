---
entity_id: "reaction.ecocyc.RXN-15743"
entity_type: "reaction"
name: "RXN-15743"
source_database: "EcoCyc"
source_id: "RXN-15743"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15743

`reaction.ecocyc.RXN-15743`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15743`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8891 + NADP -> CPD-358 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-8891 + NADP -> CPD-358 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), (R)-propane-1,2-diol (molecule.ecocyc.CPD-8891). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (R)-Lactaldehyde (molecule.C00937).

## Annotation

CPD-8891 + NADP -> CPD-358 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75691|protein.P75691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00937|molecule.C00937]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-8891|molecule.ecocyc.CPD-8891]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15743`

## Notes

CPD-8891 + NADP -> CPD-358 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
