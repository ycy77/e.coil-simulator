---
entity_id: "reaction.ecocyc.KDO-8PSYNTH-RXN"
entity_type: "reaction"
name: "KDO-8PSYNTH-RXN"
source_database: "EcoCyc"
source_id: "KDO-8PSYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDO-8PSYNTH-RXN

`reaction.ecocyc.KDO-8PSYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDO-8PSYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis. EcoCyc reaction equation: CPD-18118 + WATER + PHOSPHO-ENOL-PYRUVATE -> KDO-8P + Pi; direction=LEFT-TO-RIGHT. This is the first step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Biological Role

Catalyzed by 3-deoxy-D-manno-octulosonate 8-phosphate synthase (complex.ecocyc.KDO-8PSYNTH-CPLX). Substrates: H2O (molecule.C00001), Phosphoenolpyruvate (molecule.C00074), D-arabinofuranose 5-phosphate (molecule.ecocyc.CPD-18118). Products: 3-Deoxy-D-manno-octulosonate 8-phosphate (molecule.C04478), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Annotation

This is the first step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.KDO-8PSYNTH-CPLX|complex.ecocyc.KDO-8PSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04478|molecule.C04478]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18118|molecule.ecocyc.CPD-18118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04478|molecule.C04478]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDO-8PSYNTH-RXN`

## Notes

CPD-18118 + WATER + PHOSPHO-ENOL-PYRUVATE -> KDO-8P + Pi; direction=LEFT-TO-RIGHT
