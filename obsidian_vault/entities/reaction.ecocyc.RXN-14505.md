---
entity_id: "reaction.ecocyc.RXN-14505"
entity_type: "reaction"
name: "RXN-14505"
source_database: "EcoCyc"
source_id: "RXN-14505"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14505

`reaction.ecocyc.RXN-14505`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14505`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-THREONINE-O-3-PHOSPHATE + WATER -> THR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-THREONINE-O-3-PHOSPHATE + WATER -> THR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), L-Threonine O-3-phosphate (molecule.C12147). Products: L-Threonine (molecule.C00188), phosphate (molecule.ecocyc.Pi).

## Annotation

L-THREONINE-O-3-PHOSPHATE + WATER -> THR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12147|molecule.C12147]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14505`

## Notes

L-THREONINE-O-3-PHOSPHATE + WATER -> THR + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
