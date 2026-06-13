---
entity_id: "reaction.ecocyc.RXN-16330"
entity_type: "reaction"
name: "RXN-16330"
source_database: "EcoCyc"
source_id: "RXN-16330"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16330

`reaction.ecocyc.RXN-16330`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16330`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTOPORPHYRIN_IX + PROTON + E- -> PROTOPORPHYRINOGEN; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTOPORPHYRIN_IX + PROTON + E- -> PROTOPORPHYRINOGEN; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), Protoporphyrin (molecule.C02191). Products: Protoporphyrinogen IX (molecule.C01079).

## Annotation

PROTOPORPHYRIN_IX + PROTON + E- -> PROTOPORPHYRINOGEN; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16330`

## Notes

PROTOPORPHYRIN_IX + PROTON + E- -> PROTOPORPHYRINOGEN; direction=LEFT-TO-RIGHT
