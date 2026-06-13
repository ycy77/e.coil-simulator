---
entity_id: "gene.b1284"
entity_type: "gene"
name: "yciT"
source_database: "NCBI RefSeq"
source_id: "gene-b1284"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1284"
  - "yciT"
---

# yciT

`gene.b1284`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1284`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciT (gene.b1284) is a gene entity. It encodes yciT (protein.P76034). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YciT EcoCyc product frame: G6638-MONOMER. EcoCyc synonyms: deoT. Genomic coordinates: 1343597-1344346. EcoCyc protein note: YciT was predicted to be a DeoR-type transcription factor using the Hidden Markov Model . DNA binding was probed by chromatin immunoprecipitation assays (ChIP-exo) . Consensus binding motif of YciT was found to be palindromic and approximately 16 nt: NTTTCANNTNAAANNN . Gene expression profile analysis of the wild-type strain and a yciT knockout strain using RNA-seq showed differential expression of a set of genes also identified by ChIP-exo (between others), indicating they are the direct regulatory targets of this transcription factor . RNA-seq studies and mutant phenotype analysis showed that YciT is involved in the control of osmolarity in E. coli . The deletion of the yciT gene did not affect significantly the growth in glucose, fructose, or sorbitol; however, in glucose and fructose the stationary phase was reached at an OD600 slightly lower than that for the wild-type strain . YciT belongs to the DeoR family of transcriptional regulators. Expression of malK, malE, pepN and fadA was downregulated in the presence of YciT; the effect could be indirect...

## Biological Role

Activated by lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76034|protein.P76034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yciT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004312,ECOCYC:G6638,GeneID:945869`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1343597-1344346:-; feature_type=gene
