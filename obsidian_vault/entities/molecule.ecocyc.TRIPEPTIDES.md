---
entity_id: "molecule.ecocyc.TRIPEPTIDES"
entity_type: "small_molecule"
name: "a tripeptide"
source_database: "EcoCyc"
source_id: "TRIPEPTIDES"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a tripeptide

`molecule.ecocyc.TRIPEPTIDES`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:TRIPEPTIDES`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound TRIPEPTIDES

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Annotation

EcoCyc compound TRIPEPTIDES

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-267|reaction.ecocyc.TRANS-RXN0-267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.4.11.4-RXN|reaction.ecocyc.3.4.11.4-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-267|reaction.ecocyc.TRANS-RXN0-267]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P39276|protein.P39276]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:TRIPEPTIDES`
- `SEED:cpd28237`
- `METANETX:MNXM88106`
