---
entity_id: "reaction.ecocyc.RXN0-5263"
entity_type: "reaction"
name: "RXN0-5263"
source_database: "EcoCyc"
source_id: "RXN0-5263"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5263

`reaction.ecocyc.RXN0-5263`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5263`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRIMETHYLAMINE-N-O + PROTON + E- -> TRIMETHYLAMINE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: TRIMETHYLAMINE-N-O + PROTON + E- -> TRIMETHYLAMINE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Trimethylamine N-oxide (molecule.C01104). Products: H2O (molecule.C00001), Trimethylamine (molecule.C00565).

## Annotation

TRIMETHYLAMINE-N-O + PROTON + E- -> TRIMETHYLAMINE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5263`

## Notes

TRIMETHYLAMINE-N-O + PROTON + E- -> TRIMETHYLAMINE + WATER; direction=LEFT-TO-RIGHT
