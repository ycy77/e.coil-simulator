---
entity_id: "gene.b3253"
entity_type: "gene"
name: "yhdH"
source_database: "NCBI RefSeq"
source_id: "gene-b3253"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3253"
  - "yhdH"
---

# yhdH

`gene.b3253`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3253`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdH (gene.b3253) is a gene entity. It encodes acuI (protein.P26646). Encoded protein function: FUNCTION: Probably catalyzes the NADPH-dependent reduction of acrylyl-CoA to propanoyl-CoA. {ECO:0000269|PubMed:22563425}. EcoCyc product frame: EG11315-MONOMER. EcoCyc synonyms: acuI. Genomic coordinates: 3403484-3404458.

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26646|protein.P26646]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010667,ECOCYC:EG11315,GeneID:947848`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3403484-3404458:+; feature_type=gene
