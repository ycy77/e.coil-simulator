---
entity_id: "reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN"
entity_type: "reaction"
name: "2,3,4-saturated fatty acyl-[acp] dehydrogenase"
source_database: "EcoCyc"
source_id: "ENOYL-ACP-REDUCT-NADPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2,3,4-saturated fatty acyl-[acp] dehydrogenase

`reaction.ecocyc.ENOYL-ACP-REDUCT-NADPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENOYL-ACP-REDUCT-NADPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Saturated-Fatty-Acyl-ACPs + NADP -> NADPH + TRANS-D2-ENOYL-ACP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Saturated-Fatty-Acyl-ACPs + NADP -> NADPH + TRANS-D2-ENOYL-ACP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Annotation

Saturated-Fatty-Acyl-ACPs + NADP -> NADPH + TRANS-D2-ENOYL-ACP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ENOYL-ACP-REDUCT-NADPH-RXN`

## Notes

Saturated-Fatty-Acyl-ACPs + NADP -> NADPH + TRANS-D2-ENOYL-ACP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
