---
entity_id: "reaction.ecocyc.RXN-17493"
entity_type: "reaction"
name: "RXN-17493"
source_database: "EcoCyc"
source_id: "RXN-17493"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17493

`reaction.ecocyc.RXN-17493`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17493`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-18903 + WATER -> CPD-6746 + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18903 + WATER -> CPD-6746 + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by periplasmic phosphoanhydride phosphatase/multiple inositol-polyphosphate phosphatase (complex.ecocyc.CPLX-722). Substrates: H2O (molecule.C00001), D-myo-inositol (2,5) bisphosphate (molecule.ecocyc.CPD-18903). Products: 1D-myo-inositol 2-phosphate (molecule.ecocyc.CPD-6746), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-18903 + WATER -> CPD-6746 + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-722|complex.ecocyc.CPLX-722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-6746|molecule.ecocyc.CPD-6746]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18903|molecule.ecocyc.CPD-18903]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17493`

## Notes

CPD-18903 + WATER -> CPD-6746 + Pi; direction=LEFT-TO-RIGHT
