---
entity_id: "reaction.ecocyc.FPPSYN-RXN"
entity_type: "reaction"
name: "FPPSYN-RXN"
source_database: "EcoCyc"
source_id: "FPPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "farnesyl pyrophosphate synthase"
  - "farnesyl diphosphate synthase"
  - "FPP synthase"
  - "FPP synthetase"
  - "Farnesyl diphosphate synthetase"
  - "Farnesyl pyrophosphate synthetase"
  - "Farnesyl-diphosphate synthase"
---

# FPPSYN-RXN

`reaction.ecocyc.FPPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FPPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in the biosynthesis of polyisoprenoids. EcoCyc reaction equation: GERANYL-PP + DELTA3-ISOPENTENYL-PP -> FARNESYL-PP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third reaction in the biosynthesis of polyisoprenoids.

## Biological Role

Catalyzed by ispA (protein.P22939). Substrates: Isopentenyl diphosphate (molecule.C00129), Geranyl diphosphate (molecule.C00341). Products: Diphosphate (molecule.C00013), trans,trans-Farnesyl diphosphate (molecule.C00448).

## Enriched Pathways

- `ecocyc.PWY-5123` trans, trans-farnesyl diphosphate biosynthesis (EcoCyc)

## Annotation

This is the third reaction in the biosynthesis of polyisoprenoids.

## Pathways

- `ecocyc.PWY-5123` trans, trans-farnesyl diphosphate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P22939|protein.P22939]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00448|molecule.C00448]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00129|molecule.C00129]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00341|molecule.C00341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FPPSYN-RXN`

## Notes

GERANYL-PP + DELTA3-ISOPENTENYL-PP -> FARNESYL-PP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
