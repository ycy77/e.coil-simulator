---
entity_id: "gene.b1372"
entity_type: "gene"
name: "stfR"
source_database: "NCBI RefSeq"
source_id: "gene-b1372"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1372"
  - "stfR"
---

# stfR

`gene.b1372`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1372`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

stfR (gene.b1372) is a gene entity. It encodes stfR (protein.P76072). Encoded protein function: Prophage side tail fiber protein homolog StfR (Side tail fiber protein homolog from lambdoid prophage Rac) EcoCyc product frame: G6695-MONOMER. EcoCyc synonyms: ynaB. Genomic coordinates: 1429049-1432411. EcoCyc protein note: stfR encodes a predicted tail fiber protein of the cryptic Rac prophage , and shows similarity to the e14 lambdoid prophage element . stfR encodes an interacting sequence tag which suggests StfR is a self-assembling protein . Expression of stfR decreased after addition of ZnSO4 to a minimal medium culture .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76072|protein.P76072]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=stfR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004595,ECOCYC:G6695,GeneID:945207`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1429049-1432411:+; feature_type=gene
