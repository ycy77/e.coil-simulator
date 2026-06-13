---
entity_id: "reaction.ecocyc.GLUC1PADENYLTRANS-RXN"
entity_type: "reaction"
name: "GLUC1PADENYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "GLUC1PADENYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUC1PADENYLTRANS-RXN

`reaction.ecocyc.GLUC1PADENYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUC1PADENYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step in glycogen biosynthesis. EcoCyc reaction equation: PROTON + GLC-1-P + ATP -> ADP-D-GLUCOSE + PPI; direction=LEFT-TO-RIGHT. The first step in glycogen biosynthesis.

## Biological Role

Catalyzed by glucose-1-phosphate adenylyltransferase (complex.ecocyc.GLUC1PADENYLTRANS-CPLX). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P). Products: Diphosphate (molecule.C00013), ADP-glucose (molecule.C00498).

## Enriched Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Annotation

The first step in glycogen biosynthesis.

## Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-967|molecule.ecocyc.CPD0-967]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLUC1PADENYLTRANS-CPLX|complex.ecocyc.GLUC1PADENYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUC1PADENYLTRANS-RXN`

## Notes

PROTON + GLC-1-P + ATP -> ADP-D-GLUCOSE + PPI; direction=LEFT-TO-RIGHT
