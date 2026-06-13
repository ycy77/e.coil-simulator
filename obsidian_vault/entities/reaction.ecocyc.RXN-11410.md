---
entity_id: "reaction.ecocyc.RXN-11410"
entity_type: "reaction"
name: "RXN-11410"
source_database: "EcoCyc"
source_id: "RXN-11410"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11410

`reaction.ecocyc.RXN-11410`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11410`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DGTP + CPD-12377 -> 8-Oxo-dGTP + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DGTP + CPD-12377 -> 8-Oxo-dGTP + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: dGTP (molecule.C00286), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), 8-oxo-dGTP (molecule.ecocyc.8-Oxo-dGTP).

## Annotation

DGTP + CPD-12377 -> 8-Oxo-dGTP + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.8-Oxo-dGTP|molecule.ecocyc.8-Oxo-dGTP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11410`

## Notes

DGTP + CPD-12377 -> 8-Oxo-dGTP + WATER; direction=LEFT-TO-RIGHT
