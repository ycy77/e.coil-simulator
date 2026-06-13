---
entity_id: "reaction.ecocyc.RXN-11409"
entity_type: "reaction"
name: "RXN-11409"
source_database: "EcoCyc"
source_id: "RXN-11409"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11409

`reaction.ecocyc.RXN-11409`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11409`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + CPD-12377 -> CPD-12366 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GTP + CPD-12377 -> CPD-12366 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: GTP (molecule.C00044), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), 8-oxo-GTP (molecule.ecocyc.CPD-12366).

## Annotation

GTP + CPD-12377 -> CPD-12366 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12366|molecule.ecocyc.CPD-12366]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11409`

## Notes

GTP + CPD-12377 -> CPD-12366 + WATER; direction=LEFT-TO-RIGHT
