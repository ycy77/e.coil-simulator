---
entity_id: "reaction.ecocyc.RXN-15744"
entity_type: "reaction"
name: "RXN-15744"
source_database: "EcoCyc"
source_id: "RXN-15744"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15744

`reaction.ecocyc.RXN-15744`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15744`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROPANE-1-2-DIOL + NADP -> LACTALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: PROPANE-1-2-DIOL + NADP -> LACTALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), (S)-propane-1,2-diol (molecule.ecocyc.PROPANE-1-2-DIOL). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (S)-Lactaldehyde (molecule.C00424).

## Annotation

PROPANE-1-2-DIOL + NADP -> LACTALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75691|protein.P75691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROPANE-1-2-DIOL|molecule.ecocyc.PROPANE-1-2-DIOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15744`

## Notes

PROPANE-1-2-DIOL + NADP -> LACTALD + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
