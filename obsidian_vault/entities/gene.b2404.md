---
entity_id: "gene.b2404"
entity_type: "gene"
name: "lysV"
source_database: "NCBI RefSeq"
source_id: "gene-b2404"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2404"
  - "lysV"
---

# lysV

`gene.b2404`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2404`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysV (gene.b2404) is a gene entity. EcoCyc product frame: lysV-tRNA. EcoCyc synonyms: supN. Genomic coordinates: 2521253-2521328.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=lysV; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007920,ECOCYC:EG30056,GeneID:946866`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2521253-2521328:+; feature_type=gene
