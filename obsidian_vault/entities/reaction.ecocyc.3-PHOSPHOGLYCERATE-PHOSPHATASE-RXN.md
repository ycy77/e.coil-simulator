---
entity_id: "reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN

`reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + G3P -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + G3P -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), 3-Phospho-D-glycerate (molecule.C00197). Products: D-Glycerate (molecule.C00258), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + G3P -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN`

## Notes

WATER + G3P -> GLYCERATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
