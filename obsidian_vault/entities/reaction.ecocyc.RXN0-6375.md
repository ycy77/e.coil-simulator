---
entity_id: "reaction.ecocyc.RXN0-6375"
entity_type: "reaction"
name: "RXN0-6375"
source_database: "EcoCyc"
source_id: "RXN0-6375"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6375

`reaction.ecocyc.RXN0-6375`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6375`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACET + CARBON-DIOXIDE + PROTON + E- -> PYRUVATE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ACET + CARBON-DIOXIDE + PROTON + E- -> PYRUVATE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: CO2 (molecule.C00011), Acetate (molecule.C00033), H+ (molecule.C00080). Products: H2O (molecule.C00001), Pyruvate (molecule.C00022).

## Annotation

ACET + CARBON-DIOXIDE + PROTON + E- -> PYRUVATE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6375`

## Notes

ACET + CARBON-DIOXIDE + PROTON + E- -> PYRUVATE + WATER; direction=LEFT-TO-RIGHT
