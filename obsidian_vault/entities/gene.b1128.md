---
entity_id: "gene.b1128"
entity_type: "gene"
name: "roxA"
source_database: "NCBI RefSeq"
source_id: "gene-b1128"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1128"
  - "roxA"
---

# roxA

`gene.b1128`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1128`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

roxA (gene.b1128) is a gene entity. It encodes roxA (protein.P27431). Encoded protein function: FUNCTION: Growth-regulating oxygenase that catalyzes the hydroxylation of ribosomal protein uL16 on 'Arg-81'. {ECO:0000269|PubMed:23103944, ECO:0000269|PubMed:24530688}. EcoCyc product frame: EG11430-MONOMER. EcoCyc synonyms: ycfD. Genomic coordinates: 1187119-1188240.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27431|protein.P27431]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003802,ECOCYC:EG11430,GeneID:945391`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1187119-1188240:-; feature_type=gene
