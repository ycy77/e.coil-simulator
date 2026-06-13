---
entity_id: "molecule.C00566"
entity_type: "small_molecule"
name: "(3S)-Citryl-CoA"
source_database: "KEGG"
source_id: "C00566"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(3S)-Citryl-CoA"
---

# (3S)-Citryl-CoA

`molecule.C00566`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00566`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (3S)-Citryl-CoA

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: (3S)-Citryl-CoA

## Pathways

- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R01323|reaction.R01323]] `KEGG` `database` - C00024 + C00158 <=> C00033 + C00566
- `is_substrate_of` --> [[reaction.R00354|reaction.R00354]] `KEGG` `database` - C00566 <=> C00024 + C00036

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00566`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
