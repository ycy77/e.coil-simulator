---
entity_id: "reaction.ecocyc.RXN-11476"
entity_type: "reaction"
name: "3-oxo-glutaryl-[acp] methyl ester reductase"
source_database: "EcoCyc"
source_id: "RXN-11476"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-oxo-glutaryl-[acp] methyl ester reductase

`reaction.ecocyc.RXN-11476`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11476`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Hydroxyglutaryl-ACP-methyl-ester + NADP -> 3-Ketoglutaryl-ACP-methyl-ester + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: 3-Hydroxyglutaryl-ACP-methyl-ester + NADP -> 3-Ketoglutaryl-ACP-methyl-ester + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl-carrier-protein] reductase FabG (complex.ecocyc.CPLX0-8005). Substrates: NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

3-Hydroxyglutaryl-ACP-methyl-ester + NADP -> 3-Ketoglutaryl-ACP-methyl-ester + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

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

- `EcoCyc:RXN-11476`

## Notes

3-Hydroxyglutaryl-ACP-methyl-ester + NADP -> 3-Ketoglutaryl-ACP-methyl-ester + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
