---
entity_id: "reaction.ecocyc.RXN0-5248"
entity_type: "reaction"
name: "RXN0-5248"
source_database: "EcoCyc"
source_id: "RXN0-5248"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5248

`reaction.ecocyc.RXN0-5248`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5248`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + PROTON + E- -> NADH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NAD + PROTON + E- -> NADH; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), H+ (molecule.C00080). Products: NADH (molecule.C00004).

## Annotation

NAD + PROTON + E- -> NADH; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5248`

## Notes

NAD + PROTON + E- -> NADH; direction=LEFT-TO-RIGHT
