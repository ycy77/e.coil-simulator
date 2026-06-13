---
entity_id: "reaction.ecocyc.LYXK-RXN"
entity_type: "reaction"
name: "LYXK-RXN"
source_database: "EcoCyc"
source_id: "LYXK-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LYXK-RXN

`reaction.ecocyc.LYXK-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LYXK-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of L-lyxose utilization. This reaction is catalyzed by LyxK as part of the L-ascorbic acid degradation pathway . EcoCyc reaction equation: L-XYLULOSE + ATP -> PROTON + L-XYLULOSE-5-P + ADP; direction=LEFT-TO-RIGHT. This reaction is part of L-lyxose utilization. This reaction is catalyzed by LyxK as part of the L-ascorbic acid degradation pathway .

## Biological Role

Catalyzed by L-xylulose kinase (complex.ecocyc.LYXK-CPLX). Substrates: ATP (molecule.C00002), L-Xylulose (molecule.C00312). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Xylulose 5-phosphate (molecule.C03291).

## Enriched Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)

## Annotation

This reaction is part of L-lyxose utilization. This reaction is catalyzed by LyxK as part of the L-ascorbic acid degradation pathway .

## Pathways

- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.LYXK-CPLX|complex.ecocyc.LYXK-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03291|molecule.C03291]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00312|molecule.C00312]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LYXK-RXN`

## Notes

L-XYLULOSE + ATP -> PROTON + L-XYLULOSE-5-P + ADP; direction=LEFT-TO-RIGHT
