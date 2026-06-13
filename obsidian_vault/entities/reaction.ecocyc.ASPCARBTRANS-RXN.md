---
entity_id: "reaction.ecocyc.ASPCARBTRANS-RXN"
entity_type: "reaction"
name: "ASPCARBTRANS-RXN"
source_database: "EcoCyc"
source_id: "ASPCARBTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPCARBTRANS-RXN

`reaction.ecocyc.ASPCARBTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPCARBTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first committed reaction, but the second step, in the biosynthesis of pyrimidine. EcoCyc reaction equation: L-ASPARTATE + CARBAMOYL-P -> PROTON + CARBAMYUL-L-ASPARTATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. The first committed reaction, but the second step, in the biosynthesis of pyrimidine.

## Biological Role

Catalyzed by aspartate carbamoyltransferase (complex.ecocyc.ASPCARBTRANS-CPLX). Substrates: L-Aspartate (molecule.C00049), Carbamoyl phosphate (molecule.C00169). Products: H+ (molecule.C00080), N-Carbamoyl-L-aspartate (molecule.C00438), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

The first committed reaction, but the second step, in the biosynthesis of pyrimidine.

## Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ASPCARBTRANS-CPLX|complex.ecocyc.ASPCARBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00438|molecule.C00438]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1617|molecule.ecocyc.CPD0-1617]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPCARBTRANS-RXN`

## Notes

L-ASPARTATE + CARBAMOYL-P -> PROTON + CARBAMYUL-L-ASPARTATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
