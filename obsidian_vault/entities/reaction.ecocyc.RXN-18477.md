---
entity_id: "reaction.ecocyc.RXN-18477"
entity_type: "reaction"
name: "RXN-18477"
source_database: "EcoCyc"
source_id: "RXN-18477"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18477

`reaction.ecocyc.RXN-18477`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18477`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15826 -> CPD-15709; direction=REVERSIBLE EcoCyc reaction equation: CPD-15826 -> CPD-15709; direction=REVERSIBLE.

## Biological Role

Catalyzed by gatZ (protein.P0C8J8), kbaZ (protein.P0C8K0). Substrates: keto-D-tagatose 6-phosphate (molecule.ecocyc.CPD-15826). Products: keto-D-fructose 6-phosphate (molecule.ecocyc.CPD-15709).

## Annotation

CPD-15826 -> CPD-15709; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0C8J8|protein.P0C8J8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C8K0|protein.P0C8K0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15709|molecule.ecocyc.CPD-15709]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15826|molecule.ecocyc.CPD-15826]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18477`

## Notes

CPD-15826 -> CPD-15709; direction=REVERSIBLE
