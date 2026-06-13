---
entity_id: "reaction.ecocyc.RXN-17726"
entity_type: "reaction"
name: "RXN-17726"
source_database: "EcoCyc"
source_id: "RXN-17726"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17726

`reaction.ecocyc.RXN-17726`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17726`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-3561 + WATER -> GALACTOSE + Fructofuranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3561 + WATER -> GALACTOSE + Fructofuranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX). Substrates: H2O (molecule.C00001), lactulose (molecule.ecocyc.CPD-3561). Products: D-fructofuranose (molecule.ecocyc.Fructofuranose), β-D-galactopyranose (molecule.ecocyc.GALACTOSE).

## Annotation

CPD-3561 + WATER -> GALACTOSE + Fructofuranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Fructofuranose|molecule.ecocyc.Fructofuranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GALACTOSE__677c1dad|molecule.ecocyc.GALACTOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3561|molecule.ecocyc.CPD-3561]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17726`

## Notes

CPD-3561 + WATER -> GALACTOSE + Fructofuranose; direction=PHYSIOL-LEFT-TO-RIGHT
