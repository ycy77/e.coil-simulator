---
entity_id: "gene.b3977"
entity_type: "gene"
name: "tyrU"
source_database: "NCBI RefSeq"
source_id: "gene-b3977"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3977"
  - "tyrU"
---

# tyrU

`gene.b3977`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3977`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrU (gene.b3977) is a gene entity. EcoCyc product frame: tyrU-tRNA. EcoCyc synonyms: sup15B, supM, supZ. Genomic coordinates: 4175472-4175556.

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

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=tyrU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013013,ECOCYC:EG30107,GeneID:948474`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:4175472-4175556:+; feature_type=gene
