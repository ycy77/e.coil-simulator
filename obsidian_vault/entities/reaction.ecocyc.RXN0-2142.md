---
entity_id: "reaction.ecocyc.RXN0-2142"
entity_type: "reaction"
name: "RXN0-2142"
source_database: "EcoCyc"
source_id: "RXN0-2142"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2142

`reaction.ecocyc.RXN0-2142`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2142`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

b-Hydroxy-cis-D5-dodecenoyl-ACPs + NADP -> b-Keto-cis-D5-dodecenoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: b-Hydroxy-cis-D5-dodecenoyl-ACPs + NADP -> b-Keto-cis-D5-dodecenoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl-carrier-protein] reductase FabG (complex.ecocyc.CPLX0-8005). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Annotation

b-Hydroxy-cis-D5-dodecenoyl-ACPs + NADP -> b-Keto-cis-D5-dodecenoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-862` (5Z)-dodecenoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8005|complex.ecocyc.CPLX0-8005]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2142`

## Notes

b-Hydroxy-cis-D5-dodecenoyl-ACPs + NADP -> b-Keto-cis-D5-dodecenoyl-ACPs + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
