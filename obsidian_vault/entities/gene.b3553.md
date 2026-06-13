---
entity_id: "gene.b3553"
entity_type: "gene"
name: "ghrB"
source_database: "NCBI RefSeq"
source_id: "gene-b3553"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3553"
  - "ghrB"
---

# ghrB

`gene.b3553`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3553`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ghrB (gene.b3553) is a gene entity. It encodes ghrB (protein.P37666). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Can also reduce 2,5-diketo-D-gluconate (25DKG) to 5-keto-D-gluconate (5KDG), 2-keto-D-gluconate (2KDG) to D-gluconate, and 2-keto-L-gulonate (2KLG) to L-idonate (IA), but it is not its physiological function. Inactive towards 2-oxoglutarate, oxaloacetate, pyruvate, 5-keto-D-gluconate, D-fructose and L-sorbose. Activity with NAD is very low. EcoCyc product frame: MONOMER-43. EcoCyc synonyms: tkrA, yiaE. Genomic coordinates: 3717310-3718284.

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37666|protein.P37666]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011604,ECOCYC:EG12272,GeneID:948074`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3717310-3718284:+; feature_type=gene
