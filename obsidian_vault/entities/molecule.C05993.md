---
entity_id: "molecule.C05993"
entity_type: "small_molecule"
name: "Acetyl adenylate"
source_database: "KEGG"
source_id: "C05993"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetyl adenylate"
  - "5'-Acetylphosphoadenosine"
---

# Acetyl adenylate

`molecule.C05993`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05993`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetyl adenylate; 5'-Acetylphosphoadenosine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: Acetyl adenylate; 5'-Acetylphosphoadenosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R00316|reaction.R00316]] `KEGG` `database` - C00002 + C00033 <=> C00013 + C05993
- `is_substrate_of` --> [[reaction.R00236|reaction.R00236]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05993`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
