---
entity_id: "reaction.ecocyc.RXN-14026"
entity_type: "reaction"
name: "RXN-14026"
source_database: "EcoCyc"
source_id: "RXN-14026"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14026

`reaction.ecocyc.RXN-14026`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14026`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CMP + WATER -> CYTIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CMP + WATER -> CYTIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), CMP (molecule.C00055). Products: Cytidine (molecule.C00475), phosphate (molecule.ecocyc.Pi).

## Annotation

CMP + WATER -> CYTIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14026`

## Notes

CMP + WATER -> CYTIDINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
