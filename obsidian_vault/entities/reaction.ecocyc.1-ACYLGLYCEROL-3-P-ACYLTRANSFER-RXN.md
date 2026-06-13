---
entity_id: "reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN"
entity_type: "reaction"
name: "1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN

`reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety. EcoCyc reaction equation: ACYL-SN-GLYCEROL-3P + ACYL-ACP -> L-PHOSPHATIDATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety.

## Biological Role

Catalyzed by plsC (protein.P26647), yihG (protein.P32129). Substrates: 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681). Products: Phosphatidate (molecule.C00416).

## Enriched Pathways

- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Annotation

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety.

## Pathways

- `ecocyc.PWY0-1319` CDP-diacylglycerol biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P32129|protein.P32129]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00416|molecule.C00416]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00681|molecule.C00681]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN`

## Notes

ACYL-SN-GLYCEROL-3P + ACYL-ACP -> L-PHOSPHATIDATE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
