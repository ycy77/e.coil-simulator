---
entity_id: "reaction.ecocyc.GLYCEROL-KIN-RXN"
entity_type: "reaction"
name: "GLYCEROL-KIN-RXN"
source_database: "EcoCyc"
source_id: "GLYCEROL-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCEROL-KIN-RXN

`reaction.ecocyc.GLYCEROL-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCEROL-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the pathway for the utilization of glycerol as a carbon and energy source. EcoCyc reaction equation: GLYCEROL + ATP -> PROTON + GLYCEROL-3P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the pathway for the utilization of glycerol as a carbon and energy source.

## Biological Role

Catalyzed by glycerol kinase (complex.ecocyc.GLYCEROL-KIN-CPLX). Substrates: ATP (molecule.C00002), Glycerol (molecule.C00116). Products: ADP (molecule.C00008), H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093).

## Enriched Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)

## Annotation

This is the first reaction in the pathway for the utilization of glycerol as a carbon and energy source.

## Pathways

- `ecocyc.PWY-4261` glycerol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLYCEROL-KIN-CPLX|complex.ecocyc.GLYCEROL-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1054|molecule.ecocyc.CPD0-1054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1461|molecule.ecocyc.CPD0-1461]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P69783|protein.P69783]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCEROL-KIN-RXN`

## Notes

GLYCEROL + ATP -> PROTON + GLYCEROL-3P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
