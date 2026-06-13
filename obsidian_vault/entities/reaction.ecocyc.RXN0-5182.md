---
entity_id: "reaction.ecocyc.RXN0-5182"
entity_type: "reaction"
name: "RXN0-5182"
source_database: "EcoCyc"
source_id: "RXN0-5182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5182

`reaction.ecocyc.RXN0-5182`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5182`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOTETRAOSE + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOTETRAOSE + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin phosphorylase (complex.ecocyc.MALDEXPHOSPHORYL-CPLX). Substrates: maltotetraose (molecule.ecocyc.MALTOTETRAOSE), phosphate (molecule.ecocyc.Pi). Products: Maltotriose (molecule.C01835), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

MALTOTETRAOSE + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5182`

## Notes

MALTOTETRAOSE + Pi -> MALTOTRIOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT
