---
entity_id: "gene.b0057"
entity_type: "gene"
name: "yabQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0057"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0057"
  - "yabQ"
---

# yabQ

`gene.b0057`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0057`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yabQ (gene.b0057) is a gene entity. It encodes yabQ (protein.P39221). Encoded protein function: FUNCTION: Identified as a multicopy suppressor of the slow growth phenotype of an rsgA (yjeQ) deletion mutant. {ECO:0000269|PubMed:18223068}. EcoCyc product frame: EG12611-MONOMER. EcoCyc synonyms: b4659. Genomic coordinates: 59121-59279. EcoCyc protein note: yabQ is a multicopy suppressor of the slow growth phenotype of an G7841 rsgA deletion mutant .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39221|protein.P39221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000194,ECOCYC:EG12611,GeneID:38094933`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:59121-59279:+; feature_type=gene
