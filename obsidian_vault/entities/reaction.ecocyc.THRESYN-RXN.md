---
entity_id: "reaction.ecocyc.THRESYN-RXN"
entity_type: "reaction"
name: "THRESYN-RXN"
source_database: "EcoCyc"
source_id: "THRESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THRESYN-RXN

`reaction.ecocyc.THRESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THRESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the final step in threonine biosynthesis. EcoCyc reaction equation: O-PHOSPHO-L-HOMOSERINE + WATER -> Pi + THR; direction=PHYSIOL-LEFT-TO-RIGHT. This is the final step in threonine biosynthesis.

## Biological Role

Catalyzed by thrC (protein.P00934). Substrates: H2O (molecule.C00001), O-Phospho-L-homoserine (molecule.C01102). Products: L-Threonine (molecule.C00188), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.HOMOSER-THRESYN-PWY` L-threonine biosynthesis (EcoCyc)

## Annotation

This is the final step in threonine biosynthesis.

## Pathways

- `ecocyc.HOMOSER-THRESYN-PWY` L-threonine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00934|protein.P00934]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01102|molecule.C01102]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C06055|molecule.C06055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:THRESYN-RXN`

## Notes

O-PHOSPHO-L-HOMOSERINE + WATER -> Pi + THR; direction=PHYSIOL-LEFT-TO-RIGHT
