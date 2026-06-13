---
entity_id: "reaction.ecocyc.RXN-20079"
entity_type: "reaction"
name: "RXN-20079"
source_database: "EcoCyc"
source_id: "RXN-20079"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20079

`reaction.ecocyc.RXN-20079`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20079`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROXYPROPANAL + WATER -> CPD-21703; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HYDROXYPROPANAL + WATER -> CPD-21703; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), 3-Hydroxypropanal (molecule.C00969). Products: 3-hydroxypropanal hydrate (molecule.ecocyc.CPD-21703).

## Annotation

HYDROXYPROPANAL + WATER -> CPD-21703; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-21703|molecule.ecocyc.CPD-21703]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00969|molecule.C00969]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20079`

## Notes

HYDROXYPROPANAL + WATER -> CPD-21703; direction=PHYSIOL-LEFT-TO-RIGHT
