---
entity_id: "reaction.ecocyc.3.1.3.74-RXN"
entity_type: "reaction"
name: "3.1.3.74-RXN"
source_database: "EcoCyc"
source_id: "3.1.3.74-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.3.74-RXN

`reaction.ecocyc.3.1.3.74-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.3.74-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

PYRIDOXAL_PHOSPHATE + WATER -> PYRIDOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PYRIDOXAL_PHOSPHATE + WATER -> PYRIDOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), ybhA (protein.P21829), yigL (protein.P27848), cof (protein.P46891). Substrates: H2O (molecule.C00001), Pyridoxal phosphate (molecule.C00018). Products: Pyridoxal (molecule.C00250), phosphate (molecule.ecocyc.Pi).

## Annotation

PYRIDOXAL_PHOSPHATE + WATER -> PYRIDOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21829|protein.P21829]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27848|protein.P27848]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P46891|protein.P46891]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.3.74-RXN`

## Notes

PYRIDOXAL_PHOSPHATE + WATER -> PYRIDOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
