---
entity_id: "gene.b1977"
entity_type: "gene"
name: "asnT"
source_database: "NCBI RefSeq"
source_id: "gene-b1977"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1977"
  - "asnT"
---

# asnT

`gene.b1977`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1977`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnT (gene.b1977) is a gene entity. EcoCyc product frame: asnT-tRNA. Genomic coordinates: 2044549-2044624.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=asnT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006560,ECOCYC:EG30020,GeneID:946488`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2044549-2044624:+; feature_type=gene
