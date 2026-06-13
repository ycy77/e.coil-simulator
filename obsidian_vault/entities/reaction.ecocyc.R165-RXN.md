---
entity_id: "reaction.ecocyc.R165-RXN"
entity_type: "reaction"
name: "R165-RXN"
source_database: "EcoCyc"
source_id: "R165-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R165-RXN

`reaction.ecocyc.R165-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R165-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + CPD-1091 -> NADH-P-OR-NOP + CPD-389 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NAD-P-OR-NOP + CPD-1091 -> NADH-P-OR-NOP + CPD-389 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: (S)-Ureidoglycolate (molecule.C00603), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), Oxalureate (molecule.C00802), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Annotation

NAD-P-OR-NOP + CPD-1091 -> NADH-P-OR-NOP + CPD-389 + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00802|molecule.C00802]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00603|molecule.C00603]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:R165-RXN`

## Notes

NAD-P-OR-NOP + CPD-1091 -> NADH-P-OR-NOP + CPD-389 + PROTON; direction=LEFT-TO-RIGHT
