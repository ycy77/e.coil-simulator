---
entity_id: "reaction.ecocyc.RXN0-5146"
entity_type: "reaction"
name: "RXN0-5146"
source_database: "EcoCyc"
source_id: "RXN0-5146"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5146

`reaction.ecocyc.RXN0-5146`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5146`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-971 + WATER -> CPD0-1027 + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-971 + WATER -> CPD0-1027 + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glgX (protein.P15067). Substrates: H2O (molecule.C00001), an α-limit dextrin (molecule.ecocyc.CPD0-971). Products: a debranched α-limit dextrin (molecule.ecocyc.CPD0-1027), maltotetraose (molecule.ecocyc.MALTOTETRAOSE).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

CPD0-971 + WATER -> CPD0-1027 + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P15067|protein.P15067]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1027|molecule.ecocyc.CPD0-1027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-971|molecule.ecocyc.CPD0-971]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CUSO4|molecule.ecocyc.CUSO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5146`

## Notes

CPD0-971 + WATER -> CPD0-1027 + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT
