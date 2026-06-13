---
entity_id: "reaction.ecocyc.RXN-12445"
entity_type: "reaction"
name: "RXN-12445"
source_database: "EcoCyc"
source_id: "RXN-12445"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12445

`reaction.ecocyc.RXN-12445`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12445`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-316 + NAD-P-OR-NOP -> RIBOFLAVIN + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-316 + NAD-P-OR-NOP -> RIBOFLAVIN + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by fre (protein.P0AEN1). Substrates: Reduced riboflavin (molecule.C01007), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), Riboflavin (molecule.C00255), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

CPD-316 + NAD-P-OR-NOP -> RIBOFLAVIN + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEN1|protein.P0AEN1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01007|molecule.C01007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12445`

## Notes

CPD-316 + NAD-P-OR-NOP -> RIBOFLAVIN + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
