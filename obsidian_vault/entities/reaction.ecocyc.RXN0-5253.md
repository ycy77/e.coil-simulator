---
entity_id: "reaction.ecocyc.RXN0-5253"
entity_type: "reaction"
name: "RXN0-5253"
source_database: "EcoCyc"
source_id: "RXN0-5253"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5253

`reaction.ecocyc.RXN0-5253`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5253`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBON-DIOXIDE + PROTON + E- -> FORMATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CARBON-DIOXIDE + PROTON + E- -> FORMATE; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: CO2 (molecule.C00011), H+ (molecule.C00080). Products: Formate (molecule.C00058).

## Annotation

CARBON-DIOXIDE + PROTON + E- -> FORMATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5253`

## Notes

CARBON-DIOXIDE + PROTON + E- -> FORMATE; direction=LEFT-TO-RIGHT
