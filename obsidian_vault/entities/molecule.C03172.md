---
entity_id: "molecule.C03172"
entity_type: "small_molecule"
name: "S-Methyl-L-methionine"
source_database: "KEGG"
source_id: "C03172"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "S-Methyl-L-methionine"
---

# S-Methyl-L-methionine

`molecule.C03172`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03172`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: S-Methyl-L-methionine

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: S-Methyl-L-methionine

## Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-486|reaction.ecocyc.TRANS-RXN0-486]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MMUM-RXN|reaction.ecocyc.MMUM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-486|reaction.ecocyc.TRANS-RXN0-486]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03172`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
