---
entity_id: "reaction.ecocyc.RXN0-5183"
entity_type: "reaction"
name: "RXN0-5183"
source_database: "EcoCyc"
source_id: "RXN0-5183"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5183

`reaction.ecocyc.RXN0-5183`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5183`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOTRIOSE + WATER -> MALTOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOTRIOSE + WATER -> MALTOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin glucosidase (complex.ecocyc.CPLX0-8615). Substrates: H2O (molecule.C00001), Maltotriose (molecule.C01835). Products: Maltose (molecule.C00208), alpha-D-Glucose (molecule.C00267).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

MALTOTRIOSE + WATER -> MALTOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8615|complex.ecocyc.CPLX0-8615]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5183`

## Notes

MALTOTRIOSE + WATER -> MALTOSE + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT
