---
entity_id: "reaction.ecocyc.RXN-16788"
entity_type: "reaction"
name: "RXN-16788"
source_database: "EcoCyc"
source_id: "RXN-16788"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16788

`reaction.ecocyc.RXN-16788`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16788`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the Salmonella cobalamin biosynthetic pathway. It is not known if E. coli has an equivalent reaction. EcoCyc reaction equation: ALPHA-RIBAZOLE-5-P + WATER -> ALPHA-RIBAZOLE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in the Salmonella cobalamin biosynthetic pathway. It is not known if E. coli has an equivalent reaction.

## Biological Role

Catalyzed by cobC (protein.P52086). Substrates: H2O (molecule.C00001), N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole (molecule.C04778). Products: alpha-Ribazole (molecule.C05775), phosphate (molecule.ecocyc.Pi).

## Annotation

This is a reaction in the Salmonella cobalamin biosynthetic pathway. It is not known if E. coli has an equivalent reaction.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52086|protein.P52086]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05775|molecule.C05775]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04778|molecule.C04778]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16788`

## Notes

ALPHA-RIBAZOLE-5-P + WATER -> ALPHA-RIBAZOLE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
