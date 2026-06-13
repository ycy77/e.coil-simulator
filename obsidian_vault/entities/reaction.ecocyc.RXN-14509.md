---
entity_id: "reaction.ecocyc.RXN-14509"
entity_type: "reaction"
name: "RXN-14509"
source_database: "EcoCyc"
source_id: "RXN-14509"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14509

`reaction.ecocyc.RXN-14509`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14509`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

RIBOSE-5P + WATER -> CPD-15818 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RIBOSE-5P + WATER -> CPD-15818 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), D-Ribose 5-phosphate (molecule.C00117). Products: aldehydo-D-ribose (molecule.ecocyc.CPD-15818), phosphate (molecule.ecocyc.Pi).

## Annotation

RIBOSE-5P + WATER -> CPD-15818 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15818|molecule.ecocyc.CPD-15818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14509`

## Notes

RIBOSE-5P + WATER -> CPD-15818 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
