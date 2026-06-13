---
entity_id: "reaction.ecocyc.RXN0-5185"
entity_type: "reaction"
name: "RXN0-5185"
source_database: "EcoCyc"
source_id: "RXN0-5185"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5185

`reaction.ecocyc.RXN0-5185`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5185`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

CPD-2961 + WATER -> GLUCONATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-2961 + WATER -> GLUCONATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), yieH (protein.P31467). Substrates: H2O (molecule.C00001), 6-Phospho-D-gluconate (molecule.C00345). Products: D-Gluconic acid (molecule.C00257), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-2961 + WATER -> GLUCONATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P31467|protein.P31467]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5185`

## Notes

CPD-2961 + WATER -> GLUCONATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
