---
entity_id: "gene.b1356"
entity_type: "gene"
name: "racR"
source_database: "NCBI RefSeq"
source_id: "gene-b1356"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1356"
  - "racR"
---

# racR

`gene.b1356`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1356`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

racR (gene.b1356) is a gene entity. It encodes racR (protein.P76062). Encoded protein function: FUNCTION: Transcriptional regulator that represses the expression of ydaS and ydaT under normal physiological conditions (PubMed:29205228, PubMed:29205229). It binds to its own upstream sequence and represses the adjacent and divergently coded ydaS-ydaT operon (PubMed:29205228). RacR-mediated down-regulation of ydaS and ydaT may be critical for cell survival (PubMed:29205229). RacR ensures that the prophage DNA is maintained in the genome (PubMed:38153127). When the expression of the racR gene is reduced, the prophage Rac is excised from the genome, possibly to counteract the lethal toxicity of YdaT (PubMed:38153127). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}. EcoCyc product frame: G6680-MONOMER. EcoCyc synonyms: rarC, ydaR. Genomic coordinates: 1419765-1420241.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76062|protein.P76062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004548,ECOCYC:G6680,GeneID:945899`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1419765-1420241:-; feature_type=gene
