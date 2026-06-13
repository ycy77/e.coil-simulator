---
entity_id: "reaction.ecocyc.RXN0-7196"
entity_type: "reaction"
name: "RXN0-7196"
source_database: "EcoCyc"
source_id: "RXN0-7196"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7196

`reaction.ecocyc.RXN0-7196`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7196`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated. EcoCyc reaction equation: DEOXYXYLULOSE-5P + CPD-12279 + ThiS-ThiF-disulfides + Reduced-ferredoxins + PROTON -> CPD-13575 + WATER + ThiF-Proteins + Thi-S + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Biological Role

Substrates: H+ (molecule.C00080), 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437), Iminoglycine (molecule.C15809). Products: H2O (molecule.C00001), 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate (molecule.C20246).

## Annotation

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20246|molecule.C20246]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15809|molecule.C15809]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7196`

## Notes

DEOXYXYLULOSE-5P + CPD-12279 + ThiS-ThiF-disulfides + Reduced-ferredoxins + PROTON -> CPD-13575 + WATER + ThiF-Proteins + Thi-S + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
