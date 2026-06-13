---
entity_id: "reaction.ecocyc.RXN-11480"
entity_type: "reaction"
name: "RXN-11480"
source_database: "EcoCyc"
source_id: "RXN-11480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11480

`reaction.ecocyc.RXN-11480`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11480`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-hydroxypimeloyl-ACP-methyl-esters + NADP -> 3-Ketopimeloyl-ACP-methyl-esters + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: 3-hydroxypimeloyl-ACP-methyl-esters + NADP -> 3-Ketopimeloyl-ACP-methyl-esters + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl-carrier-protein] reductase FabG (complex.ecocyc.CPLX0-8005). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

3-hydroxypimeloyl-ACP-methyl-esters + NADP -> 3-Ketopimeloyl-ACP-methyl-esters + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8005|complex.ecocyc.CPLX0-8005]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11480`

## Notes

3-hydroxypimeloyl-ACP-methyl-esters + NADP -> 3-Ketopimeloyl-ACP-methyl-esters + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
