---
entity_id: "gene.b1373"
entity_type: "gene"
name: "tfaR"
source_database: "NCBI RefSeq"
source_id: "gene-b1373"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1373"
  - "tfaR"
---

# tfaR

`gene.b1373`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1373`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tfaR (gene.b1373) is a gene entity. It encodes tfaR (protein.P77163). Encoded protein function: Prophage tail fiber assembly protein homolog TfaR (Tail fiber assembly protein homolog from lambdoid prophage Rac) EcoCyc product frame: G6696-MONOMER. EcoCyc synonyms: ynaC. Genomic coordinates: 1432411-1432986. EcoCyc protein note: Transcription of tfaR is induced upon biofilm formation .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77163|protein.P77163]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tfaR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004597,ECOCYC:G6696,GeneID:946062`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1432411-1432986:+; feature_type=gene
