---
entity_id: "reaction.ecocyc.RXN0-1001"
entity_type: "reaction"
name: "RXN0-1001"
source_database: "EcoCyc"
source_id: "RXN0-1001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1001

`reaction.ecocyc.RXN0-1001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1001`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

MI-HEXAKISPHOSPHATE + WATER -> CPD-534 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MI-HEXAKISPHOSPHATE + WATER -> CPD-534 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glucose-1-phosphatase (complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX). Substrates: H2O (molecule.C00001), Phytic acid (molecule.C01204). Products: D-myo-Inositol 1,2,4,5,6-pentakisphosphate (molecule.C04563), phosphate (molecule.ecocyc.Pi).

## Annotation

MI-HEXAKISPHOSPHATE + WATER -> CPD-534 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX|complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04563|molecule.C04563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01204|molecule.C01204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1001`

## Notes

MI-HEXAKISPHOSPHATE + WATER -> CPD-534 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
