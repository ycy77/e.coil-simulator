---
entity_id: "reaction.ecocyc.RXN-14523"
entity_type: "reaction"
name: "RXN-14523"
source_database: "EcoCyc"
source_id: "RXN-14523"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14523

`reaction.ecocyc.RXN-14523`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14523`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-15393 + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15393 + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), 2'-deoxyuridine 3'-monophosphate (molecule.ecocyc.CPD-15393). Products: Deoxyuridine (molecule.C00526), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-15393 + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15393|molecule.ecocyc.CPD-15393]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14523`

## Notes

CPD-15393 + WATER -> DEOXYURIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
