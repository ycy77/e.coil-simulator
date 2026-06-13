---
entity_id: "reaction.ecocyc.RXN-14283"
entity_type: "reaction"
name: "RXN-14283"
source_database: "EcoCyc"
source_id: "RXN-14283"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14283

`reaction.ecocyc.RXN-14283`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14283`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1133 + WATER -> MALTOHEXAOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1133 + WATER -> MALTOHEXAOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin glucosidase (complex.ecocyc.CPLX0-8615). Substrates: H2O (molecule.C00001), maltoheptaose (molecule.ecocyc.CPD0-1133). Products: alpha-D-Glucose (molecule.C00267), maltohexaose (molecule.ecocyc.MALTOHEXAOSE).

## Annotation

CPD0-1133 + WATER -> MALTOHEXAOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8615|complex.ecocyc.CPLX0-8615]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1133|molecule.ecocyc.CPD0-1133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14283`

## Notes

CPD0-1133 + WATER -> MALTOHEXAOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT
