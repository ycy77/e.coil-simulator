---
entity_id: "reaction.ecocyc.RXN-9376"
entity_type: "reaction"
name: "RXN-9376"
source_database: "EcoCyc"
source_id: "RXN-9376"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9376

`reaction.ecocyc.RXN-9376`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9376`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLY + ATP -> CPD-9993 + PPI; direction= EcoCyc reaction equation: GLY + ATP -> CPD-9993 + PPI; direction=.

## Biological Role

Substrates: ATP (molecule.C00002), Glycine (molecule.C00037). Products: Diphosphate (molecule.C00013), (glycyl)adenylate (molecule.ecocyc.CPD-9993).

## Annotation

GLY + ATP -> CPD-9993 + PPI; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9993|molecule.ecocyc.CPD-9993]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9376`

## Notes

GLY + ATP -> CPD-9993 + PPI; direction=
