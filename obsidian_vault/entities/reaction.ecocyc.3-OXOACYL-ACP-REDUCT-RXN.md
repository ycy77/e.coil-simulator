---
entity_id: "reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN"
entity_type: "reaction"
name: "3-OXOACYL-ACP-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "3-OXOACYL-ACP-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-OXOACYL-ACP-REDUCT-RXN

`reaction.ecocyc.3-OXOACYL-ACP-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-OXOACYL-ACP-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reduction step in the fatty acid biosynthesis pathway. EcoCyc reaction equation: OH-ACYL-ACP + NADP -> B-KETOACYL-ACP + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This is the first reduction step in the fatty acid biosynthesis pathway.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl-carrier-protein] reductase FabG (complex.ecocyc.CPLX0-8005). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Annotation

This is the first reduction step in the fatty acid biosynthesis pathway.

## Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8005|complex.ecocyc.CPLX0-8005]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3-OXOACYL-ACP-REDUCT-RXN`

## Notes

OH-ACYL-ACP + NADP -> B-KETOACYL-ACP + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
