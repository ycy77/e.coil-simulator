---
entity_id: "gene.b1989"
entity_type: "gene"
name: "asnV"
source_database: "NCBI RefSeq"
source_id: "gene-b1989"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1989"
  - "asnV"
---

# asnV

`gene.b1989`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1989`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnV (gene.b1989) is a gene entity. EcoCyc product frame: asnV-tRNA. Genomic coordinates: 2062260-2062335.

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

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=asnV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006605,ECOCYC:EG30022,GeneID:946509`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2062260-2062335:+; feature_type=gene
