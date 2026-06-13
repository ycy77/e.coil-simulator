---
entity_id: "molecule.C05223"
entity_type: "small_molecule"
name: "Dodecanoyl-[acyl-carrier protein]"
source_database: "KEGG"
source_id: "C05223"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dodecanoyl-[acyl-carrier protein]"
  - "Dodecanoyl-[acp]"
  - "Lauroyl-[acyl-carrier protein]"
---

# Dodecanoyl-[acyl-carrier protein]

`molecule.C05223`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05223`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dodecanoyl-[acyl-carrier protein]; Dodecanoyl-[acp]; Lauroyl-[acyl-carrier protein]

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: Dodecanoyl-[acyl-carrier protein]; Dodecanoyl-[acp]; Lauroyl-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R04724|reaction.R04724]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04725|reaction.R04725]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04726|reaction.R04726]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05223`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
