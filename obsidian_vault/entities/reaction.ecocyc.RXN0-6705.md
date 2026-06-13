---
entity_id: "reaction.ecocyc.RXN0-6705"
entity_type: "reaction"
name: "RXN0-6705"
source_database: "EcoCyc"
source_id: "RXN0-6705"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6705

`reaction.ecocyc.RXN0-6705`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6705`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety. This reaction, using the specific compound instances leading to the dipalmitoyl lipid, was needed for FBA, because the instantiation of the generic reaction failed for this case (because of an ambiguous match). EcoCyc reaction equation: 1-PALMITOYLGLYCEROL-3-PHOSPHATE + Palmitoyl-ACPs -> CPD0-1422 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety. This reaction, using the specific compound instances leading to the dipalmitoyl lipid, was needed for FBA, because the instantiation of the generic reaction failed for this case (because of an ambiguous match).

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: dipalmitoyl phosphatidate (molecule.ecocyc.CPD0-1422).

## Annotation

This is the second step in de novo phospholipid biosynthesis in which a second fatty acid is esterified at C2 of the glycerol moiety. This reaction, using the specific compound instances leading to the dipalmitoyl lipid, was needed for FBA, because the instantiation of the generic reaction failed for this case (because of an ambiguous match).

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1422|molecule.ecocyc.CPD0-1422]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6705`

## Notes

1-PALMITOYLGLYCEROL-3-PHOSPHATE + Palmitoyl-ACPs -> CPD0-1422 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
