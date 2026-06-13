---
entity_id: "gene.b0673"
entity_type: "gene"
name: "metT"
source_database: "NCBI RefSeq"
source_id: "gene-b0673"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0673"
  - "metT"
---

# metT

`gene.b0673`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0673`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metT (gene.b0673) is a gene entity. EcoCyc product frame: metT-tRNA. EcoCyc synonyms: metTalpha. Genomic coordinates: 697057-697133.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002290,ECOCYC:EG30058,GeneID:945280`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:697057-697133:-; feature_type=gene
