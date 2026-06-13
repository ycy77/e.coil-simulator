---
entity_id: "reaction.ecocyc.RXN-17754"
entity_type: "reaction"
name: "RXN-17754"
source_database: "EcoCyc"
source_id: "RXN-17754"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17754

`reaction.ecocyc.RXN-17754`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17754`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-3801 + WATER -> ALPHA-D-GALACTOSE + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3801 + WATER -> ALPHA-D-GALACTOSE + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by α-galactosidase (complex.ecocyc.ALPHAGALACTOSID-CPLX). Substrates: H2O (molecule.C00001), melibionate (molecule.ecocyc.CPD-3801). Products: D-Gluconic acid (molecule.C00257), alpha-D-Galactose (molecule.C00984).

## Annotation

CPD-3801 + WATER -> ALPHA-D-GALACTOSE + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALPHAGALACTOSID-CPLX|complex.ecocyc.ALPHAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00984|molecule.C00984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3801|molecule.ecocyc.CPD-3801]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17754`

## Notes

CPD-3801 + WATER -> ALPHA-D-GALACTOSE + GLUCONATE; direction=PHYSIOL-LEFT-TO-RIGHT
