---
entity_id: "gene.b1667"
entity_type: "gene"
name: "ydhR"
source_database: "NCBI RefSeq"
source_id: "gene-b1667"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1667"
  - "ydhR"
---

# ydhR

`gene.b1667`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1667`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydhR (gene.b1667) is a gene entity. It encodes ydhR (protein.P0ACX3). Encoded protein function: FUNCTION: May function as monooxygenase and play a role in the metabolism of aromatic compounds. {ECO:0000305}. EcoCyc product frame: G6895-MONOMER. Genomic coordinates: 1746700-1747005. EcoCyc protein note: A solution structure of YdhR has been determined; the protein belongs to the α/β barrel superfamily of proteins. Bioinformatic analysis suggests that it might function as a mono-oxygenase involved in the oxygenation of polyaromatic ring compounds . YdhR accumulates in response to exposure to uranium .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACX3|protein.P0ACX3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005572,ECOCYC:G6895,GeneID:946177`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1746700-1747005:+; feature_type=gene
