---
entity_id: "reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHOGLYCERATE-PHOSPHATASE-RXN

`reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHOGLYCERATE-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + 2-PG -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + 2-PG -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), 2-Phospho-D-glycerate (molecule.C00631). Products: D-Glycerate (molecule.C00258), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + 2-PG -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSPHOGLYCERATE-PHOSPHATASE-RXN`

## Notes

WATER + 2-PG -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
