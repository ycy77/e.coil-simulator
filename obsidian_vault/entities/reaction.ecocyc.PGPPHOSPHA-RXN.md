---
entity_id: "reaction.ecocyc.PGPPHOSPHA-RXN"
entity_type: "reaction"
name: "PGPPHOSPHA-RXN"
source_database: "EcoCyc"
source_id: "PGPPHOSPHA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PGPPHOSPHA-RXN

`reaction.ecocyc.PGPPHOSPHA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGPPHOSPHA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes phosphatidylglycerol, the major anionic membrane phospholipid. EcoCyc reaction equation: L-1-PHOSPHATIDYL-GLYCEROL-P + WATER -> L-1-PHOSPHATIDYL-GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes phosphatidylglycerol, the major anionic membrane phospholipid.

## Biological Role

Catalyzed by pgpB (protein.P0A924), pgpC (protein.P0AD42), pgpA (protein.P18200). Substrates: H2O (molecule.C00001), Phosphatidylglycerophosphate (molecule.C03892). Products: Phosphatidylglycerol (molecule.C00344), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Annotation

This reaction synthesizes phosphatidylglycerol, the major anionic membrane phospholipid.

## Pathways

- `ecocyc.PWY-5668` cardiolipin biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1545` cardiolipin biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0A924|protein.P0A924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AD42|protein.P0AD42]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P18200|protein.P18200]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03892|molecule.C03892]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NaF|molecule.ecocyc.NaF]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PGPPHOSPHA-RXN`

## Notes

L-1-PHOSPHATIDYL-GLYCEROL-P + WATER -> L-1-PHOSPHATIDYL-GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
