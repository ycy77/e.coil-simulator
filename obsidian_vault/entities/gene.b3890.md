---
entity_id: "gene.b3890"
entity_type: "gene"
name: "yiiF"
source_database: "NCBI RefSeq"
source_id: "gene-b3890"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3890"
  - "yiiF"
---

# yiiF

`gene.b3890`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3890`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiiF (gene.b3890) is a gene entity. It encodes yiiF (protein.P0AFU6). Encoded protein function: Uncharacterized protein YiiF EcoCyc product frame: EG11855-MONOMER. Genomic coordinates: 4079751-4079969. EcoCyc protein note: YiiF appears to belong to the AraC family of transcription factors, and it was predicted to regulate genes related to metabolism . Upstream of the yiiF gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yiiF gene is affected by glucose-lactose shift and conditions that generate general transcriptional termination . A transposon insertion in the intergenic region between yiiE and yiiF, which potentially affects expression of yiiF, confers increased resistance to thymol .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFU6|protein.P0AFU6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yiiF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012700,ECOCYC:EG11855,GeneID:948385`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4079751-4079969:+; feature_type=gene
