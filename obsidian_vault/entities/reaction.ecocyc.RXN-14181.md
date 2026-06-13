---
entity_id: "reaction.ecocyc.RXN-14181"
entity_type: "reaction"
name: "RXN-14181"
source_database: "EcoCyc"
source_id: "RXN-14181"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14181

`reaction.ecocyc.RXN-14181`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14181`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

PYRIDOXINE-5P + WATER -> PYRIDOXINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PYRIDOXINE-5P + WATER -> PYRIDOXINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Pyridoxine phosphate (molecule.C00627). Products: Pyridoxine (molecule.C00314), phosphate (molecule.ecocyc.Pi).

## Annotation

PYRIDOXINE-5P + WATER -> PYRIDOXINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00627|molecule.C00627]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14181`

## Notes

PYRIDOXINE-5P + WATER -> PYRIDOXINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
