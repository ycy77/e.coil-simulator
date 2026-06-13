---
entity_id: "gene.b0506"
entity_type: "gene"
name: "allR"
source_database: "NCBI RefSeq"
source_id: "gene-b0506"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0506"
  - "allR"
---

# allR

`gene.b0506`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0506`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

allR (gene.b0506) is a gene entity. It encodes allR (protein.P0ACN4). Encoded protein function: FUNCTION: Negative regulator of allantoin and glyoxylate utilization operons. Binds to the gcl promoter and to the allS-allA intergenic region. Binding to DNA is abolished by glyoxylate. {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:12460564, ECO:0000269|PubMed:16546208}. EcoCyc product frame: G6276-MONOMER. EcoCyc synonyms: glxA3, ybbU. Genomic coordinates: 533011-533826. EcoCyc protein note: AllR (for "allantoin repressor") regulates several genes involved in the anaerobic utilization of allantoin as a nitrogen source . Inhibition of allR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic novobiocin . At very low concentrations of glyoxylate, AllR represses transcription from allAp, allSp, and gclp. A highly conserved region featuring an almost perfect palindromic sequence has been identified in gclp and in the intergenic region between the divergent promoters allAp and allSp. It has been proven that AllR binds to this region, and it has been proposed that it may interfere with RNA polymerase by steric hindrance or contact inhibition, thus repressing transcription. In the presence of glyoxylate (the coeffector molecule of this regulator), DNA binding by AllR is inhibited and transcription of the allantoin regulon is derepressed...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACN4|protein.P0ACN4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=allR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001750,ECOCYC:G6276,GeneID:945333`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:533011-533826:+; feature_type=gene
