---
entity_id: "reaction.ecocyc.RXN-14115"
entity_type: "reaction"
name: "RXN-14115"
source_database: "EcoCyc"
source_id: "RXN-14115"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14115

`reaction.ecocyc.RXN-14115`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14115`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-3724 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-3724 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), cpdB (protein.P08331). Substrates: H2O (molecule.C00001), 3'-UMP (molecule.C01368). Products: Uridine (molecule.C00299), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-3724 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01368|molecule.C01368]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14115`

## Notes

CPD-3724 + WATER -> URIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
