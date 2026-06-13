---
entity_id: "gene.b2846"
entity_type: "gene"
name: "yqeH"
source_database: "NCBI RefSeq"
source_id: "gene-b2846"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2846"
  - "yqeH"
---

# yqeH

`gene.b2846`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2846`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqeH (gene.b2846) is a gene entity. It encodes yqeH (protein.Q46941). Encoded protein function: Uncharacterized protein YqeH EcoCyc product frame: G7466-MONOMER. Genomic coordinates: 2987536-2988168. EcoCyc protein note: YqeH was predicted to regulate genes related to metabolism . Upstream of the yqeH gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yqeH gene is affected by conditions that generate general transcriptional termination in O157:H7 and MDS42 strains . yqeH is located within a remnant of an ETT2 (type III secretion system) pathogenicity island that is fully present in pathogenic strains such as E. coli O157:H7 and at least partially present in most sequenced E. coli and Shigella strains . ETT2 has been shown to contribute to pathogenesis .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46941|protein.Q46941]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yqeH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009349,ECOCYC:G7466,GeneID:945263`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2987536-2988168:+; feature_type=gene
