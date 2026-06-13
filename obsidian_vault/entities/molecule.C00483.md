---
entity_id: "molecule.C00483"
entity_type: "small_molecule"
name: "Tyramine"
source_database: "KEGG"
source_id: "C00483"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Tyramine"
  - "2-(p-Hydroxyphenyl)ethylamine"
---

# Tyramine

`molecule.C00483`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00483`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Tyramine; 2-(p-Hydroxyphenyl)ethylamine

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Tyramine; 2-(p-Hydroxyphenyl)ethylamine

## Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.R02382|reaction.R02382]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00483`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
