---
entity_id: "gene.b0536"
entity_type: "gene"
name: "argU"
source_database: "NCBI RefSeq"
source_id: "gene-b0536"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0536"
  - "argU"
---

# argU

`gene.b0536`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0536`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argU (gene.b0536) is a gene entity. EcoCyc product frame: argU-tRNA. EcoCyc synonyms: dnaY, pin. Genomic coordinates: 564723-564799.

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=argU; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001840,ECOCYC:EG30014,GeneID:945161`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:564723-564799:+; feature_type=gene
