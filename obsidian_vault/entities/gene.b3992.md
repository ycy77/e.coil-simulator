---
entity_id: "gene.b3992"
entity_type: "gene"
name: "thiF"
source_database: "NCBI RefSeq"
source_id: "gene-b3992"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3992"
  - "thiF"
---

# thiF

`gene.b3992`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3992`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiF (gene.b3992) is a gene entity. It encodes thiF (protein.P30138). Encoded protein function: FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein ThiS. EcoCyc product frame: THIF-MONOMER. EcoCyc synonyms: thiA. Genomic coordinates: 4192821-4193576.

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30138|protein.P30138]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013053,ECOCYC:EG11587,GeneID:948500`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4192821-4193576:-; feature_type=gene
