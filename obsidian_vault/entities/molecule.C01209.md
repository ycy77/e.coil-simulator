---
entity_id: "molecule.C01209"
entity_type: "small_molecule"
name: "Malonyl-[acyl-carrier protein]"
source_database: "KEGG"
source_id: "C01209"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Malonyl-[acyl-carrier protein]"
  - "Malonyl-[acp]"
---

# Malonyl-[acyl-carrier protein]

`molecule.C01209`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01209`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Malonyl-[acyl-carrier protein]; Malonyl-[acp]

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)

## Annotation

KEGG compound: Malonyl-[acyl-carrier protein]; Malonyl-[acp]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R04726|reaction.R04726]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_substrate_of` --> [[reaction.R04957|reaction.R04957]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_substrate_of` --> [[reaction.R04960|reaction.R04960]] `KEGG` `database` - C05752 + C01209 <=> C05753 + C00011 + C00229
- `is_substrate_of` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - C05755 + C01209 <=> C05756 + C00011 + C00229

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01209`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
