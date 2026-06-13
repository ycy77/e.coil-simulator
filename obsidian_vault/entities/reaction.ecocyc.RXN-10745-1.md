---
entity_id: "reaction.ecocyc.RXN-10745-1"
entity_type: "reaction"
name: "RXN-10745-1"
source_database: "EcoCyc"
source_id: "RXN-10745-1"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-10745-1

`reaction.ecocyc.RXN-10745-1`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-10745-1`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADH-P-OR-NOP + OXYGEN-MOLECULE -> NAD-P-OR-NOP + HYDROGEN-PEROXIDE + SUPER-OXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NADH-P-OR-NOP + OXYGEN-MOLECULE -> NAD-P-OR-NOP + HYDROGEN-PEROXIDE + SUPER-OXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: Hydrogen peroxide (molecule.C00027), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP), superoxide (molecule.ecocyc.SUPER-OXIDE).

## Annotation

NADH-P-OR-NOP + OXYGEN-MOLECULE -> NAD-P-OR-NOP + HYDROGEN-PEROXIDE + SUPER-OXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-10745-1`

## Notes

NADH-P-OR-NOP + OXYGEN-MOLECULE -> NAD-P-OR-NOP + HYDROGEN-PEROXIDE + SUPER-OXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
