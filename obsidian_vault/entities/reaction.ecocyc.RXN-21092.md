---
entity_id: "reaction.ecocyc.RXN-21092"
entity_type: "reaction"
name: "RXN-21092"
source_database: "EcoCyc"
source_id: "RXN-21092"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21092

`reaction.ecocyc.RXN-21092`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21092`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1027 + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1027 + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin phosphorylase (complex.ecocyc.MALDEXPHOSPHORYL-CPLX). Substrates: a debranched α-limit dextrin (molecule.ecocyc.CPD0-1027), phosphate (molecule.ecocyc.Pi). Products: Maltotriose (molecule.C01835), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

CPD0-1027 + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1027|molecule.ecocyc.CPD0-1027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1029|molecule.ecocyc.CPD0-1029]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-21092`

## Notes

CPD0-1027 + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT
