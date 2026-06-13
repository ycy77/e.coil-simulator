---
entity_id: "gene.b1711"
entity_type: "gene"
name: "btuC"
source_database: "NCBI RefSeq"
source_id: "gene-b1711"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1711"
  - "btuC"
---

# btuC

`gene.b1711`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1711`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuC (gene.b1711) is a gene entity. It encodes btuC (protein.P06609). Encoded protein function: FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Involved in the translocation of the substrate across the membrane. EcoCyc product frame: BTUC-MONOMER. Genomic coordinates: 1794172-1795152. EcoCyc protein note: BtuC is the integral membrane component an ATP-dependent vitamin B12 uptake system. A Tn10 insertion in the btuCED promoter region restores colony-forming ability to an rne mutant. The suppression phenotype is reversed by overexpression of btuC, E or D .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06609|protein.P06609]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005712,ECOCYC:EG10127,GeneID:945877`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1794172-1795152:-; feature_type=gene
