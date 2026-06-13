---
entity_id: "reaction.ecocyc.FMNREDUCT-RXN"
entity_type: "reaction"
name: "FMNREDUCT-RXN"
source_database: "EcoCyc"
source_id: "FMNREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FMNREDUCT-RXN

`reaction.ecocyc.FMNREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FMNREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction reduces flavins. In some circumstances it produces the free reduced flavins needed for the activation of the ribonucleoside-diphosphate reductase β subunit. EcoCyc reaction equation: NAD-P-OR-NOP + FMNH2 -> NADH-P-OR-NOP + FMN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction reduces flavins. In some circumstances it produces the free reduced flavins needed for the activation of the ribonucleoside-diphosphate reductase β subunit.

## Biological Role

Catalyzed by fre (protein.P0AEN1). Substrates: Reduced FMN (molecule.C01847), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: FMN (molecule.C00061), H+ (molecule.C00080), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

This reaction reduces flavins. In some circumstances it produces the free reduced flavins needed for the activation of the ribonucleoside-diphosphate reductase β subunit.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0AEN1|protein.P0AEN1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01727|molecule.C01727]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FMNREDUCT-RXN`

## Notes

NAD-P-OR-NOP + FMNH2 -> NADH-P-OR-NOP + FMN + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
