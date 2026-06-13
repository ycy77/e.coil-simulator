---
entity_id: "reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "SORBITOL-6-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "SORBITOL-6-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SORBITOL-6-PHOSPHATASE-RXN

`reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SORBITOL-6-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-SORBITOL-6-P + WATER -> SORBITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-SORBITOL-6-P + WATER -> SORBITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hxpB (protein.P77247), hxpA (protein.P77625). Substrates: H2O (molecule.C00001), Sorbitol 6-phosphate (molecule.C01096). Products: D-Sorbitol (molecule.C00794), phosphate (molecule.ecocyc.Pi).

## Annotation

D-SORBITOL-6-P + WATER -> SORBITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77247|protein.P77247]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77625|protein.P77625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00794|molecule.C00794]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01096|molecule.C01096]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SORBITOL-6-PHOSPHATASE-RXN`

## Notes

D-SORBITOL-6-P + WATER -> SORBITOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
