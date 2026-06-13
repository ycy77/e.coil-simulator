---
entity_id: "reaction.ecocyc.GPH-RXN"
entity_type: "reaction"
name: "GPH-RXN"
source_database: "EcoCyc"
source_id: "GPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GPH-RXN

`reaction.ecocyc.GPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

This reaction is part of carbohydrate metabolism. EcoCyc reaction equation: WATER + CPD-67 -> GLYCOLLATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of carbohydrate metabolism.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), gph (protein.P32662). Substrates: H2O (molecule.C00001), 2-Phosphoglycolate (molecule.C00988). Products: Glycolate (molecule.C00160), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is part of carbohydrate metabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P32662|protein.P32662]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00988|molecule.C00988]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GPH-RXN`

## Notes

WATER + CPD-67 -> GLYCOLLATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
