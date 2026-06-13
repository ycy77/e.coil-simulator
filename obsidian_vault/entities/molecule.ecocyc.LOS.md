---
entity_id: "molecule.ecocyc.LOS"
entity_type: "small_molecule"
name: "a lipid A-core oligosaccharide"
source_database: "EcoCyc"
source_id: "LOS"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a rough-form LPS"
  - "an (R)-form LPS"
  - "a lipooligosaccharide"
  - "a lipid A-core"
  - "a core oligosaccharide-lipid A"
  - "a rough-form lipopolysaccharide"
---

# a lipid A-core oligosaccharide

`molecule.ecocyc.LOS`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:LOS`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

EcoCyc compound LOS

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

EcoCyc compound LOS

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-236|reaction.ecocyc.TRANS-RXN-236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-236|reaction.ecocyc.TRANS-RXN-236]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-7704|complex.ecocyc.CPLX0-7704]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:LOS`
- `CHEBI:62004`
- `PUBCHEM:91972194`
