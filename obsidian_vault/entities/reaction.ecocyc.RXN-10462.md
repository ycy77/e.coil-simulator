---
entity_id: "reaction.ecocyc.RXN-10462"
entity_type: "reaction"
name: "RXN-10462"
source_database: "EcoCyc"
source_id: "RXN-10462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10462

`reaction.ecocyc.RXN-10462`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10462`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCEROL-3P + ACYL-ACP -> ACYL-SN-GLYCEROL-3P + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLYCEROL-3P + ACYL-ACP -> ACYL-SN-GLYCEROL-3P + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681).

## Enriched Pathways

- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Annotation

GLYCEROL-3P + ACYL-ACP -> ACYL-SN-GLYCEROL-3P + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00681|molecule.C00681]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10462`

## Notes

GLYCEROL-3P + ACYL-ACP -> ACYL-SN-GLYCEROL-3P + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
