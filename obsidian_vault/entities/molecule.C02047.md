---
entity_id: "molecule.C02047"
entity_type: "small_molecule"
name: "L-Leucyl-tRNA"
source_database: "KEGG"
source_id: "C02047"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Leucyl-tRNA"
  - "L-Leucyl-tRNA(Leu)"
---

# L-Leucyl-tRNA

`molecule.C02047`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02047`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Leucyl-tRNA; L-Leucyl-tRNA(Leu)

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

KEGG compound: L-Leucyl-tRNA; L-Leucyl-tRNA(Leu)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `is_substrate_of` --> [[reaction.R11443|reaction.R11443]] `KEGG` `database` - C02047 + C21388 <=> C01645 + C21387
- `is_substrate_of` --> [[reaction.R11444|reaction.R11444]] `KEGG` `database` - C02047 + C16739 <=> C01645 + C21386

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02047`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
