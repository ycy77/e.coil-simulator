---
entity_id: "gene.b1346"
entity_type: "gene"
name: "xisR"
source_database: "NCBI RefSeq"
source_id: "gene-b1346"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1346"
  - "xisR"
---

# xisR

`gene.b1346`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1346`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xisR (gene.b1346) is a gene entity. It encodes xisR (protein.P76057). Encoded protein function: FUNCTION: Induces the excision of the Rac prophage, a cryptic prophage that harbors several genes with important physiological functions (PubMed:26530864). XisR binds and shifts the right attachment site of Rac (PubMed:26530864). {ECO:0000269|PubMed:26530864}. EcoCyc product frame: G6677-MONOMER. EcoCyc synonyms: ydaQ. Genomic coordinates: 1413237-1413452. EcoCyc protein note: XisR is the excisionase of the Rac prophage. Excision of Rac is induced during biofilm formation and during stationary phase . Deletion of xisR leads to reduced Rac excision, while overexpression increases Rac excision . Increased expression of xisR during stationary phase is RpoS-dependent . XisR: "excisionase gene for Rac"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76057|protein.P76057]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004519,ECOCYC:G6677,GeneID:947399`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1413237-1413452:-; feature_type=gene
