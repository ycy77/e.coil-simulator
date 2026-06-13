---
entity_id: "reaction.ecocyc.KDO-8PPHOSPHAT-RXN"
entity_type: "reaction"
name: "KDO-8PPHOSPHAT-RXN"
source_database: "EcoCyc"
source_id: "KDO-8PPHOSPHAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDO-8PPHOSPHAT-RXN

`reaction.ecocyc.KDO-8PPHOSPHAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDO-8PPHOSPHAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis. EcoCyc reaction equation: KDO-8P + WATER -> KDO + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Biological Role

Catalyzed by 3-deoxy-D-manno-octulosonate 8-phosphate phosphatase KdsC (complex.ecocyc.KDO-8PPHOSPHAT-CPLX). Substrates: H2O (molecule.C00001), 3-Deoxy-D-manno-octulosonate 8-phosphate (molecule.C04478). Products: 3-deoxy-α-D-manno-2-octulosonate (molecule.ecocyc.KDO), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Annotation

This is the second step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.KDO-8PPHOSPHAT-CPLX|complex.ecocyc.KDO-8PPHOSPHAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.KDO|molecule.ecocyc.KDO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04478|molecule.C04478]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDO-8PPHOSPHAT-RXN`

## Notes

KDO-8P + WATER -> KDO + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
