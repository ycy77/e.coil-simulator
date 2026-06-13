---
entity_id: "molecule.C00512"
entity_type: "small_molecule"
name: "Benzoyl-CoA"
source_database: "KEGG"
source_id: "C00512"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Benzoyl-CoA"
  - "S-Benzoyl-coenzyme A"
---

# Benzoyl-CoA

`molecule.C00512`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00512`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Benzoyl-CoA; S-Benzoyl-coenzyme A

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: Benzoyl-CoA; S-Benzoyl-coenzyme A

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (1)

- `is_product_of` --> [[reaction.R05506|reaction.R05506]] `KEGG` `database` - C07118 + C00010 <=> C00512 + C00024

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00512`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
