---
entity_id: "molecule.C00017"
entity_type: "small_molecule"
name: "Protein"
source_database: "KEGG"
source_id: "C00017"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Protein"
---

# Protein

`molecule.C00017`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00017`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Protein

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

KEGG compound: Protein

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R00164|reaction.R00164]] `KEGG` `database` - C00562 + C00001 <=> C00017 + C00009
- `is_substrate_of` --> [[reaction.R00162|reaction.R00162]] `KEGG` `database` - C00002 + C00017 <=> C00008 + C00562

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00017`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
