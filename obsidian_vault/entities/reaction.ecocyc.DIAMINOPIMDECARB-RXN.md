---
entity_id: "reaction.ecocyc.DIAMINOPIMDECARB-RXN"
entity_type: "reaction"
name: "DIAMINOPIMDECARB-RXN"
source_database: "EcoCyc"
source_id: "DIAMINOPIMDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIAMINOPIMDECARB-RXN

`reaction.ecocyc.DIAMINOPIMDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIAMINOPIMDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the last step in the biosynthesis of lysine. EcoCyc reaction equation: PROTON + MESO-DIAMINOPIMELATE -> LYS + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the last step in the biosynthesis of lysine.

## Biological Role

Catalyzed by diaminopimelate decarboxylase (complex.ecocyc.DIAMINOPIMDECARB-CPLX). Substrates: H+ (molecule.C00080), meso-2,6-Diaminoheptanedioate (molecule.C00680). Products: CO2 (molecule.C00011), L-Lysine (molecule.C00047).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the last step in the biosynthesis of lysine.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.ecocyc.23-DIMERCAPTOPROPAN-1-OL|molecule.ecocyc.23-DIMERCAPTOPROPAN-1-OL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.DIAMINOPIMDECARB-CPLX|complex.ecocyc.DIAMINOPIMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00680|molecule.C00680]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9793|molecule.ecocyc.CPD-9793]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1577|molecule.ecocyc.CPD0-1577]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1578|molecule.ecocyc.CPD0-1578]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIAMINOPIMDECARB-RXN`

## Notes

PROTON + MESO-DIAMINOPIMELATE -> LYS + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
