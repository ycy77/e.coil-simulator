---
entity_id: "molecule.C01102"
entity_type: "small_molecule"
name: "O-Phospho-L-homoserine"
source_database: "KEGG"
source_id: "C01102"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "O-Phospho-L-homoserine"
---

# O-Phospho-L-homoserine

`molecule.C01102`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01102`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: O-Phospho-L-homoserine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)

## Annotation

KEGG compound: O-Phospho-L-homoserine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.HOMOSERKIN-RXN|reaction.ecocyc.HOMOSERKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.THRESYN-RXN|reaction.ecocyc.THRESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01102`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
