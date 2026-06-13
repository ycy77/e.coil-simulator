---
entity_id: "reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN"
entity_type: "reaction"
name: "ENOYL-ACP-REDUCT-NADH-RXN"
source_database: "EcoCyc"
source_id: "ENOYL-ACP-REDUCT-NADH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENOYL-ACP-REDUCT-NADH-RXN

`reaction.ecocyc.ENOYL-ACP-REDUCT-NADH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENOYL-ACP-REDUCT-NADH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

One of two final reduction reactions in fatty acid biosynthesis. EcoCyc reaction equation: Saturated-Fatty-Acyl-ACPs + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. One of two final reduction reactions in fatty acid biosynthesis.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Annotation

One of two final reduction reactions in fatty acid biosynthesis.

## Pathways

- `ecocyc.FASYN-ELONG-PWY` fatty acid elongation -- saturated (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1227|molecule.ecocyc.CPD0-1227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1228|molecule.ecocyc.CPD0-1228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ENOYL-ACP-REDUCT-NADH-RXN`

## Notes

Saturated-Fatty-Acyl-ACPs + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
