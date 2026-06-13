---
entity_id: "reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN"
entity_type: "reaction"
name: "ACETOLACTREDUCTOISOM-RXN"
source_database: "EcoCyc"
source_id: "ACETOLACTREDUCTOISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETOLACTREDUCTOISOM-RXN

`reaction.ecocyc.ACETOLACTREDUCTOISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETOLACTREDUCTOISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second shared reaction in the valine and leucine biosynthetic pathways. After three steps in common, the pathway forks to either valine or leucine. EcoCyc reaction equation: CPD-13357 + NADP -> 2-ACETO-LACTATE + NADPH + PROTON; direction=RIGHT-TO-LEFT. This is the second shared reaction in the valine and leucine biosynthetic pathways. After three steps in common, the pathway forks to either valine or leucine.

## Biological Role

Catalyzed by ketol-acid reductoisomerase (NADP+) (complex.ecocyc.CPLX0-7643). Substrates: NADP+ (molecule.C00006), (R)-2,3-Dihydroxy-3-methylbutanoate (molecule.C04272). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (S)-2-Acetolactate (molecule.C06010).

## Enriched Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Annotation

This is the second shared reaction in the valine and leucine biosynthetic pathways. After three steps in common, the pathway forks to either valine or leucine.

## Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7643|complex.ecocyc.CPLX0-7643]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06010|molecule.C06010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04272|molecule.C04272]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1218|molecule.ecocyc.CPD0-1218]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1220|molecule.ecocyc.CPD0-1220]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIOH-ISOVALERATE|molecule.ecocyc.DIOH-ISOVALERATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETOLACTREDUCTOISOM-RXN`

## Notes

CPD-13357 + NADP -> 2-ACETO-LACTATE + NADPH + PROTON; direction=RIGHT-TO-LEFT
