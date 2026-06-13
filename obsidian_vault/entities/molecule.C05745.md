---
entity_id: "molecule.C05745"
entity_type: "small_molecule"
name: "Butyryl-[acp]"
source_database: "KEGG"
source_id: "C05745"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Butyryl-[acp]"
  - "Butyryl-[acyl-carrier protein]"
  - "Butanoyl-[acp]"
---

# Butyryl-[acp]

`molecule.C05745`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05745`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Butyryl-[acp]; Butyryl-[acyl-carrier protein]; Butanoyl-[acp]

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: Butyryl-[acp]; Butyryl-[acyl-carrier protein]; Butanoyl-[acp]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R04429|reaction.R04429]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R04430|reaction.R04430]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05745`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
