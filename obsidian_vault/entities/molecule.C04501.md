---
entity_id: "molecule.C04501"
entity_type: "small_molecule"
name: "N-Acetyl-alpha-D-glucosamine 1-phosphate"
source_database: "KEGG"
source_id: "C04501"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-alpha-D-glucosamine 1-phosphate"
---

# N-Acetyl-alpha-D-glucosamine 1-phosphate

`molecule.C04501`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04501`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-alpha-D-glucosamine 1-phosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: N-Acetyl-alpha-D-glucosamine 1-phosphate

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R05332|reaction.R05332]] `KEGG` `database` - C00024 + C06156 <=> C00010 + C04501
- `is_substrate_of` --> [[reaction.R00416|reaction.R00416]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04501`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
