---
entity_id: "reaction.ecocyc.RXN0-5514"
entity_type: "reaction"
name: "1-acylglycerol-3-phosphate O-acyltransferase"
source_database: "EcoCyc"
source_id: "RXN0-5514"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1-acylglycerol-3-phosphate O-acyltransferase

`reaction.ecocyc.RXN0-5514`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5514`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety. EcoCyc reaction equation: Saturated-2-Lysophosphatidates + Saturated-Fatty-Acyl-ACPs -> 2-3-4-Saturated-L-Phosphatidates + ACP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety.

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: a 2,3,4-saturated 2-lysophosphatidate (molecule.ecocyc.Saturated-2-Lysophosphatidates). Products: a 2,3,4-saturated 1,2-diacyl-sn-glycerol 3-phosphate (molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates).

## Annotation

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates|molecule.ecocyc.2-3-4-Saturated-L-Phosphatidates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-2-Lysophosphatidates|molecule.ecocyc.Saturated-2-Lysophosphatidates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5514`

## Notes

Saturated-2-Lysophosphatidates + Saturated-Fatty-Acyl-ACPs -> 2-3-4-Saturated-L-Phosphatidates + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
