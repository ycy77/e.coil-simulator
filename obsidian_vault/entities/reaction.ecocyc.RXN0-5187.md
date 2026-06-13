---
entity_id: "reaction.ecocyc.RXN0-5187"
entity_type: "reaction"
name: "RXN0-5187"
source_database: "EcoCyc"
source_id: "RXN0-5187"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5187

`reaction.ecocyc.RXN0-5187`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5187`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

FMN + WATER -> RIBOFLAVIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FMN + WATER -> RIBOFLAVIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), yigB (protein.P0ADP0), ybjI (protein.P75809). Substrates: H2O (molecule.C00001), FMN (molecule.C00061). Products: Riboflavin (molecule.C00255), phosphate (molecule.ecocyc.Pi).

## Annotation

FMN + WATER -> RIBOFLAVIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ADP0|protein.P0ADP0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75809|protein.P75809]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5187`

## Notes

FMN + WATER -> RIBOFLAVIN + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
