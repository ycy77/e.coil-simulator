---
entity_id: "reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "GLYCEROL-1-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "GLYCEROL-1-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCEROL-1-PHOSPHATASE-RXN

`reaction.ecocyc.GLYCEROL-1-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCEROL-1-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycerol-1-phosphate + WATER -> GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Glycerol-1-phosphate + WATER -> GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hxpA (protein.P77625). Substrates: H2O (molecule.C00001), glycerol 1-phosphate (molecule.ecocyc.Glycerol-1-phosphate). Products: Glycerol (molecule.C00116), phosphate (molecule.ecocyc.Pi).

## Annotation

Glycerol-1-phosphate + WATER -> GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77625|protein.P77625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Glycerol-1-phosphate|molecule.ecocyc.Glycerol-1-phosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYCEROL-1-PHOSPHATASE-RXN`

## Notes

Glycerol-1-phosphate + WATER -> GLYCEROL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
