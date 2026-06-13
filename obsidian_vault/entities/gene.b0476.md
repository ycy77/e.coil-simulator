---
entity_id: "gene.b0476"
entity_type: "gene"
name: "aes"
source_database: "NCBI RefSeq"
source_id: "gene-b0476"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0476"
  - "aes"
---

# aes

`gene.b0476`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0476`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aes (gene.b0476) is a gene entity. It encodes aes (protein.P23872). Encoded protein function: FUNCTION: Displays esterase activity towards short chain fatty esters (acyl chain length of up to 8 carbons). Able to hydrolyze triacetylglycerol (triacetin) and tributyrylglycerol (tributyrin), but not trioleylglycerol (triolein) or cholesterol oleate. Negatively regulates MalT activity by antagonizing maltotriose binding. Inhibits MelA galactosidase activity. {ECO:0000269|PubMed:11867639, ECO:0000269|PubMed:12374803, ECO:0000269|PubMed:9576853}. EcoCyc product frame: EG11101-MONOMER. EcoCyc synonyms: ybaC. Genomic coordinates: 499014-499973.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23872|protein.P23872]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001651,ECOCYC:EG11101,GeneID:947514`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:499014-499973:-; feature_type=gene
