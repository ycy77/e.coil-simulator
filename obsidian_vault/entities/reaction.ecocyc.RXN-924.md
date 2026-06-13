---
entity_id: "reaction.ecocyc.RXN-924"
entity_type: "reaction"
name: "RXN-924"
source_database: "EcoCyc"
source_id: "RXN-924"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-924

`reaction.ecocyc.RXN-924`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-924`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADP + PROTON + E- -> NADPH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NADP + PROTON + E- -> NADPH; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NADP+ (molecule.C00006), H+ (molecule.C00080). Products: NADPH (molecule.C00005).

## Annotation

NADP + PROTON + E- -> NADPH; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-924`

## Notes

NADP + PROTON + E- -> NADPH; direction=LEFT-TO-RIGHT
