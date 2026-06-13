---
entity_id: "reaction.ecocyc.R621-RXN"
entity_type: "reaction"
name: "R621-RXN"
source_database: "EcoCyc"
source_id: "R621-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R621-RXN

`reaction.ecocyc.R621-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R621-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADH-P-OR-NOP + NITRIC-OXIDE + OXYGEN-MOLECULE -> NAD-P-OR-NOP + NITRATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NADH-P-OR-NOP + NITRIC-OXIDE + OXYGEN-MOLECULE -> NAD-P-OR-NOP + NITRATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hmp (protein.P24232). Substrates: Oxygen (molecule.C00007), Nitric oxide (molecule.C00533), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H+ (molecule.C00080), Nitrate (molecule.C00244), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP).

## Annotation

NADH-P-OR-NOP + NITRIC-OXIDE + OXYGEN-MOLECULE -> NAD-P-OR-NOP + NITRATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P24232|protein.P24232]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4501|molecule.ecocyc.CPD-4501]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:R621-RXN`

## Notes

NADH-P-OR-NOP + NITRIC-OXIDE + OXYGEN-MOLECULE -> NAD-P-OR-NOP + NITRATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
