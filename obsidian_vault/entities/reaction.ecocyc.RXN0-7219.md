---
entity_id: "reaction.ecocyc.RXN0-7219"
entity_type: "reaction"
name: "RXN0-7219"
source_database: "EcoCyc"
source_id: "RXN0-7219"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7219

`reaction.ecocyc.RXN0-7219`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7219`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-3785 + WATER -> D-galactopyranose + D-ARABINOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3785 + WATER -> D-galactopyranose + D-ARABINOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX). Substrates: H2O (molecule.C00001), 3-O-β-D-galactopyranosyl-D-arabinose (molecule.ecocyc.CPD-3785). Products: D-Galactose (molecule.C00124), D-Arabinose (molecule.C00216).

## Annotation

CPD-3785 + WATER -> D-galactopyranose + D-ARABINOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3785|molecule.ecocyc.CPD-3785]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7219`

## Notes

CPD-3785 + WATER -> D-galactopyranose + D-ARABINOSE; direction=PHYSIOL-LEFT-TO-RIGHT
