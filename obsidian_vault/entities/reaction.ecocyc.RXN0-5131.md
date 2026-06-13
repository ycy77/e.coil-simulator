---
entity_id: "reaction.ecocyc.RXN0-5131"
entity_type: "reaction"
name: "RXN0-5131"
source_database: "EcoCyc"
source_id: "RXN0-5131"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5131

`reaction.ecocyc.RXN0-5131`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5131`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

IS30-Insertion-Sequences -> IS30-with-Integrated-Transposon; direction= EcoCyc reaction equation: IS30-Insertion-Sequences -> IS30-with-Integrated-Transposon; direction=.

## Biological Role

Catalyzed by insI1 (protein.P0CF88), insI3 (protein.P0CF89), insI4 (protein.P0CF90). Substrates: an insertion sequence element IS30 (molecule.ecocyc.IS30-Insertion-Sequences). Products: an insertion sequence IS30 with integrated transposon (molecule.ecocyc.IS30-with-Integrated-Transposon).

## Annotation

IS30-Insertion-Sequences -> IS30-with-Integrated-Transposon; direction=

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0CF88|protein.P0CF88]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CF89|protein.P0CF89]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0CF90|protein.P0CF90]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.IS30-with-Integrated-Transposon|molecule.ecocyc.IS30-with-Integrated-Transposon]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.IS30-Insertion-Sequences|molecule.ecocyc.IS30-Insertion-Sequences]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5131`

## Notes

IS30-Insertion-Sequences -> IS30-with-Integrated-Transposon; direction=
