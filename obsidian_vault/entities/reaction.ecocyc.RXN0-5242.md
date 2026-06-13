---
entity_id: "reaction.ecocyc.RXN0-5242"
entity_type: "reaction"
name: "RXN0-5242"
source_database: "EcoCyc"
source_id: "RXN0-5242"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5242

`reaction.ecocyc.RXN0-5242`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5242`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NITRATE + PROTON + E- -> NITRITE + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NITRATE + PROTON + E- -> NITRITE + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Nitrate (molecule.C00244). Products: H2O (molecule.C00001), Nitrite (molecule.C00088).

## Annotation

NITRATE + PROTON + E- -> NITRITE + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5242`

## Notes

NITRATE + PROTON + E- -> NITRITE + WATER; direction=LEFT-TO-RIGHT
