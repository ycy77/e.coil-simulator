---
entity_id: "gene.b1709"
entity_type: "gene"
name: "btuD"
source_database: "NCBI RefSeq"
source_id: "gene-b1709"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1709"
  - "btuD"
---

# btuD

`gene.b1709`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1709`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuD (gene.b1709) is a gene entity. It encodes btuD (protein.P06611). Encoded protein function: FUNCTION: Part of the ABC transporter complex BtuCDF involved in vitamin B12 import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01005}. EcoCyc product frame: BTUD-MONOMER. Genomic coordinates: 1792809-1793558. EcoCyc protein note: BtuD is the ATP-binding component of a high-affinity vitamin B12 uptake system; BtuB contains sequence motifs that are conserved in ATP binding cassette (ABC) proteins A Tn10 insertion in the btuCED promoter region restores colony-forming ability to an rne mutant. The suppression phenotype is reversed by overexpression of btuC, E or D .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06611|protein.P06611]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=btuD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005707,ECOCYC:EG10128,GeneID:945751`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1792809-1793558:-; feature_type=gene
