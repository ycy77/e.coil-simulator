---
entity_id: "reaction.ecocyc.3.1.27.5-RXN"
entity_type: "reaction"
name: "3.1.27.5-RXN"
source_database: "EcoCyc"
source_id: "3.1.27.5-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.27.5-RXN

`reaction.ecocyc.3.1.27.5-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.27.5-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA-Holder + WATER -> 3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNA-Holder + WATER -> 3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), RNA (molecule.C00046). Products: H+ (molecule.C00080).

## Annotation

RNA-Holder + WATER -> 3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.27.5-RXN`

## Notes

RNA-Holder + WATER -> 3-Prime-Phosphate-Terminated-RNAs + 5Prime-OH-Terminated-RNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
