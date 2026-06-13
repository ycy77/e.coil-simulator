---
entity_id: "gene.b2398"
entity_type: "gene"
name: "yfeC"
source_database: "NCBI RefSeq"
source_id: "gene-b2398"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2398"
  - "yfeC"
---

# yfeC

`gene.b2398`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2398`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeC (gene.b2398) is a gene entity. It encodes yfeC (protein.P0AD37). Encoded protein function: Uncharacterized protein YfeC EcoCyc product frame: EG11431-MONOMER. Genomic coordinates: 2518467-2518811. EcoCyc protein note: YfeC was initially identified as a putative transcription factor using a homology-based algorithm . DNA binding was probed by chromatin immunoprecipitation assays (ChIP-exo) . Gene expression profile analysis of the wild-type strain and a yfeC knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo (between others), indicating they are the direct regulatory targets . Some of these direct regulatory targets were upregulated and others were downregulated, indicating that YfeC is a dual regulator . Consensus binding motif analysis showed that the TFBSs of YfeC have TTC-rich inverted repeats separated by 6 nt . Based on SWISS-MODEL, YfeC was predicted to form homodimers . The yfeCD locus was predicted to encode a toxin/antitoxin pair . However, no evidence for this function was found . Levels of extracellular DNA are increased in a yfeC deletion strain grown in liquid culture . The transcription of the yfeC gene is affected by temperature, oxidative stress and glucose-lactose shift...

## Biological Role

Activated by yfeC (protein.P0AD37).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD37|protein.P0AD37]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007907,ECOCYC:EG11431,GeneID:946857`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2518467-2518811:+; feature_type=gene
