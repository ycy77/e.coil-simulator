---
entity_id: "reaction.ecocyc.CROBETREDUCT-RXN"
entity_type: "reaction"
name: "CROBETREDUCT-RXN"
source_database: "EcoCyc"
source_id: "CROBETREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CROBETREDUCT-RXN

`reaction.ecocyc.CROBETREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CROBETREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in carnitine metabolism. EcoCyc reaction equation: GAMMA-BUTYROBETAINYL-COA + ETF-Oxidized + PROTON -> CROTONOBETAINYL-COA + ETF-Reduced; direction=PHYSIOL-RIGHT-TO-LEFT. This is a reaction in carnitine metabolism.

## Biological Role

Catalyzed by caiA (protein.P60584). Substrates: H+ (molecule.C00080), γ-butyrobetainyl-CoA (molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA). Products: crotonobetainyl-CoA (molecule.ecocyc.CROTONOBETAINYL-COA).

## Enriched Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Annotation

This is a reaction in carnitine metabolism.

## Pathways

- `ecocyc.CARNMET-PWY` L-carnitine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P60584|protein.P60584]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CROTONOBETAINYL-COA|molecule.ecocyc.CROTONOBETAINYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA|molecule.ecocyc.GAMMA-BUTYROBETAINYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01181|molecule.C01181]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.D-CARNITINE|molecule.ecocyc.D-CARNITINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CROBETREDUCT-RXN`

## Notes

GAMMA-BUTYROBETAINYL-COA + ETF-Oxidized + PROTON -> CROTONOBETAINYL-COA + ETF-Reduced; direction=PHYSIOL-RIGHT-TO-LEFT
