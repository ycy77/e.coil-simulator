---
entity_id: "reaction.ecocyc.RXN-17724"
entity_type: "reaction"
name: "RXN-17724"
source_database: "EcoCyc"
source_id: "RXN-17724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17724

`reaction.ecocyc.RXN-17724`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17724`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Mannose-6-phosphate + WATER -> MANNOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Mannose-6-phosphate + WATER -> MANNOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), D-Mannose 6-phosphate (molecule.C00275). Products: D-Mannose (molecule.C00159), phosphate (molecule.ecocyc.Pi).

## Annotation

Mannose-6-phosphate + WATER -> MANNOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00159|molecule.C00159]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00275|molecule.C00275]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17724`

## Notes

Mannose-6-phosphate + WATER -> MANNOSE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
