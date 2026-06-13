---
entity_id: "reaction.ecocyc.RXN-14286"
entity_type: "reaction"
name: "RXN-14286"
source_database: "EcoCyc"
source_id: "RXN-14286"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14286

`reaction.ecocyc.RXN-14286`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14286`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1133 + Pi -> MALTOHEXAOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1133 + Pi -> MALTOHEXAOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin phosphorylase (complex.ecocyc.MALDEXPHOSPHORYL-CPLX). Substrates: maltoheptaose (molecule.ecocyc.CPD0-1133), phosphate (molecule.ecocyc.Pi). Products: α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P), maltohexaose (molecule.ecocyc.MALTOHEXAOSE).

## Annotation

CPD0-1133 + Pi -> MALTOHEXAOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1133|molecule.ecocyc.CPD0-1133]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14286`

## Notes

CPD0-1133 + Pi -> MALTOHEXAOSE + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT
