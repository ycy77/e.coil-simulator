---
entity_id: "molecule.C05756"
entity_type: "small_molecule"
name: "3-Oxododecanoyl-[acp]"
source_database: "KEGG"
source_id: "C05756"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Oxododecanoyl-[acp]"
  - "3-Oxododecanoyl-[acyl-carrier protein]"
---

# 3-Oxododecanoyl-[acp]

`molecule.C05756`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05756`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Oxododecanoyl-[acp]; 3-Oxododecanoyl-[acyl-carrier protein]

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: 3-Oxododecanoyl-[acp]; 3-Oxododecanoyl-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - C05755 + C01209 <=> C05756 + C00011 + C00229
- `is_product_of` --> [[reaction.R04964|reaction.R04964]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05756`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
