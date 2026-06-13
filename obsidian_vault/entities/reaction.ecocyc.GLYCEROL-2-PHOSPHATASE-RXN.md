---
entity_id: "reaction.ecocyc.GLYCEROL-2-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "GLYCEROL-2-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "GLYCEROL-2-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCEROL-2-PHOSPHATASE-RXN

`reaction.ecocyc.GLYCEROL-2-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCEROL-2-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

WATER + CPD-536 -> Pi + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + CPD-536 -> Pi + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), suhB (protein.P0ADG4). Substrates: H2O (molecule.C00001), glycerol 2-phosphate (molecule.ecocyc.CPD-536). Products: Glycerol (molecule.C00116), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + CPD-536 -> Pi + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ADG4|protein.P0ADG4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-536|molecule.ecocyc.CPD-536]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYCEROL-2-PHOSPHATASE-RXN`

## Notes

WATER + CPD-536 -> Pi + GLYCEROL; direction=PHYSIOL-LEFT-TO-RIGHT
