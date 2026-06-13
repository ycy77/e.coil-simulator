---
entity_id: "reaction.ecocyc.HEMEOSYN-RXN"
entity_type: "reaction"
name: "heme o biosynthesis"
source_database: "EcoCyc"
source_id: "HEMEOSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# heme o biosynthesis

`reaction.ecocyc.HEMEOSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HEMEOSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes heme O, a prosthetic group essential for the catalytic functions of cytochrome o ubiquinol oxidase. EcoCyc reaction equation: PROTOHEME + FARNESYL-PP + WATER -> CPD-17063 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes heme O, a prosthetic group essential for the catalytic functions of cytochrome o ubiquinol oxidase.

## Biological Role

Catalyzed by cyoE (protein.P0AEA5). Substrates: H2O (molecule.C00001), trans,trans-Farnesyl diphosphate (molecule.C00448), protoheme (molecule.ecocyc.PROTOHEME). Products: Diphosphate (molecule.C00013), ferroheme o (molecule.ecocyc.CPD-17063).

## Annotation

This reaction synthesizes heme O, a prosthetic group essential for the catalytic functions of cytochrome o ubiquinol oxidase.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEA5|protein.P0AEA5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17063|molecule.ecocyc.CPD-17063]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00448|molecule.C00448]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HEMEOSYN-RXN`

## Notes

PROTOHEME + FARNESYL-PP + WATER -> CPD-17063 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
