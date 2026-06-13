---
entity_id: "gene.b4368"
entity_type: "gene"
name: "leuV"
source_database: "NCBI RefSeq"
source_id: "gene-b4368"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4368"
  - "leuV"
---

# leuV

`gene.b4368`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4368`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuV (gene.b4368) is a gene entity. EcoCyc product frame: leuV-tRNA. EcoCyc synonyms: leuValpha. Genomic coordinates: 4606079-4606165.

## Biological Role

Activated by fis (protein.P0A6R3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=leuV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014329,ECOCYC:EG30051,GeneID:948873`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4606079-4606165:-; feature_type=gene
