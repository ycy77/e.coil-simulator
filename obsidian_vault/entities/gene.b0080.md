---
entity_id: "gene.b0080"
entity_type: "gene"
name: "cra"
source_database: "NCBI RefSeq"
source_id: "gene-b0080"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0080"
  - "cra"
---

# cra

`gene.b0080`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0080`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cra (gene.b0080) is a gene entity. It encodes cra (protein.P0ACP1). Encoded protein function: FUNCTION: Global transcriptional regulator, which plays an important role in the regulation of carbon metabolism. Activates transcription of genes encoding biosynthetic and oxidative enzymes (involved in Krebs cycle, glyoxylate shunt and gluconeogenesis, such as ppsA and fbp). Represses genes involved in sugar catabolism, such as fruB, pfkA, pykF and adhE. Binds asymmetrically to the two half-sites of its operator. {ECO:0000269|PubMed:16115199, ECO:0000269|PubMed:8195118, ECO:0000269|PubMed:8230205, ECO:0000269|PubMed:8550429, ECO:0000269|PubMed:8577250, ECO:0000269|PubMed:8858581, ECO:0000269|PubMed:9084760, ECO:0000269|PubMed:9371462}. EcoCyc product frame: PD00521. EcoCyc synonyms: fruR, fruC, shl. Genomic coordinates: 88028-89032.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACP1|protein.P0ACP1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000299,ECOCYC:EG10338,GeneID:944804`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:88028-89032:+; feature_type=gene
