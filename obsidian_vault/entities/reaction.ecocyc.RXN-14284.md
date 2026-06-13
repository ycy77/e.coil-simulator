---
entity_id: "reaction.ecocyc.RXN-14284"
entity_type: "reaction"
name: "RXN-14284"
source_database: "EcoCyc"
source_id: "RXN-14284"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14284

`reaction.ecocyc.RXN-14284`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14284`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOPENTAOSE + Pi -> GLC-1-P + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOPENTAOSE + Pi -> GLC-1-P + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin phosphorylase (complex.ecocyc.MALDEXPHOSPHORYL-CPLX). Substrates: maltopentaose (molecule.ecocyc.MALTOPENTAOSE), phosphate (molecule.ecocyc.Pi). Products: α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P), maltotetraose (molecule.ecocyc.MALTOTETRAOSE).

## Annotation

MALTOPENTAOSE + Pi -> GLC-1-P + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOPENTAOSE|molecule.ecocyc.MALTOPENTAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1029|molecule.ecocyc.CPD0-1029]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14284`

## Notes

MALTOPENTAOSE + Pi -> GLC-1-P + MALTOTETRAOSE; direction=PHYSIOL-LEFT-TO-RIGHT
