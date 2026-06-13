---
entity_id: "reaction.ecocyc.RXN-14534"
entity_type: "reaction"
name: "RXN-14534"
source_database: "EcoCyc"
source_id: "RXN-14534"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14534

`reaction.ecocyc.RXN-14534`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14534`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3728 + WATER -> TYR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3728 + WATER -> TYR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), O-phospho-L-tyrosine (molecule.ecocyc.CPD-3728). Products: L-Tyrosine (molecule.C00082), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3728 + WATER -> TYR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3728|molecule.ecocyc.CPD-3728]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14534`

## Notes

CPD-3728 + WATER -> TYR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
