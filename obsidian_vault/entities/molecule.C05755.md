---
entity_id: "molecule.C05755"
entity_type: "small_molecule"
name: "Decanoyl-[acp]"
source_database: "KEGG"
source_id: "C05755"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Decanoyl-[acp]"
  - "Decanoyl-[acyl-carrier protein]"
---

# Decanoyl-[acp]

`molecule.C05755`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05755`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Decanoyl-[acp]; Decanoyl-[acyl-carrier protein]

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: Decanoyl-[acp]; Decanoyl-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R04961|reaction.R04961]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04962|reaction.R04962]] `KEGG` `database` - C05755 + C00006 <=> C05754 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - C05755 + C01209 <=> C05756 + C00011 + C00229

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05755`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
