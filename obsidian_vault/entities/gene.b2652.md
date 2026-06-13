---
entity_id: "gene.b2652"
entity_type: "gene"
name: "ileY"
source_database: "NCBI RefSeq"
source_id: "gene-b2652"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2652"
  - "ileY"
---

# ileY

`gene.b2652`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2652`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ileY (gene.b2652) is a gene entity. EcoCyc product frame: RNA0-305. Genomic coordinates: 2785762-2785837.

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

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ileY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008733,ECOCYC:G7387,GeneID:947163`
- `gbkey:Gene`
- `gene_biotype:tRNA`

## Notes

NC_000913.3:2785762-2785837:-; feature_type=gene
