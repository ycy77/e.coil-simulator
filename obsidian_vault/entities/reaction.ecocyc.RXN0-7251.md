---
entity_id: "reaction.ecocyc.RXN0-7251"
entity_type: "reaction"
name: "RXN0-7251"
source_database: "EcoCyc"
source_id: "RXN0-7251"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7251

`reaction.ecocyc.RXN0-7251`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7251`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-GLYCERALDEHYDE-3-PHOSPHATE + WATER -> L-GLYCERALDEHYDE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-GLYCERALDEHYDE-3-PHOSPHATE + WATER -> L-GLYCERALDEHYDE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), L-glyceraldehyde 3-phosphate (molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE). Products: L-Glyceraldehyde (molecule.C02426), phosphate (molecule.ecocyc.Pi).

## Annotation

L-GLYCERALDEHYDE-3-PHOSPHATE + WATER -> L-GLYCERALDEHYDE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C02426|molecule.C02426]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE|molecule.ecocyc.L-GLYCERALDEHYDE-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7251`

## Notes

L-GLYCERALDEHYDE-3-PHOSPHATE + WATER -> L-GLYCERALDEHYDE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
