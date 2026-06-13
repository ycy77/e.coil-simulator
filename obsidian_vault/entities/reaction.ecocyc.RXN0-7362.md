---
entity_id: "reaction.ecocyc.RXN0-7362"
entity_type: "reaction"
name: "RXN0-7362"
source_database: "EcoCyc"
source_id: "RXN0-7362"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7362

`reaction.ecocyc.RXN0-7362`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7362`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Glucose-6-phosphate + WATER -> D-Glucose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Glucose-6-phosphate + WATER -> D-Glucose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), D-Glucose 6-phosphate (molecule.C00092). Products: D-Glucose (molecule.C00031), phosphate (molecule.ecocyc.Pi).

## Annotation

Glucose-6-phosphate + WATER -> D-Glucose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7362`

## Notes

Glucose-6-phosphate + WATER -> D-Glucose + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
