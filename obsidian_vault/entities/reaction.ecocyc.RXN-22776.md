---
entity_id: "reaction.ecocyc.RXN-22776"
entity_type: "reaction"
name: "RXN-22776"
source_database: "EcoCyc"
source_id: "RXN-22776"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22776

`reaction.ecocyc.RXN-22776`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22776`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15374 + GLY -> CPD-26731 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15374 + GLY -> CPD-26731 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glycine (molecule.C00037), aldehydo-D-glucose (molecule.ecocyc.CPD-15374). Products: H2O (molecule.C00001), N-(1-deoxy-D-fructopyranos-1-yl)glycine (molecule.ecocyc.CPD-26731).

## Annotation

CPD-15374 + GLY -> CPD-26731 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26731|molecule.ecocyc.CPD-26731]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15374|molecule.ecocyc.CPD-15374]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22776`

## Notes

CPD-15374 + GLY -> CPD-26731 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
