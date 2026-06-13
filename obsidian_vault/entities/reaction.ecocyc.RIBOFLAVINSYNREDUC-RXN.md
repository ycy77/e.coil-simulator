---
entity_id: "reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN"
entity_type: "reaction"
name: "RIBOFLAVINSYNREDUC-RXN"
source_database: "EcoCyc"
source_id: "RIBOFLAVINSYNREDUC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOFLAVINSYNREDUC-RXN

`reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOFLAVINSYNREDUC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of riboflavin biosynthesis. EcoCyc reaction equation: CPD-1086 + NADP -> CPD-602 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is part of riboflavin biosynthesis.

## Biological Role

Catalyzed by fused diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase (complex.ecocyc.CPLX0-7659). Substrates: NADP+ (molecule.C00006), 5-Amino-6-(5'-phospho-D-ribitylamino)uracil (molecule.C04454). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 5-Amino-6-(5'-phosphoribosylamino)uracil (molecule.C01268).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This reaction is part of riboflavin biosynthesis.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7659|complex.ecocyc.CPLX0-7659]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01268|molecule.C01268]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04454|molecule.C04454]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1407|molecule.ecocyc.CPD0-1407]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RIBOFLAVINSYNREDUC-RXN`

## Notes

CPD-1086 + NADP -> CPD-602 + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
