---
entity_id: "reaction.ecocyc.RXN0-5245"
entity_type: "reaction"
name: "RXN0-5245"
source_database: "EcoCyc"
source_id: "RXN0-5245"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5245

`reaction.ecocyc.RXN0-5245`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5245`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FUM + PROTON + E- -> SUC; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FUM + PROTON + E- -> SUC; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Fumarate (molecule.C00122). Products: Succinate (molecule.C00042).

## Annotation

FUM + PROTON + E- -> SUC; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5245`

## Notes

FUM + PROTON + E- -> SUC; direction=LEFT-TO-RIGHT
