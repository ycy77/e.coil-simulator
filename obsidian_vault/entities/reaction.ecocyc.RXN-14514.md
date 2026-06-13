---
entity_id: "reaction.ecocyc.RXN-14514"
entity_type: "reaction"
name: "RXN-14514"
source_database: "EcoCyc"
source_id: "RXN-14514"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14514

`reaction.ecocyc.RXN-14514`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14514`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3721 + WATER -> CPD-239 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3721 + WATER -> CPD-239 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), cysteamine S-phosphate (molecule.ecocyc.CPD-3721). Products: Cysteamine (molecule.C01678), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3721 + WATER -> CPD-239 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01678|molecule.C01678]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3721|molecule.ecocyc.CPD-3721]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14514`

## Notes

CPD-3721 + WATER -> CPD-239 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
