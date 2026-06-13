---
entity_id: "molecule.C06481"
entity_type: "small_molecule"
name: "L-Seryl-tRNA(Sec)"
source_database: "KEGG"
source_id: "C06481"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Seryl-tRNA(Sec)"
---

# L-Seryl-tRNA(Sec)

`molecule.C06481`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06481`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Seryl-tRNA(Sec)

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

KEGG compound: L-Seryl-tRNA(Sec)

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R08218|reaction.R08218]] `KEGG` `database` - C00002 + C00065 + C16636 <=> C00020 + C00013 + C06481
- `is_substrate_of` --> [[reaction.R08219|reaction.R08219]] `KEGG` `database` - C06481 + C05172 <=> C06482 + C00009

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06481`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
