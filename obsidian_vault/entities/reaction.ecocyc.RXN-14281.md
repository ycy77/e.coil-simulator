---
entity_id: "reaction.ecocyc.RXN-14281"
entity_type: "reaction"
name: "RXN-14281"
source_database: "EcoCyc"
source_id: "RXN-14281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14281

`reaction.ecocyc.RXN-14281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALTOPENTAOSE + WATER -> MALTOTETRAOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MALTOPENTAOSE + WATER -> MALTOTETRAOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by maltodextrin glucosidase (complex.ecocyc.CPLX0-8615). Substrates: H2O (molecule.C00001), maltopentaose (molecule.ecocyc.MALTOPENTAOSE). Products: D-Glucose (molecule.C00031), maltotetraose (molecule.ecocyc.MALTOTETRAOSE).

## Annotation

MALTOPENTAOSE + WATER -> MALTOTETRAOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8615|complex.ecocyc.CPLX0-8615]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOPENTAOSE|molecule.ecocyc.MALTOPENTAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14281`

## Notes

MALTOPENTAOSE + WATER -> MALTOTETRAOSE + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
