---
entity_id: "gene.b0082"
entity_type: "gene"
name: "rsmH"
source_database: "NCBI RefSeq"
source_id: "gene-b0082"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0082"
  - "rsmH"
---

# rsmH

`gene.b0082`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0082`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmH (gene.b0082) is a gene entity. It encodes rsmH (protein.P60390). Encoded protein function: FUNCTION: Specifically methylates the N4 position of cytidine in position 1402 (C1402) of 16S rRNA. In vitro, active on the assembled 30S subunit, but not naked 16S rRNA or 70S ribosomes. {ECO:0000269|PubMed:10572301, ECO:0000269|PubMed:19965768}. EcoCyc product frame: EG11085-MONOMER. EcoCyc synonyms: yabC, mraW. Genomic coordinates: 90094-91035.

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60390|protein.P60390]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=rsmH; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=rsmH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000304,ECOCYC:EG11085,GeneID:944806`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:90094-91035:+; feature_type=gene
