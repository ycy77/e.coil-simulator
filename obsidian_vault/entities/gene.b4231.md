---
entity_id: "gene.b4231"
entity_type: "gene"
name: "yjfF"
source_database: "NCBI RefSeq"
source_id: "gene-b4231"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4231"
  - "yjfF"
---

# yjfF

`gene.b4231`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4231`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjfF (gene.b4231) is a gene entity. It encodes yjfF (protein.P37772). Encoded protein function: FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. EcoCyc product frame: YJFF-MONOMER. Genomic coordinates: 4453583-4454578. EcoCyc protein note: Sequence analysis suggests that YjfF is the integral membrane protein of an ATP-binding cassette (ABC) transporter .

## Biological Role

Repressed by araC (protein.P0A9E0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37772|protein.P37772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=yjfF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013840,ECOCYC:EG12439,GeneID:948754`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4453583-4454578:+; feature_type=gene
