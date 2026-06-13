---
entity_id: "molecule.C00826"
entity_type: "small_molecule"
name: "L-Arogenate"
source_database: "KEGG"
source_id: "C00826"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Arogenate"
  - "L-Arogenic acid"
  - "Pretyrosine"
---

# L-Arogenate

`molecule.C00826`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00826`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Arogenate; L-Arogenic acid; Pretyrosine

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Annotation

KEGG compound: L-Arogenate; L-Arogenic acid; Pretyrosine

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R00691|reaction.R00691]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011
- `is_substrate_of` --> [[reaction.R01731|reaction.R01731]] `KEGG` `database` - C00036 + C00826 <=> C00049 + C00254

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00826`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
