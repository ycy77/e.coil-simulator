---
entity_id: "molecule.C03069"
entity_type: "small_molecule"
name: "3-Methylcrotonyl-CoA"
source_database: "KEGG"
source_id: "C03069"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3-Methylcrotonyl-CoA"
  - "3-Methylbut-2-enoyl-CoA"
  - "3-Methylcrotonoyl-CoA"
  - "Dimethylacryloyl-CoA"
---

# 3-Methylcrotonyl-CoA

`molecule.C03069`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03069`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3-Methylcrotonyl-CoA; 3-Methylbut-2-enoyl-CoA; 3-Methylcrotonoyl-CoA; Dimethylacryloyl-CoA

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)

## Annotation

KEGG compound: 3-Methylcrotonyl-CoA; 3-Methylbut-2-enoyl-CoA; 3-Methylcrotonoyl-CoA; Dimethylacryloyl-CoA

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.R04137|reaction.R04137]] `KEGG` `database` - C05998 <=> C03069 + C00001
- `is_product_of` --> [[reaction.ecocyc.RXN0-2301|reaction.ecocyc.RXN0-2301]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03069`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
