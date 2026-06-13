---
entity_id: "molecule.C05752"
entity_type: "small_molecule"
name: "Octanoyl-[acp]"
source_database: "KEGG"
source_id: "C05752"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Octanoyl-[acp]"
  - "Octanoyl-[acyl-carrier protein]"
---

# Octanoyl-[acp]

`molecule.C05752`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05752`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Octanoyl-[acp]; Octanoyl-[acyl-carrier protein]

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Octanoyl-[acp]; Octanoyl-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R04958|reaction.R04958]] `KEGG` `database` - C05752 + C00003 <=> C05751 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04959|reaction.R04959]] `KEGG` `database` - C05752 + C00006 <=> C05751 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04960|reaction.R04960]] `KEGG` `database` - C05752 + C01209 <=> C05753 + C00011 + C00229
- `is_substrate_of` --> [[reaction.R07766|reaction.R07766]] `KEGG` `database` - C05752 + C16240 <=> C16236 + C00229

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05752`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
