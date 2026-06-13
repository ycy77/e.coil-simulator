---
entity_id: "molecule.C05757"
entity_type: "small_molecule"
name: "(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein]"
source_database: "KEGG"
source_id: "C05757"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(3R)-3-Hydroxydodecanoyl-[acyl-carrier protein]"
  - "(R)-3-Hydroxydodecanoyl-[acp]"
  - "(R)-3-Hydroxydodecanoyl-[acyl-carrier protein]"
  - "D-3-Hydroxydodecanoyl-[acp]"
  - "D-3-Hydroxydodecanoyl-[acyl-carrier protein]"
---

# (3R)-3-Hydroxydodecanoyl-[acyl-carrier protein]

`molecule.C05757`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05757`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (3R)-3-Hydroxydodecanoyl-[acyl-carrier protein]; (R)-3-Hydroxydodecanoyl-[acp]; (R)-3-Hydroxydodecanoyl-[acyl-carrier protein]; D-3-Hydroxydodecanoyl-[acp]; D-3-Hydroxydodecanoyl-[acyl-carrier protein]

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: (3R)-3-Hydroxydodecanoyl-[acyl-carrier protein]; (R)-3-Hydroxydodecanoyl-[acp]; (R)-3-Hydroxydodecanoyl-[acyl-carrier protein]; D-3-Hydroxydodecanoyl-[acp]; D-3-Hydroxydodecanoyl-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R04964|reaction.R04964]] `KEGG` `database` - C05757 + C00006 <=> C05756 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R04965|reaction.R04965]] `KEGG` `database` - C05757 <=> C05758 + C00001

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05757`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
