---
entity_id: "reaction.ecocyc.RXN-17495"
entity_type: "reaction"
name: "RXN-17495"
source_database: "EcoCyc"
source_id: "RXN-17495"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17495

`reaction.ecocyc.RXN-17495`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17495`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

MI-PENTAKISPHOSPHATE + WATER -> CPD-18901 + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MI-PENTAKISPHOSPHATE + WATER -> CPD-18901 + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by periplasmic phosphoanhydride phosphatase/multiple inositol-polyphosphate phosphatase (complex.ecocyc.CPLX-722). Substrates: H2O (molecule.C00001), D-myo-inositol (1,2,3,4,5)-pentakisphosphate (molecule.ecocyc.MI-PENTAKISPHOSPHATE). Products: D-myo-inositol (2,3,4,5) tetrakisphosphate (molecule.ecocyc.CPD-18901), phosphate (molecule.ecocyc.Pi).

## Annotation

MI-PENTAKISPHOSPHATE + WATER -> CPD-18901 + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-722|complex.ecocyc.CPLX-722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18901|molecule.ecocyc.CPD-18901]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MI-PENTAKISPHOSPHATE|molecule.ecocyc.MI-PENTAKISPHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17495`

## Notes

MI-PENTAKISPHOSPHATE + WATER -> CPD-18901 + Pi; direction=LEFT-TO-RIGHT
