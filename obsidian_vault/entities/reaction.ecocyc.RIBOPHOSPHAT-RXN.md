---
entity_id: "reaction.ecocyc.RIBOPHOSPHAT-RXN"
entity_type: "reaction"
name: "RIBOPHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "RIBOPHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOPHOSPHAT-RXN

`reaction.ecocyc.RIBOPHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOPHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in the biosynthesis of riboflavin. EcoCyc reaction equation: CPD-1086 + WATER -> AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + Pi; direction=LEFT-TO-RIGHT. This is the fourth step in the biosynthesis of riboflavin.

## Biological Role

Catalyzed by yigB (protein.P0ADP0), ybjI (protein.P75809). Substrates: H2O (molecule.C00001), 5-Amino-6-(5'-phospho-D-ribitylamino)uracil (molecule.C04454). Products: 5-Amino-6-(1-D-ribitylamino)uracil (molecule.C04732), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This is the fourth step in the biosynthesis of riboflavin.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADP0|protein.P0ADP0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75809|protein.P75809]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04732|molecule.C04732]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04454|molecule.C04454]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOPHOSPHAT-RXN`

## Notes

CPD-1086 + WATER -> AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + Pi; direction=LEFT-TO-RIGHT
