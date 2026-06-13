---
entity_id: "reaction.ecocyc.RXN-10940"
entity_type: "reaction"
name: "6-phytase"
source_database: "EcoCyc"
source_id: "RXN-10940"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 6-phytase

`reaction.ecocyc.RXN-10940`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10940`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

MI-HEXAKISPHOSPHATE + WATER -> MI-PENTAKISPHOSPHATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MI-HEXAKISPHOSPHATE + WATER -> MI-PENTAKISPHOSPHATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by periplasmic phosphoanhydride phosphatase/multiple inositol-polyphosphate phosphatase (complex.ecocyc.CPLX-722). Substrates: H2O (molecule.C00001), Phytic acid (molecule.C01204). Products: D-myo-inositol (1,2,3,4,5)-pentakisphosphate (molecule.ecocyc.MI-PENTAKISPHOSPHATE), phosphate (molecule.ecocyc.Pi).

## Annotation

MI-HEXAKISPHOSPHATE + WATER -> MI-PENTAKISPHOSPHATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-722|complex.ecocyc.CPLX-722]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.MI-PENTAKISPHOSPHATE|molecule.ecocyc.MI-PENTAKISPHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01204|molecule.C01204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10940`

## Notes

MI-HEXAKISPHOSPHATE + WATER -> MI-PENTAKISPHOSPHATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
