---
entity_id: "gene.b2522"
entity_type: "gene"
name: "sseB"
source_database: "NCBI RefSeq"
source_id: "gene-b2522"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2522"
  - "sseB"
---

# sseB

`gene.b2522`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2522`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sseB (gene.b2522) is a gene entity. It encodes sseB (protein.P0AFZ1). Encoded protein function: FUNCTION: May be involved in the enhancement of serine-sensitivity. EcoCyc product frame: EG11601-MONOMER. Genomic coordinates: 2654157-2654933. EcoCyc protein note: Overexpression of sseA or sseB enhances the serine sensitivity caused by serine-mediated inhibition of ASPKINIHOMOSERDEHYDROGI-MONOMER homoserine dehydrogenase I activity during growth on some carbon sources . A transposon insertion mutation in sseB causes increased fimbrial production in an E. coli strain that exhibits K88 fimbriae . SseB: "serine sensitivity enhancing B"

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFZ1|protein.P0AFZ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sseB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008301,ECOCYC:EG11601,GeneID:946994`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2654157-2654933:-; feature_type=gene
