---
entity_id: "molecule.C00282"
entity_type: "small_molecule"
name: "Hydrogen"
source_database: "KEGG"
source_id: "C00282"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydrogen"
  - "H2"
---

# Hydrogen

`molecule.C00282`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00282`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydrogen; H2 EcoCyc common name: H2.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Hydrogen; H2

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.FHLMULTI-RXN|reaction.ecocyc.FHLMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5255|reaction.ecocyc.RXN0-5255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-610|reaction.ecocyc.TRANS-RXN0-610]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.HYDROG-RXN|reaction.ecocyc.HYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16420|reaction.ecocyc.RXN-16420]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5256|reaction.ecocyc.RXN0-5256]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7399|reaction.ecocyc.RXN0-7399]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-610|reaction.ecocyc.TRANS-RXN0-610]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00282`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
