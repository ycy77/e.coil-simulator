---
entity_id: "molecule.ecocyc.Ions"
entity_type: "small_molecule"
name: "an ion"
source_database: "EcoCyc"
source_id: "Ions"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# an ion

`molecule.ecocyc.Ions`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Ions`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound Ions

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

EcoCyc compound Ions

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-601|reaction.ecocyc.TRANS-RXN0-601]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-601|reaction.ecocyc.TRANS-RXN0-601]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:Ions`
