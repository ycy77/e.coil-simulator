---
entity_id: "reaction.ecocyc.THIAZOLSYN2-RXN"
entity_type: "reaction"
name: "THIAZOLSYN2-RXN"
source_database: "EcoCyc"
source_id: "THIAZOLSYN2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# THIAZOLSYN2-RXN

`reaction.ecocyc.THIAZOLSYN2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:THIAZOLSYN2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated. EcoCyc reaction equation: DEOXYXYLULOSE-5P + CPD-12279 + ThiS-CoASH-proteins -> CPD-13575 + WATER + Thi-S; direction=LEFT-TO-RIGHT. This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Biological Role

Catalyzed by thiG (protein.P30139). Substrates: 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437), Iminoglycine (molecule.C15809). Products: H2O (molecule.C00001), 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate (molecule.C20246).

## Enriched Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Annotation

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Pathways

- `ecocyc.PWY-6892` thiazole component of thiamine diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P30139|protein.P30139]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20246|molecule.C20246]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15809|molecule.C15809]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:THIAZOLSYN2-RXN`

## Notes

DEOXYXYLULOSE-5P + CPD-12279 + ThiS-CoASH-proteins -> CPD-13575 + WATER + Thi-S; direction=LEFT-TO-RIGHT
