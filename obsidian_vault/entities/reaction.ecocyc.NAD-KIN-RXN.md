---
entity_id: "reaction.ecocyc.NAD-KIN-RXN"
entity_type: "reaction"
name: "NAD-KIN-RXN"
source_database: "EcoCyc"
source_id: "NAD-KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NAD-KIN-RXN

`reaction.ecocyc.NAD-KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAD-KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction can adjust the turnover and sizes of the pools of `NAD + NADH' and `NADP + NADPH'. EcoCyc reaction equation: NAD + ATP -> PROTON + NADP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction can adjust the turnover and sizes of the pools of `NAD + NADH' and `NADP + NADPH'.

## Biological Role

Catalyzed by NAD kinase (complex.ecocyc.CPLX0-682). Substrates: ATP (molecule.C00002), NAD+ (molecule.C00003). Products: NADP+ (molecule.C00006), ADP (molecule.C00008), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Annotation

This reaction can adjust the turnover and sizes of the pools of `NAD + NADH' and `NADP + NADPH'.

## Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-682|complex.ecocyc.CPLX0-682]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NAD-KIN-RXN`

## Notes

NAD + ATP -> PROTON + NADP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
