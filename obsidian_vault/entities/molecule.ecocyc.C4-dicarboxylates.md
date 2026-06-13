---
entity_id: "molecule.ecocyc.C4-dicarboxylates"
entity_type: "small_molecule"
name: "a C4-dicarboxylate"
source_database: "EcoCyc"
source_id: "C4-dicarboxylates"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "C4-dicarboxylate"
---

# a C4-dicarboxylate

`molecule.ecocyc.C4-dicarboxylates`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:C4-dicarboxylates`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound C4-dicarboxylates

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

EcoCyc compound C4-dicarboxylates

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-517|reaction.ecocyc.TRANS-RXN0-517]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-517|reaction.ecocyc.TRANS-RXN0-517]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:C4-dicarboxylates`
- `SEED:cpd28713`
- `METANETX:MNXM45131`
