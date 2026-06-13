---
entity_id: "reaction.ecocyc.RXN0-5186"
entity_type: "reaction"
name: "RXN0-5186"
source_database: "EcoCyc"
source_id: "RXN0-5186"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5186

`reaction.ecocyc.RXN0-5186`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5186`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FRU1P + WATER -> BETA-D-FRUCTOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FRU1P + WATER -> BETA-D-FRUCTOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yqaB (protein.P77475). Substrates: H2O (molecule.C00001), β-D-fructofuranose 1-phosphate (molecule.ecocyc.FRU1P). Products: β-D-fructofuranose (molecule.ecocyc.BETA-D-FRUCTOSE), phosphate (molecule.ecocyc.Pi).

## Annotation

FRU1P + WATER -> BETA-D-FRUCTOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77475|protein.P77475]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.BETA-D-FRUCTOSE|molecule.ecocyc.BETA-D-FRUCTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FRU1P|molecule.ecocyc.FRU1P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5186`

## Notes

FRU1P + WATER -> BETA-D-FRUCTOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
