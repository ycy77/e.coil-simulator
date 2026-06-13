---
entity_id: "molecule.C01438"
entity_type: "small_molecule"
name: "Methane"
source_database: "KEGG"
source_id: "C01438"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methane"
  - "CH4"
---

# Methane

`molecule.C01438`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01438`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methane; CH4

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Methane; CH4

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6734|reaction.ecocyc.RXN0-6734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-526|reaction.ecocyc.TRANS-RXN0-526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-526|reaction.ecocyc.TRANS-RXN0-526]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01438`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
