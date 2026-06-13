---
entity_id: "gene.b2019"
entity_type: "gene"
name: "hisG"
source_database: "NCBI RefSeq"
source_id: "gene-b2019"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2019"
  - "hisG"
---

# hisG

`gene.b2019`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2019`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisG (gene.b2019) is a gene entity. It encodes hisG (protein.P60757). Encoded protein function: FUNCTION: Catalyzes the condensation of ATP and 5-phosphoribose 1-diphosphate to form N'-(5'-phosphoribosyl)-ATP (PR-ATP). Has a crucial role in the pathway because the rate of histidine biosynthesis seems to be controlled primarily by regulation of HisG enzymatic activity. {ECO:0000269|PubMed:4909873}. EcoCyc product frame: ATPPHOSRIBOSTRANS-MONOMER. Genomic coordinates: 2090192-2091091.

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60757|protein.P60757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006713,ECOCYC:EG10449,GeneID:946549`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2090192-2091091:+; feature_type=gene
