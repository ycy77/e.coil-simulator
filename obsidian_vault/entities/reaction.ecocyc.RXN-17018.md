---
entity_id: "reaction.ecocyc.RXN-17018"
entity_type: "reaction"
name: "RXN-17018"
source_database: "EcoCyc"
source_id: "RXN-17018"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17018

`reaction.ecocyc.RXN-17018`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17018`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Palmitoyl-ACPs + GLYCEROL-3P -> 1-PALMITOYLGLYCEROL-3-PHOSPHATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoyl-ACPs + GLYCEROL-3P -> 1-PALMITOYLGLYCEROL-3-PHOSPHATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE).

## Annotation

Palmitoyl-ACPs + GLYCEROL-3P -> 1-PALMITOYLGLYCEROL-3-PHOSPHATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17018`

## Notes

Palmitoyl-ACPs + GLYCEROL-3P -> 1-PALMITOYLGLYCEROL-3-PHOSPHATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
