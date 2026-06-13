---
entity_id: "reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN"
entity_type: "reaction"
name: "GTP-CYCLOHYDRO-I-RXN"
source_database: "EcoCyc"
source_id: "GTP-CYCLOHYDRO-I-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GTP-CYCLOHYDRO-I-RXN

`reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GTP-CYCLOHYDRO-I-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in the biosynthesis of folic acid. EcoCyc reaction equation: GTP + WATER -> PROTON + FORMATE + DIHYDRONEOPTERIN-P3; direction=LEFT-TO-RIGHT. This is the first step in the biosynthesis of folic acid.

## Biological Role

Catalyzed by GTP cyclohydrolase 1 (complex.ecocyc.FOLE-CPLX). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Formate (molecule.C00058), H+ (molecule.C00080), 7,8-Dihydroneopterin 3'-triphosphate (molecule.C04895).

## Enriched Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)
- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Annotation

This is the first step in the biosynthesis of folic acid.

## Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)
- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)
- `ecocyc.PWY0-1433` tetrahydromonapterin biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.FOLE-CPLX|complex.ecocyc.FOLE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04895|molecule.C04895]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00272|molecule.C00272]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.GUANOSINE_TETRAPHOSPHATE|molecule.ecocyc.GUANOSINE_TETRAPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GTP-CYCLOHYDRO-I-RXN`

## Notes

GTP + WATER -> PROTON + FORMATE + DIHYDRONEOPTERIN-P3; direction=LEFT-TO-RIGHT
