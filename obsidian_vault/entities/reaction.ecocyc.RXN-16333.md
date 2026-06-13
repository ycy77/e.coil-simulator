---
entity_id: "reaction.ecocyc.RXN-16333"
entity_type: "reaction"
name: "RXN-16333"
source_database: "EcoCyc"
source_id: "RXN-16333"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16333

`reaction.ecocyc.RXN-16333`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16333`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + PROTON + E- -> NADH-P-OR-NOP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NAD-P-OR-NOP + PROTON + E- -> NADH-P-OR-NOP; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Annotation

NAD-P-OR-NOP + PROTON + E- -> NADH-P-OR-NOP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16333`

## Notes

NAD-P-OR-NOP + PROTON + E- -> NADH-P-OR-NOP; direction=LEFT-TO-RIGHT
