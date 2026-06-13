---
entity_id: "gene.b3658"
entity_type: "gene"
name: "selC"
source_database: "NCBI RefSeq"
source_id: "gene-b3658"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3658"
  - "selC"
---

# selC

`gene.b3658`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3658`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selC (gene.b3658) is a gene entity. EcoCyc product frame: selC-tRNA. EcoCyc synonyms: fdhC. Genomic coordinates: 3836222-3836316.

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

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=selC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011956,ECOCYC:EG30092,GeneID:948167`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:3836222-3836316:+; feature_type=gene
