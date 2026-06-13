---
entity_id: "reaction.ecocyc.CPM-KDOSYNTH-RXN"
entity_type: "reaction"
name: "CPM-KDOSYNTH-RXN"
source_database: "EcoCyc"
source_id: "CPM-KDOSYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CPM-KDOSYNTH-RXN

`reaction.ecocyc.CPM-KDOSYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CPM-KDOSYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis. EcoCyc reaction equation: KDO + CTP -> CMP-KDO + PPI; direction=LEFT-TO-RIGHT. This is the third step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Biological Role

Catalyzed by kdsB (protein.P04951). Substrates: CTP (molecule.C00063), 3-deoxy-α-D-manno-2-octulosonate (molecule.ecocyc.KDO). Products: Diphosphate (molecule.C00013), CMP-3-deoxy-D-manno-octulosonate (molecule.C04121).

## Enriched Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Annotation

This is the third step in KDO biosynthesis, leading to lipopolysaccharide biosynthesis.

## Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P04951|protein.P04951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04121|molecule.C04121]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.KDO|molecule.ecocyc.KDO]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2019|molecule.ecocyc.CPD0-2019]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CPM-KDOSYNTH-RXN`

## Notes

KDO + CTP -> CMP-KDO + PPI; direction=LEFT-TO-RIGHT
