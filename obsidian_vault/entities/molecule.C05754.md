---
entity_id: "molecule.C05754"
entity_type: "small_molecule"
name: "trans-Dec-2-enoyl-[acp]"
source_database: "KEGG"
source_id: "C05754"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-Dec-2-enoyl-[acp]"
  - "trans-Dec-2-enoyl-[acyl-carrier protein]"
  - "trans-2-Decenoyl-[acyl-carrier protein]"
  - "(2E)-Decenoyl-[acp]"
---

# trans-Dec-2-enoyl-[acp]

`molecule.C05754`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05754`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-Dec-2-enoyl-[acp]; trans-Dec-2-enoyl-[acyl-carrier protein]; trans-2-Decenoyl-[acyl-carrier protein]; (2E)-Decenoyl-[acp]

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: trans-Dec-2-enoyl-[acp]; trans-Dec-2-enoyl-[acyl-carrier protein]; trans-2-Decenoyl-[acyl-carrier protein]; (2E)-Decenoyl-[acp]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R04961|reaction.R04961]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_product_of` --> [[reaction.R04962|reaction.R04962]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05754`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
