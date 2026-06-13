---
entity_id: "gene.b0102"
entity_type: "gene"
name: "zapD"
source_database: "NCBI RefSeq"
source_id: "gene-b0102"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0102"
  - "zapD"
---

# zapD

`gene.b0102`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0102`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zapD (gene.b0102) is a gene entity. It encodes zapD (protein.P36680). Encoded protein function: FUNCTION: Cell division factor that enhances FtsZ-ring assembly. Directly interacts with FtsZ and promotes bundling of FtsZ protofilaments, with a reduction in FtsZ GTPase activity. {ECO:0000255|HAMAP-Rule:MF_01092, ECO:0000269|PubMed:22505682}. EcoCyc product frame: EG12313-MONOMER. EcoCyc synonyms: yacF. Genomic coordinates: 111856-112599.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36680|protein.P36680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000355,ECOCYC:EG12313,GeneID:944873`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:111856-112599:-; feature_type=gene
