---
entity_id: "reaction.ecocyc.RXN-14142"
entity_type: "reaction"
name: "RXN-14142"
source_database: "EcoCyc"
source_id: "RXN-14142"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14142

`reaction.ecocyc.RXN-14142`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14142`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

DGMP + WATER -> DEOXYGUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DGMP + WATER -> DEOXYGUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), surE (protein.P0A840). Substrates: H2O (molecule.C00001), dGMP (molecule.C00362). Products: Deoxyguanosine (molecule.C00330), phosphate (molecule.ecocyc.Pi).

## Annotation

DGMP + WATER -> DEOXYGUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00362|molecule.C00362]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14142`

## Notes

DGMP + WATER -> DEOXYGUANOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
