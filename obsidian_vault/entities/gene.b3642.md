---
entity_id: "gene.b3642"
entity_type: "gene"
name: "pyrE"
source_database: "NCBI RefSeq"
source_id: "gene-b3642"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3642"
  - "pyrE"
---

# pyrE

`gene.b3642`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3642`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrE (gene.b3642) is a gene entity. It encodes pyrE (protein.P0A7E3). Encoded protein function: FUNCTION: Catalyzes the transfer of a ribosyl phosphate group from 5-phosphoribose 1-diphosphate to orotate, leading to the formation of orotidine monophosphate (OMP). {ECO:0000255|HAMAP-Rule:MF_01208, ECO:0000269|PubMed:8620002}. EcoCyc product frame: OROPRIBTRANS-MONOMER. Genomic coordinates: 3815127-3815768.

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7E3|protein.P0A7E3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011904,ECOCYC:EG10808,GeneID:948157`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3815127-3815768:-; feature_type=gene
