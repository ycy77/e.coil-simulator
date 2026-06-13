---
entity_id: "reaction.ecocyc.RXN0-7080"
entity_type: "reaction"
name: "RXN0-7080"
source_database: "EcoCyc"
source_id: "RXN0-7080"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7080

`reaction.ecocyc.RXN0-7080`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7080`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + CPD-12377 -> 5-HYDROXY-CTP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CTP + CPD-12377 -> 5-HYDROXY-CTP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: CTP (molecule.C00063), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: H2O (molecule.C00001), 5-hydroxy-CTP (molecule.ecocyc.5-HYDROXY-CTP).

## Annotation

CTP + CPD-12377 -> 5-HYDROXY-CTP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-HYDROXY-CTP|molecule.ecocyc.5-HYDROXY-CTP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7080`

## Notes

CTP + CPD-12377 -> 5-HYDROXY-CTP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
