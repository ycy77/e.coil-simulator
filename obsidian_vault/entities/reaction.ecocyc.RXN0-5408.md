---
entity_id: "reaction.ecocyc.RXN0-5408"
entity_type: "reaction"
name: "RXN0-5408"
source_database: "EcoCyc"
source_id: "RXN0-5408"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "MYO-INOSITOL-1-PHOSPHATASE"
---

# RXN0-5408

`reaction.ecocyc.RXN0-5408`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5408`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + D-MYO-INOSITOL-1-MONOPHOSPHATE -> Pi + MYO-INOSITOL; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + D-MYO-INOSITOL-1-MONOPHOSPHATE -> Pi + MYO-INOSITOL; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by suhB (protein.P0ADG4). Substrates: H2O (molecule.C00001), Inositol 1-phosphate (molecule.C01177). Products: myo-Inositol (molecule.C00137), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + D-MYO-INOSITOL-1-MONOPHOSPHATE -> Pi + MYO-INOSITOL; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADG4|protein.P0ADG4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00137|molecule.C00137]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01177|molecule.C01177]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5408`

## Notes

WATER + D-MYO-INOSITOL-1-MONOPHOSPHATE -> Pi + MYO-INOSITOL; direction=PHYSIOL-LEFT-TO-RIGHT
