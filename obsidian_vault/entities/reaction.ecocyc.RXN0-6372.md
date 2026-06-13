---
entity_id: "reaction.ecocyc.RXN0-6372"
entity_type: "reaction"
name: "RXN0-6372"
source_database: "EcoCyc"
source_id: "RXN0-6372"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6372

`reaction.ecocyc.RXN0-6372`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6372`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLC-D-LACTONE + E- + PROTON -> Glucopyranose; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GLC-D-LACTONE + E- + PROTON -> Glucopyranose; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), D-Glucono-1,5-lactone (molecule.C00198). Products: D-Glucose (molecule.C00031).

## Annotation

GLC-D-LACTONE + E- + PROTON -> Glucopyranose; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00198|molecule.C00198]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6372`

## Notes

GLC-D-LACTONE + E- + PROTON -> Glucopyranose; direction=LEFT-TO-RIGHT
